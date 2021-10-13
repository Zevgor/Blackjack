#CLASS FOR CARD, POSSIBLY USE INSTEAD OF OTHERS???

class card: 
    def __init__(self,val,suit,bjval): 
        self.val = val
        self.bjval = bjval
        self.suit = suit
                
def makestandarddeck():
 #mydeck = [r+s for r in '23456789TJQKA' for s in 'SHCD']
 mydeck=[]
 for r in '23456789TJQKA':
  for s in 'SHCD':
   if r.isnumeric():
     bjval=r
   else:
    if r == "A":
     bjval=11
    else:
     bjval=10
   mydeck.append(card(r,s,bjval))
 return mydeck

sdeck=makestandarddeck()
alldecks=[]
for i in range(4):
 for card in sdeck:
  alldecks.append(card)

for card in alldecks:
  print(card.val,card.suit,card.bjval,end=". ")