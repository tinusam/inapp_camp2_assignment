#Q3. The denominations in Indian currency are:
#|1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000.
#Given an amount N, print how many coins/notes make up N
#Sample input:
#Enter the amount: 2640
#Output:
#2000 1
#500 1
#100 1
#10 4
#Also test your program with N=3781, 4928, and 5134


currency = {2000:0,500:0,200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
amt = int(input("Enter the amount:"))


for i in currency.keys():
    if amt!=0:
        currency[i] = amt//i
        amt=amt%i
for i in currency.keys():
    if currency[i]!=0:
        print('%d:%d' %(i,currency[i]))