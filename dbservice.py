import psycopg2


def get_data_from_db():
    conn = psycopg2.connect(
        host="localhost",
        database="dev",
        user="dev",
        password="dev")
    cur = conn.cursor()
    cur.execute('select * from Salaries')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
