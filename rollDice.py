import random as ran

def rollDn(max: int, min = 1): #rolls a dice of size n, with a max of n and a default min of 1
    return ran.randint(min, max)

def rollD4(): #calls rDn func to prevent duplicate code
    return rollDn(4)   

def rollD6():
    return rollDn(6)  

def rollD8():
    return rollDn(8)   

def rollD10():
    return rollDn(10)   

def rollPercentile():
    return (rollD10() * 10) + rollD10() 

def rollD12():
    return rollDn(12)   

def rollD20():
    return rollDn(20)