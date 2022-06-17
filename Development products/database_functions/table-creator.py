import psycopg2

DB_NAME = "jwjuiwdg"
DB_USER = "jwjuiwdg"
DB_PASS = "o8dUXLTQev50L-yuZ8F8mRllAvFCoNke"
DB_HOST = "rajje.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password =  DB_PASS, host = DB_HOST, port = DB_PORT)

print("Database connected succesfully")

cur = conn.cursor()
cur.execute("""
CREATE TABLE Review_Data
(
id_Review UUID PRIMARY KEY NOT NULL,
url_Review TEXT NOT NULL,
body_Review TEXT NOT NULL,
rating_Review TEXT NOT NULL,
platform_Review TEXT NOT NULL,
locationId_Review TEXT NOT NULL,
userId_Review TEXT NOT NULL,
brandId_Review TEXT NOT NULL,
timeCreated_Review TIME NOT NULL
)
""")

conn.commit()
print("Table created sucessfully")
