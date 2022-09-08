class Card:

    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
        if self.value < 1 or self.value > 13:
            raise TypeError("card doesnt exist. ")

    def __gt__(self, other):
        """method that compering the values of cards to find out who is bigger"""
        if self.value == other.value:
            return self.symbol > other.symbol
        if self.value == 1:
            return True
        if other.value == 1:
            return False
        if self.value > other.value:
            return True
        else:
            return False

    # unit test
    def __eq__(self, other):
        """method that created for tests if we popped out a card and the card didn't stayed in the deck"""
        if self.value == other.value and self.symbol == other.symbol:
            return True
        else:
            return False

    def __repr__(self):
        if self.value == 1:
            return f"ACE of {self.symbol}"
        if self.value == 11:
            return f"JACK of {self.symbol}"
        if self.value == 12:
            return f"QUEEN of {self.symbol}"
        if self.value == 13:
            return f"KING of {self.symbol}"
        return f"{self.value} {self.symbol}"
