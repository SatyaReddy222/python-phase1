# write a program to check the on road price of a bike under the conditions 
# i.if the price is greater than 72000 then income tax is 10% of the orginal price insurane will be 15% of the actual price 
# ii. if the price is greater than 150000 and less than 200000 the tax would be 25% and insurance will be 25%
# iii. if the price is above 200000 then tax will be 35% and insurance will be 28%
# iv.otherwise minimum price with us starts from 72k enter a vaild value
# acutal price +tax +insurance

price=int(input("enter the  price of the bike:"))
if(price>=72000 and price<150000):
    tax=(10/100)*price
    insurance=(15/100)*price
    on_road=price+tax+insurance
    print("the on-road price of the vehicle is",on_road)
elif(price>150000 and price < 200000):
    tax=(25/100)*price
    insurance=(25/100)*price
    on_road=price+tax+insurance
    print("the on-road price of the vehicle is",on_road)
elif(price > 200000):
    tax=(35/100)*price
    insurance=(28/100)*price
    on_road=price+tax+insurance
    print("the on-road price of the vehicle is",on_road)
else:
    print("minimum price with us starts from 72k enter a vaild value")

