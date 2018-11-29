import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


class Strings:
    GAME_TITLE = "Blackjack"

    HAND_CONTAINS = "Hand is"
    DECK_CONTAINS = "Deck is"
    HIT_OR_STAND = "Hit or Stand?"

    PLAYER_LOST_RESTART = "Player lost because of restart"

    PLAYER = "Player's %s"
    COMPUTER = "Computer's %s"

    BUSTED = "You got overflow"
    COMPUTER_BUSTED = "Computer got overflow"
    COMPUTER_BUSTED_STATUS = "Computer got overflow. You won"

    COMPUTER_WON = "Computer won"
    PLAYER_WON = "You won!"

    HIT = "HIT"
    DEAL = "DEAL"
    STAND = "STAND"


class Constants:
    # Interface size
    width = 800
    height = 600

    player_hand_pos = [100, 300]
    computer_hand_pos = [100, 150]

    # Initialize cards
    card_size = (73, 98)
    card_center = (36.5, 49)
    card_images = simplegui.load_image("https://i.imgur.com/uyt66L6.png")

    card_back_size = (71, 96)
    card_back_center = (35.5, 48)
    card_back = simplegui.load_image("https://i.imgur.com/nquI3Nb.png")

    suits = ('C', 'S', 'H', 'D')
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10,
              'K': 10}


class Card(Constants):
    def __init__(self, suit, rank):
        if (suit in self.suits) and (rank in self.ranks):
            self.suit = suit
            self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_location = (self.card_center[0] + self.card_size[0] * self.ranks.index(self.rank),
                         self.card_center[1] + self.card_size[1] * self.suits.index(self.suit))

        card_pos = [pos[0] + self.card_center[0], pos[1] + self.card_center[1]]

        canvas.draw_image(self.card_images, card_location, self.card_size, card_pos, self.card_size)


class Hand(Constants):
    def __init__(self):
        self.cards = []

    def __str__(self):
        result = ""
        for card in self.cards:
            result += " " + card.__str__()

        return Strings.HAND_CONTAINS + result

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        for card in self.cards: value += self.values[card.get_rank()]

        if value < 11 and any(card.get_rank for card in self.cards):
            value += 10

        return value

    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += 80


class Deck(Constants):
    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += " " + card.__str__()

        return Strings.DECK_CONTAINS + result


class Game(Constants):
    def __init__(self):
        self.game_is_active = False
        self.output = Strings.HIT_OR_STAND
        self.player_score = 0
        self.computer_score = 0

    def deal(self):
        if not self.game_is_active:
            self.deck = Deck()
            self.deck.shuffle()

            self.dealer_hand = Hand()
            self.player_hand = Hand()
            self.player_hand.add_card(self.deck.deal_card())
            self.player_hand.add_card(self.deck.deal_card())

            self.dealer_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

            print(Strings.PLAYER % self.player_hand)
            print(Strings.COMPUTER % self.dealer_hand)

            self.game_is_active = True
        else:
            self.computer_score += 1
            self.game_is_active = False
            self.output = Strings.PLAYER_LOST_RESTART

    def hit(self):
        if self.game_is_active:
            if self.player_hand.get_value() <= 21:
                self.player_hand.add_card(self.deck.deal_card())

            print(Strings.PLAYER % self.player_hand)

            if self.player_hand.get_value() > 21:
                self.output = Strings.BUSTED
                self.game_is_active = False
                print(self.output)

    def stand(self):
        if self.game_is_active:
            while self.dealer_hand.get_value() < 17:
                self.dealer_hand.add_card(self.deck.deal_card())

            print(Strings.COMPUTER % self.dealer_hand)

            if self.dealer_hand.get_value() > 21:
                self.output = Strings.COMPUTER_BUSTED
                self.player_score += 1
                print(Strings.COMPUTER_BUSTED_STATUS)
            else:
                if self.dealer_hand.get_value() >= self.player_hand.get_value() or self.player_hand.get_value() > 21:
                    self.output = Strings.COMPUTER_WON
                    self.computer_score += 1
                else:
                    self.output = Strings.PLAYER_WON
                    self.player_score += 1

                print(self.output)

            self.game_is_active = False

    def draw(self, canvas):
        canvas.draw_text(Strings.GAME_TITLE, [0.37 * self.width, 50], 50, "white")

        self.player_hand.draw(canvas, [10, 375])
        self.dealer_hand.draw(canvas, [10, 195])

        canvas.draw_text(self.output, [10, 100], 30, "red")

        canvas.draw_text(Strings.COMPUTER % self.computer_score, [10, 175], 20, "grey")
        canvas.draw_text(Strings.PLAYER % self.player_score, [10, 350], 20, "grey")

        if self.game_is_active:
            canvas.draw_image(self.card_back, self.card_back_center, self.card_back_size,
                              (46, 244), self.card_back_size)


class Interface:
    def __init__(self, game_object):
        self.game_object = game_object
        self._init_ui()

    def _init_ui(self):
        frame = simplegui.create_frame(Strings.GAME_TITLE, Constants.width, Constants.height)
        frame.set_canvas_background("#006400")

        frame.add_button(Strings.DEAL, self.game_object.deal, 150)
        frame.add_button(Strings.HIT, self.game_object.hit, 150)
        frame.add_button(Strings.STAND, self.game_object.stand, 150)
        frame.set_draw_handler(self.game_object.draw)
        frame.start()


def main():
    game_object = Game()
    game_object.deal()

    interface = Interface(game_object)


if __name__ == "__main__":
    main()


