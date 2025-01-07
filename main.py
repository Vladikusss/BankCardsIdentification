"""
The program should:
1. Accept a credit card number as input (could contain spaces or hyphens,
which needs to be cleaned appropriately).
2. Validate if it's a legitimate format based on the details below and
inform the user.
3. Identify the card type (Visa, Mastercard, Amex) and inform the user.
4. Format it according to the card type's standard format.
Card type details:
− Visa: 13 or 16 digits, starts with 4, formatted as XXXX XXXX XXXX
XXXX
− Mastercard: 16 digits, starts with 51-55, formatted as XXXX XXXX
XXXX XXXX
− American Express: 15 digits, starts with 34 or 37, formatted as XXXX
XXXXXX XXXXX
"""

card = input("Please enter bank card details: ").replace(" ", "").replace("-", "")

if card.startswith("4") and (len(card) == 13 or len(card) == 16):
    print("Type: Visa")
    print(" ".join([card[i:i+4] for i in range(0, len(card), 4)]))
elif card.startswith(("51", "52", "53", "54", "55")) and len(card) == 16:
    print("Type: Mastercard")
    print(" ".join([card[i:i+4] for i in range(0, len(card), 4)]))
elif card.startswith(("34", "37")) and len(card) == 15:
    print("Type: American Express")
    print(card[0:4], card[4:10], card[10:])
else:
    print("Invalid card format has been entered. Please try again.")
