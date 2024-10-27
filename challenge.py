import random
import time


start=2
finish=9
oper=["+","-","*"]
total_prob=10

def generate():
   first=random.randint(start,finish)
   last=random.randint(start,finish)
   operator=random.choice(oper)

   exp= str(first) + operator + str(last)
   answer=eval(exp)
#    print(exp,answer)
   return exp,answer

# generate()
start_time=time.time()
wrong=0
for i in range(total_prob):
   exp, answer=generate()
   while True:
    guess=input("Problem No"+ " " + str(i+1) + ":" + exp + "=")
    try:
           
           guess = int(guess)
           if guess == answer:
               break
           wrong+=1
    except ValueError:
           print("Please enter a valid number.")

end_time=time.time()
total_time=round(end_time-start_time)
print("Nice try! You took",total_time,"seconds")

    







   