#ICS3U1-3
#November 21, 2021
#Fatima Rehan 
#This program will imitate the lotto max 


import random 
ticket = []

print("Welcome to Lotto Max! How many tickets would you like to buy?")
bought = int(input())

for i in range (bought):
    for i in range(7):                                  #have only 7 numbers
        x = random.randrange(0,50)                      #only include numbers from 0 to 50
        ticket.append(x)                                #add in the random numbers
    print("Your ticket numbers are", ticket, "!")       #display ticket numbers
    ticket.clear()                                      #clear tickets for next row
    print("Good Luck, Have a good day!")