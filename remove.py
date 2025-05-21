# Discarding a specific item from a list
cards = ['Ace', 'King', 'Queen', 'Jack', '10']
discard_card = 'Queen'

if discard_card in cards:
    cards.remove(discard_card)

print("Remaining cards:", cards)
