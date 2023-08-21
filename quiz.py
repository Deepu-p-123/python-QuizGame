import sqlite3
import time
from datetime import date ,datetime

conn = sqlite3.connect('quiz.db')

name=input("enter your user name")
score=0

list1=['a','b','c','d']
cursor=conn.execute('SELECT * from Q')

for row in cursor:
    print(f"""
          {row[0]})   {row[1]} ?
          
                a){row[2]}    b){row[3]}  c){row[4]}  d){row[5]}
          """)
    
    while True:
        option=input("select your answer a,b,c or d -> \t")
        if option not in list1:
            print(" please choose a valid option [a,b,c,d]")
        else:
            break    
    
    cursor2=conn.execute(f'SELECT * from ANS where id={row[0]}')
    
    for i in cursor2:
        if row[0]==i[0]:
            if option ==i[1]:
                print("""
                         correct answer
                      """)
                score+=1
            else:
                 print("""
                          wrong answer
                      """)    

now=datetime.now()
# print(now)
day=now.strftime('%d-%m-%y')
time=now.strftime('%H : %M : %S')
# print(time)
# print(day)
     
conn.execute(f'INSERT INTO SCORE (NAME,SCORE,TIME,DATE) VALUES("{name}","{score}","{time}","{day}")')   
conn.commit() 
print(f" {name} you scored {score} ")    
   
conn.close()