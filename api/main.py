import psycopg2

from fastapi import FastAPI
from psycopg2.extras import RealDictCursor

from contextlib import contextmanager


app = FastAPI()


@contextmanager
def conn_context():
    """PostgreSQL connection context manager."""
    conn = psycopg2.connect(
        host="db", port=5432, password="parserPass-tsum_126", user="parser", dbname="parsing", 
        cursor_factory=RealDictCursor
    )
    psycopg2.extras.register_uuid()
    yield conn
    conn.close()

@app.get("/api/v1/recent_data")
def get_recent_data():
    with conn_context() as conn:
        curs = conn.cursor()
        curs.execute("select * from keng_ru where date = (select max(date) from keng_ru)")
        data = curs.fetchall()
        return data

