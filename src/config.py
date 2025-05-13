from dataclasses import dataclass
import os

@dataclass
class EnvConfig:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_DB_ADDRESS: str = os.getenv("POSTGRES_DB_ADDRESS")
    POSTGRES_DB_PORT: int = int(os.getenv("POSTGRES_DB_PORT"))


ENV_CONFIG = EnvConfig()
