import random
#we are creating a class called blackjackGame.
class BlackjacksGame:
    def __init__(self):                                        #The __init__ method initializes the class instance.
        self.deck = []                                         #deck: an empty list to store and represent the deck of cards in the game.
        self.player_hand = []                                  #player_hand: an empty list to store the player's hand and represents current hand of the player.
        self.dealer_hand = []                                  #dealer_hand: an empty list to store the dealer's hand and represents dealers hand of the player.
        self.actions = {"hit": self.hit, "stay": self.stay}    #actions:A dictionary where the keys are actions the player can take ("hit" or "stay")
        self.player_turn = True                                #player_turn: a boolean flag indicating whether it's currently the player's turn.

#The code initializes the game state with an empty deck and hands.
#The actions dictionary is used to associate user actions with corresponding methods. 
#The player_turn flag is set to True at the beginning, indicating that it's initially the player's turn.




    def initializing_cards(self):                                                   #createing a function to initialize cards
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]                           #createing the suit of the cards
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  #createing ranks of the cards
        self.deck = [{'suit': suit, 'rank': rank, 'value': min(index + 2, 10)} for index, rank in enumerate(ranks) for suit in suits]
        #Here, self.deck is created as a list of dictionaries, where each dictionary represents a card in the deck. Each card dictionary has three key-value pairs.
#self.deck is a list of dictionaries representing a standard deck of playing cards, and it serves as the source from which cards are drawn during the Blackjack game.

    def display_hand(self, hand):   #The display_hand method takes a hand parameter, which is a list of card dictionaries representing a player's or dealer's hand.
        return ', '.join([f"{card['rank']} of {card['suit']}" for card in hand])
    #It uses a list comprehension to create a string representation for each card in the hand, formatted as "Rank of Suit".
    #', '.join(...) concatenates these strings with commas between them, resulting in a human-readable representation of the hand.
    
    def shuffling_decks(self):          #The shuffling_decks method shuffles the deck using the random.shuffle function.
        random.shuffle(self.deck)       #It takes the self.deck attribute (the list representing the deck of cards) and shuffles it randomly.
        
        

    def Starting_cards(self):                                    #The Starting_cards method is called at the beginning of a round to deal two cards each to the player and the dealer.
        self.player_hand = [self.draw_card(), self.draw_card()]  #Starting_cards deals two cards each to the player and dealer.
        self.dealer_hand = [self.draw_card(), self.draw_card()]  #It assigns a list containing two drawn cards to self.player_hand and self.dealer_hand attributes.

    def draw_card(self):        #The draw_card method draws a card from the deck.
        return self.deck.pop()  #It uses self.deck.pop() to remove and return the last card from the deck, effectively simulating drawing a card from the top of the deck.

    def calculate_hand_value(self, hand):
        total = sum(card['value'] for card in hand)
        if total > 21 and any(card['rank'] == 'Ace' for card in hand):
            total -= 10
        return total

#The hand parameter represents a list of card dictionaries, typically the player's or dealer's hand.
#total is initially calculated as the sum of the 'value' attribute of each card in the hand.
#The method then checks if the total exceeds 21 and if there is at least one Ace in the hand. If both conditions are true, it means that there is at least one Ace in the hand, and treating it as 11 would result in a bust (total > 21). In this case, it subtracts 10 from the total to account for the Ace being treated as 1 instead of 11.
#The final calculated total is then returned.
#This method is crucial for determining the value of a player's or dealer's hand in the game of Blackjack, considering the flexible value of Aces. The goal is to have a hand with a total value as close to 21 as possible without exceeding it.

    def hit(self):
        if self.player_turn:
            self.player_hand.append(self.draw_card())
            print("You drew a card:", self.display_hand([self.player_hand[-1]]))
            print("Your hand:", self.display_hand(self.player_hand))
            if self.calculate_hand_value(self.player_hand) > 21:
                print("Bust! You lose.")
                self.player_turn = False
        else:
            self.dealer_hand.append(self.draw_card())
            print("Dealer drew a card:", self.display_hand([self.dealer_hand[-1]]))
            print("Dealer's hand:", self.display_hand(self.dealer_hand))

#The hit method checks if it is currently the player's turn (self.player_turn). If it is, the player is allowed to draw a card.
#For the player's turn:
#It appends the drawn card to the player's hand (self.player_hand).
#Prints the drawn card and the updated player's hand.
#Checks if the new total value of the player's hand exceeds 21. If so, it prints a message indicating that the player has busted, updates self.player_turn to False to end the player's turn, and the game will proceed to the dealer's turn.
#For the dealer's turn:
#It appends the drawn card to the dealer's hand (self.dealer_hand).
#Prints the drawn card and the updated dealer's hand.
#This hit method is an essential part of the game loop, allowing the player and dealer to draw cards during their respective turns.

    def stay(self):
        if self.player_turn:
            self.player_turn = False
            print("You chose to stay.")
        else:
            print("Dealer's turn:")
            while self.calculate_hand_value(self.dealer_hand) < 17:
                self.dealer_hand.append(self.draw_card())
                print("Dealer drew a card:", self.display_hand([self.dealer_hand[-1]]))
                print("Dealer's hand:", self.display_hand(self.dealer_hand))
            self.determine_winner()

