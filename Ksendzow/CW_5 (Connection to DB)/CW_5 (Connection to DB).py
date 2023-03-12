import psycopg2

conn = psycopg2.connect(dbname='qa_ddl_f_1_200',
                        user='padawan_user_200',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

cursor = conn.cursor()

if conn:
     print('Connection qa_ddl_f_1_200')
     sql_req = '''select * from salary'''
     cursor.execute(sql_req)
     req_result = cursor.fetchall()
     # print(cursor.description[1][0])
     for i in req_result:
         print('id =', i[0], ' -- salary =', i[1])
    conn.commit()   #соединение с базой закрыть
    conn.close()    #соединение с базой закрыть