import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

ROCK_SPAWN_DELAY = 1500.0
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
missiles = []
asteroids = []
explosions = []
started = False


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        self.lifespan = lifespan if lifespan else float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png")
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
missile_info = ImageInfo([5, 5], [10, 10], 3, 100)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image1 = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
asteroid_image2 = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
asteroid_image3 = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")
asteroid_images = [asteroid_image1, asteroid_image2, asteroid_image3]
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image1 = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_image2 = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")
explosion_image3 = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")
explosion_image4 = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
explosion_images = [explosion_image1, explosion_image2, explosion_image2, explosion_image4]

soundtrack = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.ogg")
soundtrack.set_volume(0.7)
missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.ogg")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.ogg")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.ogg")


class Utils:
    @staticmethod
    def angle_to_vector(ang):
        return [math.cos(ang), math.sin(ang)]

    @staticmethod
    def dist(p, q):
        return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def game_start():
    global started, timer, lives, score

    score = 0
    lives = 3
    started = True
    timer.start()
    soundtrack.rewind()
    soundtrack.play()


def game_stop():
    global missiles, asteroids, started

    ship.clear_velocity()
    started = False
    timer.stop()
    missiles = []
    asteroids = []
    soundtrack.pause()


def create_explosion(pos):
    explosions.append(Sprite(pos, [0, 0], 0, 0, random.choice(explosion_images), explosion_info))


class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = list(info.get_center())
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def get_pos(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def draw(self, canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]],
                              self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        if self.thrust:
            acc = Utils.angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1

        self.vel[0] *= .99
        self.vel[1] *= .99

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()

    def increment_angle_vel(self):
        self.angle_vel += .08

    def decrement_angle_vel(self):
        self.angle_vel -= .08

    def clear_velocity(self):
        self.angle_vel = 0
        self.set_thrust(False)

    def shoot(self):
        global missiles
        forward = Utils.angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        missiles.append(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))


class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = list(info.get_center())
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def get_pos(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def check_life(self):
        return self.age < self.lifespan

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        self.age += 1
        if self.animated:
            self.image_center[0] += (self.image_size[0] * self.age)

        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

    def collide(self, other):
        return Utils.dist(self.pos, other.get_pos()) <= (self.radius + other.get_radius())


class Explosion(Sprite):
    def __init__(self, pos, vel, ang, ang_vel, image, info):
        super().__init__(pos, vel, ang, ang_vel, image, info)
        self.center = [50, 50]
        self.size = [100, 100]
        self.dim = [9, 9]
        self.pos = pos
        self.age = 0
        self.lifespan = 81

    def update(self):
        self.age += 1

    def draw(self, canvas):
        explosion_index = [self.age % self.dim[0], (self.age // self.dim[0]) % self.dim[1]]
        canvas.draw_image(explosion_images,
                          [self.center[0] + explosion_index[0] * self.size[0],
                           self.center[1] + explosion_index[1] * self.size[1]],
                          self.size, self.pos, self.size)


def keydown(key):
    if started:
        if key == simplegui.KEY_MAP['a']:
            ship.decrement_angle_vel()
        elif key == simplegui.KEY_MAP['d']:
            ship.increment_angle_vel()
        elif key == simplegui.KEY_MAP['w']:
            ship.set_thrust(True)
        elif key == simplegui.KEY_MAP['space']:
            ship.shoot()


def keyup(key):
    if started:
        if key == simplegui.KEY_MAP['a']:
            ship.increment_angle_vel()
        elif key == simplegui.KEY_MAP['d']:
            ship.decrement_angle_vel()
        elif key == simplegui.KEY_MAP['w']:
            ship.set_thrust(False)


def exit_handler():
    game_stop()
    timer.stop()
    frame.stop()


def click(pos):
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)

    if (not started) and inwidth and inheight:
        game_start()


def draw(canvas):
    global time, started, lives, score

    def group_collide(sprite, sprite_group):
        for item in list(sprite_group):
            if sprite.collide(item):
                create_explosion(item.get_pos())
                sprite_group.remove(item)
                return True

    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()

    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    ship.draw(canvas)
    for asteroid in asteroids:
        asteroid.draw(canvas)
    for missile in missiles:
        missile.draw(canvas)
    for explosion in explosions:
        explosion.draw(canvas)

    ship.update()
    for asteroid in list(asteroids):
        asteroid.update()
        if asteroid.collide(ship):
            create_explosion(asteroid.get_pos())
            explosion_sound.play()
            asteroids.remove(asteroid)
            lives -= 1
            if lives <= 0:
                game_stop()

    for missile in list(missiles):
        missile.update()
        if not missile.check_life():
            missiles.remove(missile)
        if group_collide(missile, asteroids):
            missiles.remove(missile)
            explosion_sound.play()
            score += 1

    for explosion in list(explosions):
        explosion.update()
        if not explosion.check_life():
            explosions.remove(explosion)

    canvas.draw_text("Lives: " + str(lives), [30, 50], 40, 'Red')
    canvas.draw_text("Score: " + str(score), [600, 50], 40, 'Red')

    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())


def rock_spawner():
    if len(asteroids) < 12:
        rock_image = random.choice(asteroid_images)
        spawn_pos, spawn_vel = [0, 0], [0, 0]

        spawn_vel[0] = random.randrange(3)
        spawn_vel[1] = random.randrange(3)

        spawn_sides = random.randrange(2)
        if spawn_sides:
            spawn_pos[0] = random.choice([0, WIDTH - 1])
            spawn_pos[1] = random.randrange(HEIGHT)

            if spawn_pos[0] != 0:
                spawn_vel[0] = -spawn_vel[0]
        else:
            spawn_pos[0] = random.randrange(WIDTH)
            spawn_pos[1] = random.choice([0, HEIGHT - 1])

            if spawn_pos[1] != 0:
                spawn_vel[1] = -spawn_vel[1]

        spawn_rotation = (random.randrange(15) / 130.0) * random.choice([-1, 1])
        spawn_angle = random.randrange(360)

        asteroids.append(Sprite(spawn_pos, spawn_vel, spawn_angle, spawn_rotation, rock_image, asteroid_info))

def main():
    global ship, timer, exit_button, frame

    frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
    ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

    frame.set_keyup_handler(keyup)
    frame.set_keydown_handler(keydown)
    frame.set_mouseclick_handler(click)
    frame.set_draw_handler(draw)

    timer = simplegui.create_timer(ROCK_SPAWN_DELAY, rock_spawner)
    exit_button = frame.add_button('Exit', exit_handler)

    frame.start()

if __name__ == "__main__":
    main()
