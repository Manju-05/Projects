print("\n")
print("Hi Hello Namaste Vanakam...")
print("WELCOME TO ＭＥＥＬＯ　ＥＶＡＲＵ　ＰＯＴＵＧＡＤＵ．．")
print("nenu mee Computer Screen...!")

questions=[
    
    ["Who is the Captain of india cricket team?", "Rohit Sharma","MS Dhoni","Sachin Tendulkar","Bhumra",2],
    ["What is the capital of India?", "India","Bangladesh","Amaravati ","New Delhi",4],
    ["When was India’s independence day?", "15 August","15 july","26 January","25 August",1],
    ["Which is sturctured oriented language?", "C","C++","Java ","python",1],
    ["Which is object-oriented language?", "python","Maths","hindi","C",1],
    ["Who is the founder of FaceBook?", "NTR","Grahambell","Einstien","Mark Zuckerburg",4],
    ["Who is the founder of Google?", "Sundar Pichai","Grahambell","Einstien","Mark Zuckerburg",1],
    ["What is the full form of MG?", "Morning good","Morries Gan","Morries Garage","None of the above",3],
    ["What is the full form of Ip?", "Internet Package","Internet Protocol ","Internet person","None of the above",2],
    ["What is the full form of AP?", "Andhra Pradesh","Arunachal Pradesh ","Antarctica Pradesh ","None of the above",1],
    ["What is the full form of HTML?", "Hyper Text Marking Language","Hydralic Text Marking Language ","Hyper Text Markup Language","None of the above",3],
    ["What is the full form of CSS?", "canada south system","cascasde sheet style ","cascade style sheet","None of the above",3],
    ["Find Odd man Out?", "Scanner","Speaker ","Moniter","Headphones",1],
    ["which is first Hen or Egg?", "Hen","Egg ","Cock","Chicken",1],
           ]

levels=[1000,2000,3000,4000,5000,10000,20000,40000,50000,"1lakh", "25Lakhs","50Lakhs","75Lakhs","1Crore"]
Fixmoney=0

try:   
    for i in range(0,len(questions)):
        q = questions[i]
        print(f"\n---------------your {i+1} question for RS.{levels[i]}----------------")
        print(f"\nQ. {q[0]}")
        print(f"1.{q[1]} \t2.{q[2]}")
        print(f"3.{q[3]} \t4.{q[4]}")
        reply=int(input("Enter your Answer or Enter 7 to Quit : "))
        if(reply>4 or reply<=0):
            print("Enter the correct Option..🚫")
        if(reply == q[-1]):
            print(f"\nCorrect Answer✅✅ , You Won = RS.{levels[i]} ")
            if(i==4):
                Fixmoney=5000
            elif(i==9):
                Fixmoney="1Lakh"
            elif(i==14):
                Fixmoney="1Crore"
        elif(reply==7):
            print(f"\nYou have Quit the Game..! Final Amount You have won is {Fixmoney}")
            break
        else:
            print(f"\nWrong Answer..!❌❌ Restart the Game.. 🔄️! You have won  Rs.{levels[i]}")
            break
except Exception:
    print("Invalid Input ❌ Please Try Again..!")