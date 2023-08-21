
import sqlite3
conn=sqlite3.connect('quiz.db')
################## INSERT QUERY ###############
def insert():
    id=int(input("enter the question number to be add"))
    question=input("enter your question -> \n")
    a=input("enter  option a \t")
    b=input("enter  option b \t")
    c=input("enter  option c \t")
    d=input("enter  option d \t")
    solution=input("enter the correct answer -> \t")
    conn.execute(f'INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES({id},"{question}","{a}","{b}","{c}","{d}")')
    conn.execute(f'INSERT INTO ANS (ID,answer) VALUES({id},"{solution}")')
    print('value inserted successfully')
    
############ UPDATE QUERY ###############   
def update():
    id=int(input("enter the question number to be add"))
    question=input("enter your question -> \n")
    a=input("enter  option a \t")
    b=input("enter  option b \t")
    c=input("enter  option c \t")
    d=input("enter  option d \t")
    solution=input("enter the correct answer -> \t")
    
    conn.execute(f"update ANS set answer='{solution}',QUESTION='{question}',A={a},B={b},c={c},d={d} where id={id}") 
    
    print("updated successfully")  
#################### DELETE #############################   
def delete():
    id=int(input("enter the question number to be delete"))
    conn.execute(f'delete from Q where id={id}')
    conn.execute(f'delete from ANS where id={id}')
############## DISPLAY #####################################    
def display():
    id=int(input("enter the question number to show ")) 
    cursor=conn.execute(f"SELECT * FROM Q WHERE id={id}")
    for row in cursor:
        print(f"""
          {row[0]})   {row[1]} ?
          
                a){row[2]}    b){row[3]}  c){row[4]}  d){row[5]}
                
          """)
    cursor2=conn.execute(f"SELECT * FROM ANS WHERE id={id}") 
    for row in cursor2:
        print(f"answer is {row[1]}")   
         
  

while True:
    
    x=int(input("choose an option 1-insert 2-update 3-delete 4-quit"))
    if x==1:
        insert()
        # conn.commit() 
    elif x==2:
        update()
        # conn.commit() 
    elif x==3:
        delete()
        # conn.commit() 
    elif x==4:
        # conn.close()
        break 
    elif x==5:
        display()       
conn.commit() 
conn.close()  
        