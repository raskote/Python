# Предварительно в dbeaver:
# CREATE TABLE users(
#     id serial PRIMARY KEY,
#     email varchar(256) NOT NULL,
#     password_field varchar(32) NOT NULL,
#     phone varchar(32)
#     registration_date TIMESTAMPTZ default Now()
# )
#
# insert into users(email, password_field, phone)
# values ('qqq@gmail.com', '3r342r2r', '+93434343312')
#
# select email, password_field, phone, registration_date::date from users;

# alter table users
# alter column user_name set NOT NULL;
# add column user_name varchar(256);
#
# update users
# set user_name = 'Alex Axe'
# where email = 'qqq@gmail.com';

import psycopg2
import names
import time
conn = psycopg2.connect(dbname='qa_ddl_f_1_200',
                        user='padawan_user_250',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

cursor = conn.cursor()

user_name = ''
user_email = ''
user_password = ''
user_field = ''

user_data_list = []
letters = string.ascii_letters
digits = string.digits
alplhabet = letter + digits
pwd_length = 12

count = 0

for i in range(0, 50):

    if conn:

        pwd = ''
        for i in range(pwd.length):
            pwd += ''.join(secrets.choice(alphabet))

        test_phone = '+90'
        for ii in range(phone_length):
            test_phone += ''.join(secrets.choice(digits))

        print(names.get_full_name())
        user_email = user_name.replace(' ', '.') + 'gmail.com'
        user_password = pwd
        user_phone = test_phone

        base_data = (user_email, user_password, user_phone, user_name)
        insert_query = """ inset into public.users(email, password_field, phone, user_name) values(%s, %s, %s, %s) """

        cursor.execute(insert_query, base_data)
        conn.commit()

        print('Set test_user', count, '---', base_data)
        count += 1
        time.sleep(.200)

# Для почистить базу:
# truncate_query = "truncate public.users"
# cursor.execute(truncate_query)

conn.commit()
cursor.close()

