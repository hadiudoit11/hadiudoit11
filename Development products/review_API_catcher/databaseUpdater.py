import psycopg2

DB_NAME = "jwjuiwdg"
DB_USER = "jwjuiwdg"
DB_PASS = "o8dUXLTQev50L-yuZ8F8mRllAvFCoNke"
DB_HOST = "rajje.db.elephantsql.com"
DB_PORT = "5432"
conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("Database connected succesfully")

# This function opens a database connection and passes the arguments to the schema in the Review_Data table
# If bug: check the arguments in the function or in the execute command in the SQL
def runUpdated(id_Review, url_Review, body_Review, rating_Review, platform_Review, locationId_Review, userId_Review, brandId_Review, timeCreated_Review):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Review_Data
    (
    id_Review,
    url_Review,
    body_Review,
    rating_Review,
    platform_Review,
    locationId_Review,
    userId_Review,
    brandId_Review,
    timeCreated_Review
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """,
    ([id_Review], [url_Review], [body_Review], [rating_Review], [platform_Review], [locationId_Review], [userId_Review], [brandId_Review], [timeCreated_Review])
    )
    conn.commit()
    return\
        print("Table created sucessfully")

conn.close()