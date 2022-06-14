import psycopg2

DB_NAME = "jwjuiwdg"
DB_USER = "jwjuiwdg"
DB_PASS = "o8dUXLTQev50L-yuZ8F8mRllAvFCoNke"
DB_HOST = "rajje.db.elephantsql.com"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password =  DB_PASS, host = DB_HOST, port = DB_PORT)

    print("Database connected succesfully")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM review_data;
    ALTER TABLE review_data ALTER COLUMN id_review TYPE text;""")

    print("program ran sucessfully")


except:
    print("Database not fully connected")

finally:
        if conn is not None:
            conn.close()