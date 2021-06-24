def greet(name):
    '''takes name and greet user with given name'''
    print("Hello I go by "+ name) 

def name_input():
    '''Promts user for input and returns string'''
    x=input("What do you like people to call you?")
    return x  
    
z = name_input()
greet(z)

 


