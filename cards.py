import cardfuncs as funcs
import json
import random

jsondeck = "deck.json"
deckcount = 4

#read standard deck
standarddeck = funcs.read_file(jsondeck)

#load full deck
fulldeck = []
count=0
while count < deckcount:
    count=count+1
    for k in standarddeck:
        fulldeck.append(k)

#confirm # of cards loaded to fulldeck
#funcs.cardsleft(fulldeck)

#deal starting cards, 1 to player, 1 to dealer, 1 to player, 1 to dealer (facedown)
dealercards = []
playercards = []

playercards.append(funcs.drawanother(fulldeck))
print ('Your first card is the', playercards[-1]["value"], 'of', playercards[-1]["suit"])

dealercards.append(funcs.drawanother(fulldeck))
print ('Dealer first card is the', dealercards[-1]["value"], 'of', dealercards[-1]["suit"])

playercards.append(funcs.drawanother(fulldeck))
print ('Your second card is the', playercards[-1]["value"], 'of', playercards[-1]["suit"])

card = funcs.drawanother(fulldeck)
dealercards.append(card)
print ('Dealer second card is facedown')

#calculate dealers and players value
dealervalue = funcs.calcvalue(dealercards)
print ('Dealer showing a',dealercards[0]["bjval"])
playervalue = funcs.calcvalue(playercards)
print ('Your value is',playervalue)

if dealervalue == 21:
    print ('Dealer Blackjack - You Lose!')
    quit()

if playervalue == 21:
    print ('BLACKJACK!!!!!')

#player hit or stand
userinput = ''
while (playervalue < 21) and (userinput != 's'):
    userinput = input('Hit or Stand? ')
    if userinput == 'h':
        playercards.append(funcs.drawanother(fulldeck))
        print ('Player next card is the', playercards[-1]["value"], 'of', playercards[-1]["suit"])
        playervalue = funcs.calcvalue(playercards)
        print ('Your value is',playervalue)


playervalue = funcs.calcvalue(playercards)
print ('Your final value is:',playervalue)

print ('Dealer second card is the', dealercards[-1]["value"], 'of', dealercards[-1]["suit"])

#dealer takes more cards if < 17
while dealervalue < 17:
    print ('dealer hitting...')
    dealercards.append(funcs.drawanother(fulldeck))
    print ('Dealer next card is the', dealercards[-1]["value"], 'of', dealercards[-1]["suit"])
    dealervalue = funcs.calcvalue(dealercards)

print('Dealer final value:',dealervalue)

#win and lose conditions
if dealervalue > 21:
    print ('Dealer Bust!')
if (playervalue > 21):
    print('You Lose!')
if (playervalue < 22) and (dealervalue < 22 and dealervalue > playervalue):
    print('You Lose!')
if (playervalue < 22 and dealervalue < 22 and playervalue == dealervalue):
    print ('Push! No winner.')
if ((playervalue < 22) and ((dealervalue < playervalue) or (dealervalue > 21))) :
    print ('You Win!')