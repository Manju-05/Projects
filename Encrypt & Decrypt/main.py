# write a python programm to translate the message into secret code language.Use the rules below to convert the normal english mesage into secret code.

# Coding: 
""" 
If  :
==> the word contains atleast 3 letters ,remove the first letter and apppend it to the end of the word.
==> now append the three random characters , at the starting and end of the words.
else :
==> simply reverse the string..
"""

# Decoding:
"""
==> if the word contains less than 3 characters, reverse it.
==> else:
remove 3 characters from start and end how remove the last letter and append it to the begginning..
"""

import random as r
x1= r.randint(0,27)
x2= r.randint(0,27)
x3= r.randint(0,27)
y1= r.randint(0,27)
y2= r.randint(0,27)
y3= r.randint(0,27)
randsentence = ["adv","bas","cew","das","evb","f89","gwt","hqw","dsf","ier","j23","kre","wl1","47m","asn","o24","paf","qts","r=h","sr4","hgj","uew","hxv","wfh","xgj","hgy","wez"]
print(len(randsentence))

rand1 = randsentence[x1]
rand2 = randsentence[y1]

choice = int(input("Press 1 To Encode\nPress 2 to Decode\nPress 3 to Cancel\n"))
match choice:
    case 1:
        Ensent = str(input("Enter the words to encode  "))
        words= Ensent.split(" ")
        nwords = []
        for word in words:
            if(len(word)>= 3):
                stnew =  rand1 + word[1:] + word[0] + rand2
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
    case 2:
        Desent = str(input("Enter the Characters to decode.."))
        words= Desent.split(" ")
        nwords = []
        for word in words:
            if(len(word)>= 3):
                stnew = word[3:-3]
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
    case 3:
        print("operation is cancelled..")
        exit()
    case _:
        print("please enter the valid number..!")
