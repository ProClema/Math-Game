import random
import os
from time import sleep

def math_sum():   # a first function for x1+x2
    number1 =random.randint(11,100)   #number sort between 11 and 99
    number2= random.randint(11,100)
    print('{} + {}'.format(number1,number2))
    answer = int(input())
    if answer == number1+number2:
        print(answer)
        print("Well done")
        sleep(0.25) # user can read for a short time
    else:
        print('Wrong answer')
        sleep(0.25)

def difference():
    while True:
        number1 = random.randint(2, 99)
        number2 = random.randint(11, 100)

        if number2 - number1 > 0:
            print('{} - {}'.format(number2, number1))
            answer = int(input())
            if answer == number2 - number1:
                    print(answer)
                    print("Well done")
                    sleep(0.25)
            else:
                 print('Wrong answer')
                 sleep(0.25)
            break
        else:
            continue

def multiplication():
    number1 = random.randint(11, 100)
    number2 = random.randint(11, 100)
    print('{}*{}'.format(number1, number2))
    answer = int(input())
    if answer == number1 * number2:
        print(answer)
        print("Well done")
        sleep(0.25)
    else:
        print('Wrong answer')
        sleep(0.25)
def quocient():
    while True:
        number1 = random.randint(2, 99)
        number2 = random.randint(11, 100)

        if number2 % number1 == 0 and number2/number1>1:   # no equal numbers
            print('{}/{}'.format(number2, number1))
            answer = int(input())
            if answer == number2/number1:
                print(answer)
                print("Well done")
            else:
                print('Wrong answer')
            break
        else:
            continue

math_sum()
os.system('clear') # for os Linux or Mac for windowa insted of clear use cls
difference()
os.system('clear')
multiplication()
os.system('clear')
quocient()
os.system('clear')
