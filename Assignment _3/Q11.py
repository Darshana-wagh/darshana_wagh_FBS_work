#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total_amount = 0

ticket_price = float(input("Enter ticket amount per person;"))

for i in range (1,6):
    age = int (input("Enter age of person:")) 

    if age < 12:
        discount = 0.30 * ticket_price
    elif age > 59:
        discount = 0.50* ticket_price
    else:
        discount = 0
        final_price = ticket_price - discount 
        total_amount += final_price

        print("total amount for 5 people : rs.", round (total_amount,2))