import os
from dotenv import load_dotenv

def get_env_var(var_name: str) -> str:
    if "APP_ENV" in os.environ and os.environ['APP_ENV'] == 'production':
        return os.environ[var_name]
    else:
        return os.getenv(var_name)
    
if "APP_ENV" in os.environ and os.environ['APP_ENV'] == 'production':
    get_func = get_env_var
else:
    load_dotenv('.env')
    get_func = os.getenv


HELLO_WORLD = get_func('HELLO_WORLD')
    