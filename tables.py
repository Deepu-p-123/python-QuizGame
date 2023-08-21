#file for creating tables

import sqlite3
conn = sqlite3.connect('quiz.db')

conn.execute('''
             CREATE TABLE Q
             (ID INT PRIMARY KEY NOT NULL,
             QUESTION TEXT NOT NULL,
             A CHAR(50),
             B CHAR(50),
             C CHAR(50),
             D CHAR(50));
             ''')


# ### TABLE FOR ANSWER KEY #########
conn.execute('''
             CREATE TABLE ANS
             (ID INT PRIMARY KEY NOT NULL,
             
             answer CHAR(50));
             ''')
print("table created successfully")

# ########### TABLE FOR SCORE ########

conn.execute('''CREATE TABLE SCORE 
             (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
             NAME CHAR(50),
             SCORE INT,
             TIME TEXT,
             DATE TEXT
             )
            
             ''')

# conn.execute("drop table SCORE")

conn.close()