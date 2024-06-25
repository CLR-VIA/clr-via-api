# Note: the module name is psycopg, not psycopg3
import psycopg
import os

POSTGRES_USER:str = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD:str = os.environ["POSTGRES_PASSWORD"]
POSTGRES_DB:str = os.environ["POSTGRES_DB"]
POSTGRES_SERVER:str = os.environ["POSTGRES_SERVER"]
POSTGRES_PORT:str = os.environ["POSTGRES_PORT"]
url:str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

def db_test()-> None:
    # Connect to an existing database
    with psycopg.connect(url) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute("""
                CREATE TABLE test (
                    id serial PRIMARY KEY,
                    num integer,
                    data text)
                """)

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)
            cur.execute(
                "INSERT INTO test (num, data) VALUES (%s, %s)",
                (100, "abc'def"))

            # Query the database and obtain data as Python objects.
            cur.execute("SELECT * FROM test")
            cur.fetchone()
            # will return (1, 100, "abc'def")

            # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
            # of several records, or even iterate on the cursor
            for record in cur:
                print(record)

            # Make the changes to the database persistent
            conn.commit()