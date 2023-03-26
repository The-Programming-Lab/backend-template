import os
from dotenv import load_dotenv


if "APP_ENV" in os.environ and os.environ['APP_ENV'] == 'production':
    hello_world = os.environ['HELLO_WORLD']
else:
    load_dotenv('.env')
    hello_world = os.getenv('HELLO_WORLD')

    