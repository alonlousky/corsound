from flask import Flask
import psycopg2
import redis
import json

app = Flask(__name__)

POSTGRES_CONNECTION = {
    'dbname': 'newdb',
    'user': 'postgres',
    'password': 'AlonAlon',
    'host': '127.0.0.1',
    'port': '5432'
}

REDIS_CONNECTION = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

def get_postgres_connection():
    return psycopg2.connect(**POSTGRES_CONNECTION)

def get_redis_connection():
    return redis.Redis(**REDIS_CONNECTION)

@app.route('/')
def fetch_data():
    postgres_conn = get_postgres_connection()
    redis_conn = get_redis_connection()

    # Query data from PostgreSQL
    cursor = postgres_conn.cursor()
    cursor.execute("SELECT * FROM new")
    data = cursor.fetchall()
    
    # Convert data to a JSON string
    data_str = json.dumps(data)


    # Cache data in Redis
    redis_conn.set('key', data_str)

    # Close connections
    cursor.close()
    postgres_conn.close()
    redis_conn.close()

    return 'Data fetched and cached successfully!'

if __name__ == '__main__':
    app.run()