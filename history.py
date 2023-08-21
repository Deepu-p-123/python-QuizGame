#### This file shows history of quiz game ####

import sqlite3
conn=sqlite3.connect('quiz.db')

cursor=conn.execute('SELECT * from SCORE')
print("""
            HISTORY
      """)
for row in cursor:
    print(f"""
          {row[0]})   NAME : {row[1]} 
          
                      SCORE :{row[2]}
                      
                      TIME : {row[3]}
                      
                      DATE : {row[4]}
          """)