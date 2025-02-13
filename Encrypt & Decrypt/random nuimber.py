import math
import random as r
sentence = str(input("Enter the message :"))

x1= r.randint(0,26)
x2= r.randint(0,26)
x3= r.randint(0,26)
y1= r.randint(0,26)
y2= r.randint(0,26)
y3= r.randint(0,26)
randsentence = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(len(randsentence))

rand1 = randsentence[x1] + randsentence[x2] + randsentence[x3]
# print(rand1)
rand2 = randsentence[y1] + randsentence[y2] + randsentence[y3]
print(f"{rand1}{sentence[1:]}{sentence[0]}{rand2}")