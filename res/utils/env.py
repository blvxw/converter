import dotenv

def get_env_variable(key: str) -> str:
    return dotenv.get_key('.env', key)
