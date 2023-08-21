import sqlite3
conn=sqlite3.connect('quiz.db')
############## QUESTION ############
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(1,"what is the maximum possible length of an identifier in python","16","32","64","none of the above")')
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(2,"who developed the python language","zim Den","Gudio van Rossam","niene Stom","Dennis Ritchie")')
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(3,"In which year python language was developed","1995","1972","1981","1989")')
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(4,"In which year python 3.0 was developed","2008","2001","2010","none of the above")')
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(5,"wich character in python is used to make a single line comment","/","/* */","#","<!--->")')
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(6,"What is the function inside the class in python language","object","method","attribute","none of the above")')
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(7,"which of the following is not a keyword in python","val","raise","try","with")')
conn.execute('INSERT INTO Q (ID,QUESTION,A,B,C,D) VALUES(8,"which of the following operator is the correct option for power(ab)","a^b","a**b","a^^b","a Power(b)")')



############## ANSWER ##############
conn.execute('INSERT INTO ANS (ID,answer) VALUES(1,"d")')
conn.execute('INSERT INTO ANS (ID,answer) VALUES(2,"b")')
conn.execute('INSERT INTO ANS (ID,answer) VALUES(3,"d")')
conn.execute('INSERT INTO ANS (ID,answer) VALUES(4,"a")')
conn.execute('INSERT INTO ANS (ID,answer) VALUES(5,"c")')
conn.execute('INSERT INTO ANS (ID,answer) VALUES(6,"b")')
conn.execute('INSERT INTO ANS (ID,answer) VALUES(7,"a")')
conn.execute('INSERT INTO ANS (ID,answer) VALUES(8,"b")')


conn.commit()
conn.close()