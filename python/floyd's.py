#Q4. The following is called Floyd’s triangle:
#1
#2 3 
#4 5 6
#7 8 9 10
#12 13 14 11
#· · ·
#15
#Given a positive integer N, write a program that prints N rows of Floyd’s
#triangle, with the rows properly aligned

rows = int(input("Enter the Number of Rows:"))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):        
        print(number, end = '\t')
        number = number+1
    print()
