import os
from flask import Flask, request, current_app
from get_Database import runGetDatabase as runGetDatabase
import psycopg2


app = Flask(__name__)

DB_NAME = "jwjuiwdg"
DB_USER = "jwjuiwdg"
DB_PASS = "o8dUXLTQev50L-yuZ8F8mRllAvFCoNke"
DB_HOST = "rajje.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password = DB_PASS, host = DB_HOST, port = DB_PORT)

cur = conn.cursor()
cur.execute("""SELECT body_Review FROM review_data;""")
database_Response = cur.fetchall()

body_Response = {
    'body_Review': []
}
body_Response['body_Review'].append('{}'.format(database_Response))

@app.route("/sms", methods=['GET','POST'])
def home():
    #
    conn.commit()
    return \
        body_Response

if __name__ == "__main__":
    app.run()