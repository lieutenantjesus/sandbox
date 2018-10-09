#Collatzfinal
#function w/if
#error checking
#while OUTSIDE OF FUNCTION

def collatz(num):
    if num % 2  == 0:
        print(num // 2)
        return(num // 2)

    elif num % 2 != 0:
        print((num * 3) + 1)
        return (num * 3) + 1

try:
    myNum = int(input('Please enter a number: '))
except ValueError:
    print('Error: Please type an integer.')
    
while myNum != 1:
    myNum = collatz(myNum)
else:
    print('You did it!')
