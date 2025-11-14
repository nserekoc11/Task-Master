#-1counter program
#Adding time for the countdown
import time as t

#input
num = int(input("Enter any number to count down from: "))

def countdown(n):
    if n < 0:
        print("Please enter a non-negative integer.")
countdown(num)

#countdown loop
while num >= 0:
    print(num)
    num -= 1
    t.sleep(1)  # Pause for 1 second between counts
    if num == -1:
        print("Countdown finished!")
