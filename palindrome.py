# number reverse and compare

Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
    print("\n number" , Number)
print("\n Reverse of entered number is = %d" %Reverse) 
    

# palindrome check
number = int(input("Please Enter any Number: ")) 
s = str(number)
reversed = s[::-1]
if s == reversed:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")