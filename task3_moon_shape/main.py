import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

class Moon(object):
    TIMER_PHASE_INCREMENT = 0.02
    TIMER_DELAY = 100
    MOON_GLOW_COLOR = '#EBC815'
    CENTER_X = 50
    CENTER_Y = 50
    radius = 40
    phase = 0
    side = 0
    frame = None
    timer = None

    def __init__(self):
        self.frame = simplegui.create_frame("Moon Phases", 100, 100)
        self.frame.add_input("Enter moon phase", self.set_phase, 100)
        self.frame.add_button("Toggle Increment", self.create_timer, 100)
        self.frame.set_draw_handler(self.start_and_update)
        self.timer = simplegui.create_timer(self.TIMER_DELAY, self.increment_phase)

    def create_timer(self):
        if self.timer.is_running():
            self.timer.stop()
        else:
            self.timer.start()

    def set_phase(self, phase):
        self.phase = float(phase)

    def increment_phase(self):
        self.phase += self.TIMER_PHASE_INCREMENT

    def shadow_point(self, shadow_y_coord):
        x_temp = math.sqrt(self.radius ** 2 - (shadow_y_coord - self.CENTER_Y) ** 2)
        shadow_x_coord = self.side * math.cos(self.phase * math.pi) * (x_temp) + self.CENTER_X

        return [shadow_x_coord, shadow_y_coord]

    def start_and_update(self, canvas):
        limit = abs(math.sin(self.phase * math.pi))
        limit_point = math.cos(self.phase * math.pi)

        if limit > 0.2:
            canvas.draw_circle([self.CENTER_X, self.CENTER_Y], self.radius, 1, self.MOON_GLOW_COLOR, self.MOON_GLOW_COLOR)
            self.side = 1 if (math.sin(self.phase * math.pi) >= 0) else -1

            polygon_coords = [
                [self.CENTER_X - self.side * (self.radius + 2), self.CENTER_Y - self.radius],
                [self.CENTER_X, self.CENTER_Y - self.radius],
                self.shadow_point(self.CENTER_Y - self.radius),
                self.shadow_point(self.CENTER_Y - self.radius / 1.12),
                self.shadow_point(self.CENTER_Y - self.radius / 1.25),
                self.shadow_point(self.CENTER_Y - self.radius / 1.5),
                self.shadow_point(self.CENTER_Y - self.radius / 2),
                self.shadow_point(self.CENTER_Y - self.radius / 3),
                self.shadow_point(self.CENTER_Y - self.radius / 4),
                self.shadow_point(self.CENTER_Y - self.radius / 5),
                self.shadow_point(self.CENTER_Y - self.radius / 6),
                self.shadow_point(self.CENTER_Y - self.radius / 7),
                self.shadow_point(self.CENTER_Y),
                self.shadow_point(self.CENTER_Y + self.radius / 7),
                self.shadow_point(self.CENTER_Y + self.radius / 6),
                self.shadow_point(self.CENTER_Y + self.radius / 5),
                self.shadow_point(self.CENTER_Y + self.radius / 4),
                self.shadow_point(self.CENTER_Y + self.radius / 3),
                self.shadow_point(self.CENTER_Y + self.radius / 2),
                self.shadow_point(self.CENTER_Y + self.radius / 1.5),
                self.shadow_point(self.CENTER_Y + self.radius / 1.25),
                self.shadow_point(self.CENTER_Y + self.radius / 1.12),
                self.shadow_point(self.CENTER_Y + self.radius),
                [self.CENTER_X, self.CENTER_Y + self.radius],
                [self.CENTER_X - self.side * (self.radius + 2), self.CENTER_Y + self.radius],
            ]

            canvas.draw_polygon(polygon_coords, 1, 'black', 'black')
        else:
            if limit_point < 0:
                canvas.draw_circle([self.CENTER_X, self.CENTER_Y], self.radius, 1, self.MOON_GLOW_COLOR, self.MOON_GLOW_COLOR)


    def run(self):
        self.frame.start()


def main():
    moon = Moon()
    moon.run()


if __name__ == '__main__':
    main()
