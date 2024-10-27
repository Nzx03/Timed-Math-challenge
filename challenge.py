import random
import time

print("Welcome to Timed Math challenge!")
start=int(input("Enter the start value (e.g., 2):"))
finish=int(input("Enter the start value (e.g., 45):"))
oper=["+","-","*"]
total_prob=int(input("Enter the total number of questions to solve:"))

def generate():
   first=random.randint(start,finish)
   last=random.randint(start,finish)
   operator=random.choice(oper)

   exp= str(first) + operator + str(last)
   answer=eval(exp)
   return exp,answer

start_time=time.time()
wrong=0
for i in range(total_prob):
   exp, answer=generate()
   while True:
    guess=input("Problem No"+ " " + str(i+1) + ":"+ " " + exp + "=")
    try:
           
           guess = int(guess)
           if guess == answer:
               break
           wrong+=1
           print("Oops! Wrong answer, try again.")
    except ValueError:
           print("Please enter a valid number.")

end_time=time.time()
total_time=round(end_time-start_time)
print("Nice try! You took",total_time,"seconds.")

    







   