import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


class Card(object):
    state = 0
    value = None

    def __init__(self, value):
        self.value = value

    def set_opened(self):
        self.state = 1

    def set_closed(self):
        self.state = 0

    def get_state(self):
        return self.state

    def get_value(self):
        return self.value


class Game(object):
    HEIGHT = 125
    CARD_COUNT = 16
    CARD_WIDTH = 60
    CARD_HEIGHT = 125

    pairs = []

    def __init__(self):
        self.initialize_game()

        self.frame = simplegui.create_frame("Memory Game", self.WIDTH, self.HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_mouseclick_handler(self.open_card)
        self.frame.add_button("Restart", self.initialize_game)
        self.label = self.frame.add_label("Turns: " + str(self.turns))

    def initialize_game(self):
        self.reset_pairs()
        self.WIDTH = self.CARD_COUNT * self.CARD_WIDTH
        self.turns = 0
        self.cards = [Card(i % (self.CARD_COUNT // 2)) for i in range(self.CARD_COUNT)]
        random.shuffle(self.cards)

    def start(self):
        self.frame.start()

    def increment_turns(self):
        self.turns = self.turns + 1

    def draw(self, canvas):
        self.label.set_text("Turns: " + str(self.turns))

        for i in range(self.CARD_COUNT):
            if self.cards[i].get_state() == 0:
                canvas.draw_polygon(
                    [(self.CARD_WIDTH * i, 0),
                     (self.CARD_WIDTH * i + self.CARD_WIDTH, 0),
                     (self.CARD_WIDTH * i + self.CARD_WIDTH, self.CARD_HEIGHT),
                     (self.CARD_WIDTH * i, self.CARD_HEIGHT)],
                    3, "red", "grey")
            else:
                canvas.draw_text(str(self.cards[i].get_value()), (self.CARD_WIDTH * i + 20, self.CARD_HEIGHT / 2 + 10),
                                 42, "white")

    def reset_pairs(self):
        self.pairs = [-1, -1]

    def open_card(self, position):
        current_card_index = position[0] // self.CARD_WIDTH

        if self.pairs[0] == -1 and self.cards[current_card_index].get_state() == 0:
            self.cards[current_card_index].set_opened()
            self.pairs[0] = current_card_index
        elif self.pairs[1] == -1 and self.cards[current_card_index].get_state() == 0:
            self.pairs[1] = current_card_index
            self.cards[current_card_index].set_opened()
            self.increment_turns()
        else:
            if self.cards[current_card_index].get_state() == 0:
                if self.cards[self.pairs[0]].get_value() != self.cards[self.pairs[1]].get_value():
                    for pair in self.pairs: self.cards[pair].set_closed()

                self.reset_pairs()
                self.cards[current_card_index].set_opened()
                self.pairs[0] = current_card_index


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
