#-1counter program
#input
num = int(input("Enter any number to count down from: "))

def countdown(n):
    if n < 0:
        print("Please enter a non-negative integer.")
        return

#countdown loop
while num >= 0:
    print(num)
    num -= 1
    if num == 0:
        print("Countdown finished!")
        
