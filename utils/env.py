import os


def get_env(name: str) -> str:
    value = os.getenv(name)

    if value is None:
        raise Exception(f"{name} isn't set on the environment")

    return value