#The stay method checks if it is currently the player's turn (self.player_turn). If it is, the player has chosen to stay, and the method updates self.player_turn to False to end the player's turn.
#If it is not the player's turn, it means it is the dealer's turn.
#It prints a message indicating that it is the dealer's turn.
#The dealer draws cards until the total value of their hand is 17 or higher. This is a common rule in Blackjack where the dealer must draw cards until their total is at least 17.
#The drawn cards and the updated dealer's hand are printed during each iteration of the while loop.
#After the dealer's turn is completed, the determine_winner method is called to decide the winner of the round.
#This stay method is a key part of the game logic, handling the player's decision to stay and then simulating the dealer's actions until they reach a total value of 17 or higher. The winner is then determined based on the total values of the player's and dealer's hands.

    def determine_winner(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        print("Your hand:", self.display_hand(self.player_hand))
        print("Dealer's hand:", self.display_hand(self.dealer_hand))

        if player_value > 21:
            print("Bust! You lose.")
        elif dealer_value > 21:
            print("Dealer bust! You win!")
        elif player_value == dealer_value:
            print("It's a tie!")
        elif player_value > dealer_value:
            print("You win!")
        else:
            print("Dealer wins!")
#player_value and dealer_value are calculated by calling the calculate_hand_value method for the player's and dealer's hands,
#respectively. This method takes into account the flexible value of Aces.
#The hands of both the player and the dealer are displayed using the display_hand method.
#The method then compares the total values of the player's and dealer's hands to determine the winner.
#If the player's total value exceeds 21, the player has busted, and the dealer wins.
#If the dealer's total value exceeds 21, the dealer has busted, and the player wins.
#If the total values are equal, it's a tie.
#If the player's total value is higher than the dealer's, the player wins.
#If the dealer's total value is higher than the player's, the dealer wins.
#This method plays a crucial role in concluding a round of Blackjack by presenting the hands, calculating the total values, and determining the winner based on the game rules.

    def play_game(self):
        print("Welcome to Complicated Blackjack!")

        while True:
            self.initializing_cards()
            self.shuffling_decks()
            self.Starting_cards()
            self.player_turn = True

            print("Your hand:", self.display_hand([self.player_hand[0]]))
            print("Dealer's hand:", self.display_hand([self.dealer_hand[0]]))

            if self.calculate_hand_value(self.player_hand) == 21:
                print("Blackjack! You win!")
            else:
                while self.player_turn:
                    action = input("Do you want to Hit or Stay? ").lower()
                    self.actions.get(action, lambda: None)()

                if self.calculate_hand_value(self.player_hand) <= 21:
                    self.stay()

            play_again = input("Do you want to play the game again with (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing the game ")
                break

#The method starts by printing a welcome message.
#It then enters a loop that represents a single round of Blackjack.
#It initializes the cards, shuffles the deck, and deals the starting cards.
#It displays the initial hands of the player and the dealer.
#It checks if the player has a Blackjack (an initial hand value of 21) and announces a win if so.
#If there is no Blackjack, it enters a loop for the player's turn, allowing them to choose whether to hit or stay.
#After the player's turn, it checks if the player's total value is 21 or less. If so, it proceeds to the dealer's turn.
#Finally, it asks the player if they want to play again. If the answer is not "yes," the loop breaks, and the game ends.
#This play_game method encapsulates the logic for playing multiple rounds of Blackjack and handling player decisions during each round.

if __name__ == "__main__":
    game = BlackjacksGame()
    game.play_game()
if __name__ == "__main__": checks if the script is being run as the main program, not imported as a module.

#Inside this block:

#game = BlackjacksGame() creates an instance of the BlackjacksGame class. 
#This initializes the game with an empty deck, player and dealer hands, and available actions.

#game.play_game() starts the main loop of the game by calling the play_game method on the game instance. 
#This is where the actual gameplay, including dealing cards, player decisions, and determining the winner, takes place.

#If the script is run directly, the Blackjack game will start. If it's imported as a module into another script, 
#the game won't start automatically, allowing the module to be used in other contexts without executing the game logic.

#Overall, the if __name__ == "__main__": block is a good practice for making scripts reusable as modules 
#while also providing a way to execute specific code when the script is run directly.






