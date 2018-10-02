import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Stopwatch(object):
    STOPWATCH_TICKRATE = 100
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 500

    time = 0

    stopwatch_timer = None
    frame = None

    def __init__(self):
        self.stopwatch_timer = simplegui.create_timer(100, self.stopwatch_change_state)
        self.frame = simplegui.create_frame("Stopwatch", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.add_button("Toggle", self.stopwatch_toggle)
        self.frame.add_button("Reset", self.stopwatch_reset)

    def draw(self, canvas):
        canvas.draw_text(self.format(), [self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2], 18, 'white')

    def stopwatch_change_state(self):
        self.time += self.STOPWATCH_TICKRATE

    def format(self):
        timestamp = self.time / 10

        minutes = str(int(timestamp // (self.STOPWATCH_TICKRATE * 60)))
        seconds = str(timestamp % (self.STOPWATCH_TICKRATE * 60) / self.STOPWATCH_TICKRATE)

        if int(float(seconds)) < 10:
            seconds = '0' + seconds[0:]

        return minutes + ":" + seconds

    def stopwatch_toggle(self):
        if self.stopwatch_timer.is_running():
            self.stopwatch_timer.stop()
        else:
            self.stopwatch_timer.start()

    def stopwatch_reset(self):
        if self.stopwatch_timer.is_running():
            self.stopwatch_timer.stop()
        self.time = 0

    def run(self):
        self.frame.start()

def main():
    stopwatch = Stopwatch()
    stopwatch.run()

if __name__ == '__main__':
    main()