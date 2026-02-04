# Write a program to calculate profit or loss.
cost = int(input('Enter the cost:'))
Selling_price = int(input('Enter the selling price:'))
if(Selling_price>cost):
    print('profit')
elif(Selling_price<cost):
    print('loss')
else:
    print('no profit, no loss')