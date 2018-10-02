import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Stopwatch(object):
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 500
    stopwatch_timer = None
    frame = None

    time = 0
    seconds = 0

    def __init__(self):
        self.frame = simplegui.create_frame("Stopwatch", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.add_button("Toggle", self.stopwatch_toggle)
        self.frame.add_button("Reset", self.stopwatch_reset)
        self.stopwatch_timer = simplegui.create_timer(100, self.stopwatch_change_state)

    def draw(self, canvas):
        canvas.draw_text(str(self.seconds), [self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2], 18, 'white')

    def stopwatch_change_state(self):
        self.time += 100
        self.seconds = self.time // 1000

    def format(self):
        pass
        # A:BC.D -> Minute:Seconds.Milliseconds

    def stopwatch_toggle(self):
        if self.stopwatch_timer.is_running():
            self.stopwatch_timer.stop()
        else:
            self.stopwatch_timer.start()

    def stopwatch_reset(self):
        if self.stopwatch_timer.is_running():
            self.stopwatch_timer.stop()
        self.time = 0
        self.seconds = 0

    def run(self):
        self.frame.start()

def main():
    stopwatch = Stopwatch()
    stopwatch.run()

if __name__ == '__main__':
    main()