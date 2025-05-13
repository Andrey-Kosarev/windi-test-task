from dataclasses import dataclass
import os

@dataclass
class EnvConfig:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_DB_ADDRESS: str = os.getenv("POSTGRES_DB_ADDRESS")
    POSTGRES_DB_PORT: int = int(os.getenv("POSTGRES_DB_PORT"))


    def __post_init__(self):
        self.DB_URL = f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_DB_ADDRESS}:{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB}"

ENV_CONFIG = EnvConfig()
