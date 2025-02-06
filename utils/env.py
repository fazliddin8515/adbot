import os


def get_env(name: str) -> str:
    value = os.getenv(name)

    if value is None:
        raise RuntimeError(f"{name} isn't set in the environment")

    return value
