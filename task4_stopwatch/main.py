import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Stopwatch(object):
    STOPWATCH_TICKRATE = 100
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 500

    true_stop_count = 0
    stop_count = 0
    time = 0

    stopwatch_timer = None
    frame = None

    def __init__(self):
        self.stopwatch_timer = simplegui.create_timer(100, self.stopwatch_change_state)
        self.frame = simplegui.create_frame("Stopwatch", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.add_button("Toggle", self.stopwatch_toggle)
        self.frame.add_button("Reset", self.stopwatch_reset)
        self.frame.add_button("Magic Stop!", self.stopwatch_guess)

    def draw(self, canvas):
        canvas.draw_text(self.stopwatch_format(self.time), [self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2], 18, 'white')
        canvas.draw_text(
            str(self.true_stop_count) + " / " + str(self.stop_count),
            [self.CANVAS_WIDTH - 50, 20], 18, 'white')

    def stopwatch_change_state(self):
        self.time += self.STOPWATCH_TICKRATE

    def stopwatch_format(self, time):
        """
        >>> Stopwatch.stopwatch_format(Stopwatch, 0 * Stopwatch.STOPWATCH_TICKRATE)
        '0:00.0'
        >>> Stopwatch.stopwatch_format(Stopwatch, 11 * Stopwatch.STOPWATCH_TICKRATE)
        '0:01.1'
        >>> Stopwatch.stopwatch_format(Stopwatch, 321 * Stopwatch.STOPWATCH_TICKRATE)
        '0:32.1'
        >>> Stopwatch.stopwatch_format(Stopwatch, 613 * Stopwatch.STOPWATCH_TICKRATE)
        '1:01.3'
        """
        timestamp = time / 10

        minutes = str(int(timestamp // (self.STOPWATCH_TICKRATE * 60)))
        seconds = str(timestamp % (self.STOPWATCH_TICKRATE * 60) / self.STOPWATCH_TICKRATE)

        if int(float(seconds)) < 10:
            seconds = '0' + seconds[0:]

        return "{}:{}".format(minutes, seconds)

    def stopwatch_toggle(self):
        if self.stopwatch_timer.is_running():
            self.stopwatch_timer.stop()
        else:
            self.stopwatch_timer.start()

    def stopwatch_guess(self):
        if self.stopwatch_timer.is_running():
            self.stop_count += 1
            if self.time % 1000 == 0:
                self.true_stop_count += 1

    def stopwatch_reset(self):
        if self.stopwatch_timer.is_running():
            self.stopwatch_timer.stop()

        self.time = 0
        self.stop_count = 0
        self.true_stop_count = 0

    def run(self):
        self.frame.start()

def main():
    stopwatch = Stopwatch()
    stopwatch.run()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()
