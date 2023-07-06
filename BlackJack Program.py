from art import *
import random
import os

if __name__ == "__main__":
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    answer=input("would you like to play BlackJack: 'y' to play? ")
    while answer == 'y' or answer=='Y':      
        art_text = text2art("Blackjack")
        print(art_text)
        player_card=[random.choice(cards),random.choice(cards)]
        dealer_card=[random.choice(cards),random.choice(cards)]
        
        player_sum=sum(player_card)
        dealer_sum=sum(dealer_card)
        
        print(f"   Your cards: [{player_card}], current score: {player_sum}")
        print(f"   Dealer's first card: {dealer_card[0]}")

        if not(player_sum==21 or dealer_sum==21): 
            # player cards process
            new_card=input("Type 'y' to get another card: ")
            player_flag=True
            dealer_flag=True
            while new_card == 'y' or new_card=='Y':
                player_card.append(random.choice(cards))                
                player_sum=sum(player_card)
                
                if player_flag==True and player_sum>21 and 11 in player_card:
                    for x in range(len(player_card)):
                        if player_card[x]==11:
                            player_card[x]=1
                            player_flag=False
                            break
                    player_sum=sum(player_card)    
                            
                print(f"   Your cards: [{player_card}], current score: {player_sum}")
                print(f"   Dealer's first card: {dealer_card[0]}")

                if player_sum >=21:
                    break
                
                new_card=input("Type 'y' to get another card: ")

            # dealer cards process
            while dealer_sum<17:
                dealer_card.append(random.choice(cards))
                dealer_sum=sum(dealer_card)
                if dealer_flag==True and dealer_sum>21 and 11 in dealer_card:
                    for x in range(len(dealer_card)):
                        if dealer_card[x]==11:
                            dealer_card[x]=1
                            dealer_flag=False
                            break
                    dealer_sum=sum(dealer_card) 
            
        
        print(f"   Your final hand: [{player_card}], final score: {player_sum}")
        print(f"   Dealer final hand: [{dealer_card}], final score: {dealer_sum}")

        if player_sum>21:
            print("You loss.")
        elif player_sum == dealer_sum:
            print("You Tie")
        elif player_sum<21 and dealer_sum<21:
            if 21-player_sum>21-dealer_sum:
                print("You loss.")
            else:
                print("You Win")
        else:
            print("You Win")
        
            
        


        answer=input("would you like to play BlackJAck again: 'y' or 'n'? ")
        os.system('cls' if os.name == 'nt' else 'clear')

'''
if player_sum>21 or (21-player_sum>21-dealer_sum and dealer_sum<21):
            print("You loss.")
        elif 21-player_sum<21-dealer_sum:
            print("You Win")
        else:
            
'''
