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


def import_data_in_db(rows):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="dev",
            user="dev",
            password="dev")
        cursor = connection.cursor()
        for i in rows:
            postgres_insert_query = """ INSERT INTO Salaries (id, first_name, last_name, salary) VALUES (%s,%s,%s,%s)"""
            record_to_insert = i
            cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")