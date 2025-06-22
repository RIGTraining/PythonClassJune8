name = input('Enter Your Name : ')
address = input('Enter Your Address')
first = int(input('Enter First Number'))
second = int(input('Enter Second Number'))

def Greet():
    print('Min Ga Lar Bar', name)

def add_number():
    res = first + second
    print(res)
    
Greet() #function calling
add_number()

