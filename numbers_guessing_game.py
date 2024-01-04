import random as r 
import math as m
lower=int(input('Enter lower bound:'))
upper=int(input('Enter upper bound'))
x=r.randint(upper,lower)

print= ("\n\tYou have only",round(m.log(upper-lower+1,2)),"chances to guess the number\n")

count = 0
while count<(m.log(upper-lower+1,2)):
    count+=1
    Guess=int(input("Guess the bnumber:"))
    if x==Guess:
        print("\nCongratulations! You have guesse the correct number in",count,"attempts.")
        break
    elif x>Guess:
        print("You guessed too low!")
    elif x<Guess:
        print("You have guessed too high!")
        
def new_func(print):
    print("\tBetter luck next time!")

if count>(m.log(upper-lower+1,2)):
    print("\nThe number is %d" %x)
    print("\tBetter luck next time!")
    
    
            
        
    


     
