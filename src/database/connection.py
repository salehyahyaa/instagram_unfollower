import psycopg2
import os
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()

class Connection: 
    def get_connection():
        return psycopg2.connect(os.getenv("DB_URL"))

    def save_snapshot(usernames, snapshot_type):
        conn = get_connection()
        cur = conn.cursor()
        cur.executemany(
            "INSERT INTO snapshots (date, username, type) VALUES (%s, %s, %s)",
            [(date.today(), username, snapshot_type) for username in usernames]
        )
        conn.commit()
        cur.close()
        conn.close()

    def get_snapshot(snapshot_type, snapshot_date):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT username FROM snapshots WHERE type = %s AND date = %s",
            (snapshot_type, snapshot_date)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [row[0] for row in rows]

    def get_yesterday_mutuals():
        yesterday = date.today() - timedelta(days=1)
        return get_snapshot('mutual', yesterday)