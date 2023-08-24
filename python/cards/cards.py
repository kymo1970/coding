# Imports.
from tkinter import *
import random
from PIL import Image, ImageTk


def resizeCards(card):
    imgCard = Image.open(card)
    imgCardResized = imgCard.resize((150, 218))
    
    global imgResized
    imgResized = ImageTk.PhotoImage(imgCardResized)
    
    return imgResized


# Function for shuffling the cards.
def shuffle():
    suits = ["diamonds", "hearts", "clubs", "spades"]
    values = range(2, 15)
    
    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
            
    # print(deck)
    
    global dealer, player
    dealer = []
    player = []
    
    # Deal cards to dealer.
    card = random.choice(deck)
    print(card)
    # deck.remove(card)
    dealer.append(card)
    
    global imgDealer
    imgDealer = resizeCards(f'cardImages/{card}.png')
    lblDealer.config(image=imgDealer)
    
    # Deal cards to player.
    card = random.choice(deck)
    deck.remove(card)
    player.append(card)
    
    global imgPlayer
    imgPlayer = resizeCards(f'cardImages/{card}.png')
    lblPlayer.config(image=imgPlayer)
    
    # Display remaining cards in title bar.
    mw.title(f'KD - Cards -- {len(deck)} Cards left')
    
def dealCards():
    try:
        
        # Deal cards to dealer.
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        global imgDealer
        imgDealer = resizeCards(f'cards/cardImages/{card}.png')
        lblDealer.config(image=imgDealer)
        
        # Deal cards to player.
        card = random.choice(deck)
        deck.remove(card)
        player.append(card)
        global imgPlayer
        imgPlayer = resizeCards(f'cards/cardImages/{card}.png')
        lblPlayer.config(image=imgPlayer)
        
        # Display remaining cards in title bar.
        mw.title(f'KD - Cards {len(deck)} Cards left')
             
    except:
        
        mw.title("KD - Cards -- NO CARDS LEFT")
        

# Main Window(mw).
mw = Tk()
mw.title("KD - Cards")
mw.geometry("900x500")
mw.configure(background="green")

# Create frame for the dealer's and player's cards.
frmCards = Frame(mw, bg="green")
frmCards.pack(pady=20)

# Dealer frame and label.
lblFrameDealer = LabelFrame(frmCards, text="Dealer", bd=0)
lblFrameDealer.grid(row=0, column=0, padx=50, ipadx=20)
lblDealer = Label(lblFrameDealer, text="")
lblDealer.pack(pady=20)

# Player frame and label.
lblFramePlayer = LabelFrame(frmCards, text="Player", bd=0)
lblFramePlayer.grid(row=0, column=1, ipadx=20)
lblPlayer = Label(lblFramePlayer, text="")
lblPlayer.pack(pady=20)

# Buttons for shuffling and dealing cards.
btnShuffle = Button(mw, text="Shuffle Cards", font=("Helvetica", 14), command=shuffle)
btnShuffle.pack(pady=20)

btnDeal = Button(mw, text="Deal Cards", font=("Helvetica", 14), command=dealCards)
btnDeal.pack(pady=20)

shuffle()

# Mainloop for the program.
mw.mainloop()