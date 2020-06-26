from flask import Flask
from settings import configs
from redis import Redis


app = Flask(__name__)
redis_db = Redis(**configs['REDIS'])


@app.route('/')
def hello_world():
    cached = redis_db.get('/')
    if cached:
        print("cached")
        return f"Hello Cached! {cached}"

    redis_db.set('/', configs["MESSAGE"])
    return f'Hello World! {configs["MESSAGE"]}'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
