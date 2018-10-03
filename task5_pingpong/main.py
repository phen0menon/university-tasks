import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Game(object):
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 600

    frame = None

    def __init__(self):
        self.frame = simplegui.create_frame("Ping Pong", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw_game_window)

    def draw_game_window(self):
        pass

    def run(self):
        self.frame.start()

def main():
    ping_pong = Game()
    ping_pong.run()

if __name__ == '__main__':
    main()