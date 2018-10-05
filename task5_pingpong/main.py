import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


class Game(object):
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 600
    BALL_RADIUS = 20
    BALL_COLOR = '#FA4E05'
    PAD_VELOCITY = 4
    PAD_HEIGHT = 80
    PAD_WIDTH = 8

    frame = None

    score_left = 0
    score_right = 0
    ball_pos = []

    ball_vel = {'x': 0, 'y': 0, }
    paddles = {
        'left': {
            'position': {'start': {}, 'end': {}, },
            'velocity': 0,
        },
        'right': {
            'position': {'start': {}, 'end': {}, },
            'velocity': 0,
        }
    }

    def __init__(self):
        self.frame = simplegui.create_frame("Ping Pong", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw_game_window)
        self.frame.set_keyup_handler(self.keyup)
        self.frame.set_keydown_handler(self.keypress)
        self.frame.add_button("Start Over", self.create_game, 200)
        self.create_game()

    def create_game(self):
        self.reset_ball_state()
        self.generate_ball_velocity()

        self.paddles['left']['position'] = {
            'start': {'x': self.PAD_WIDTH, 'y': (self.CANVAS_HEIGHT / 2) - (self.PAD_HEIGHT / 2)},
            'end': {'x': self.PAD_WIDTH, 'y': (self.CANVAS_HEIGHT / 2) + (self.PAD_HEIGHT / 2)},
        }
        self.paddles['right']['position'] = {
            'start': {'x': self.CANVAS_WIDTH - self.PAD_WIDTH, 'y': (self.CANVAS_HEIGHT / 2) - (self.PAD_HEIGHT / 2)},
            'end': {'x': self.CANVAS_WIDTH - self.PAD_WIDTH, 'y': (self.CANVAS_HEIGHT) / 2 + (self.PAD_HEIGHT / 2)},
        }
        self.score_left = 0
        self.score_right = 0

    def keypress(self, key):
        if key == simplegui.KEY_MAP["W"]:
            self.paddles['left']['velocity'] = -self.PAD_VELOCITY
        elif key == simplegui.KEY_MAP["S"]:
            self.paddles['left']['velocity'] = self.PAD_VELOCITY
        elif key == simplegui.KEY_MAP["down"]:
            self.paddles['right']['velocity'] = self.PAD_VELOCITY
        elif key == simplegui.KEY_MAP["up"]:
            self.paddles['right']['velocity'] = -self.PAD_VELOCITY

    def keyup(self, key):
        if key == simplegui.KEY_MAP["W"] or key == simplegui.KEY_MAP["S"]:
            self.paddles['left']['velocity'] = 0
        elif key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["up"]:
            self.paddles['right']['velocity'] = 0

    def draw_game_window(self, canvas):
        canvas.draw_line(
            [self.CANVAS_WIDTH / 2, 0],
            [self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT],
            1, "White")
        canvas.draw_line(
            [self.PAD_WIDTH, 0],
            [self.PAD_WIDTH, self.CANVAS_HEIGHT],
            1, "White")
        canvas.draw_line(
            [self.CANVAS_WIDTH - self.PAD_WIDTH, 0],
            [self.CANVAS_WIDTH - self.PAD_WIDTH, self.CANVAS_HEIGHT],
            1, "White")
        canvas.draw_text(str(self.score_left) + " : " + str(self.score_right), [self.CANVAS_WIDTH / 2 - 20, 50], 24, 'white')

        self.generate_ball(canvas)
        self.generate_paddles(canvas)

    def generate_ball_velocity(self):
        allowed_values = [-4, -3, -2, 2, 3, 4]

        self.ball_vel['x'] = random.randrange(2, 6)
        self.ball_vel['y'] = random.choice(allowed_values)

    def generate_ball(self, canvas):
        self.change_ball_state()
        canvas.draw_circle(self.ball_pos, self.BALL_RADIUS, 1, self.BALL_COLOR, self.BALL_COLOR)

    def reset_ball_state(self):
        self.ball_pos = [self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2]

    def increase_ball_velocity(self):
        self.ball_vel['y'] *= 1.1
        self.ball_vel['x'] *= 1.1

    def change_ball_direction(self, direction):
        self.generate_ball_velocity()

        if direction == 'right':
            self.score_right += 1
        elif direction == 'left':
            self.ball_vel['x'] = -self.ball_vel['x']
            self.score_left += 1

    def change_ball_state(self):
        self.ball_pos[0] += self.ball_vel['x']
        self.ball_pos[1] += self.ball_vel['y']

        if (self.ball_pos[0] <= self.BALL_RADIUS):
            if (self.ball_pos[1] <= self.paddles['left']['position']['end']['y']
                    and self.ball_pos[1] > self.paddles['left']['position']['start']['y']):
                self.ball_vel['x'] *= -1
                self.increase_ball_velocity()
            else:
                self.reset_ball_state()
                self.change_ball_direction('right')

        elif (self.ball_pos[0] >= self.CANVAS_WIDTH - self.BALL_RADIUS - 1):
            if (self.ball_pos[1] <= self.paddles['right']['position']['end']['y']
                    and self.ball_pos[1] > self.paddles['right']['position']['start']['y']):
                self.ball_vel['x'] *= -1
            else:
                self.reset_ball_state()
                self.change_ball_direction('left')

        if ((self.ball_pos[1] <= self.BALL_RADIUS) or (self.ball_pos[1] >= self.CANVAS_HEIGHT - self.BALL_RADIUS - 1)):
            self.ball_vel['y'] *= -1

    def change_paddles_state(self):
        if ((self.paddles['left']['position']['start']['y'] + self.paddles['left']['velocity']) > 5
                and (self.paddles['left']['position']['end']['y'] + self.paddles['left']['velocity']) < self.CANVAS_HEIGHT - 5):
            self.paddles['left']['position']['start']['y'] += self.paddles['left']['velocity']
            self.paddles['left']['position']['end']['y'] += self.paddles['left']['velocity']

        if ((self.paddles['right']['position']['start']['y'] + self.paddles['right']['velocity']) > 5
                and (self.paddles['right']['position']['end']['y'] + self.paddles['right']['velocity']) < self.CANVAS_HEIGHT - 5):
            self.paddles['right']['position']['start']['y'] += self.paddles['right']['velocity']
            self.paddles['right']['position']['end']['y'] += self.paddles['right']['velocity']

    def generate_paddles(self, canvas):
        self.change_paddles_state()

        canvas.draw_line(
            [self.paddles['left']['position']['start']['x'], self.paddles['left']['position']['start']['y']],
            [self.paddles['left']['position']['end']['x'], self.paddles['left']['position']['end']['y']],
            12, 'Green')
        canvas.draw_line(
            [self.paddles['right']['position']['start']['x'], self.paddles['right']['position']['start']['y']],
            [self.paddles['right']['position']['end']['x'], self.paddles['right']['position']['end']['y']],
            12, 'Blue')

    def run(self):
        self.frame.start()


def main():
    ping_pong = Game()
    ping_pong.run()


if __name__ == '__main__':
    main()
