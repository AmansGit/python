
cube = int(input("enter the value u want to find :: "))
epsilon = float(input("Enter epsilon value:: "))
increment = 0.0001
guess = 0.0
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses +=1
print("num_guesses = ",num_guesses)
if abs(guess ** 3 - cube) >= epsilon:
    print("Cube not found!!")
else:
    print(guess , 'is close to cube root of ' , cube)
