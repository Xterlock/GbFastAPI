from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings

DELIMITER = '__'


class DatabaseSettings(BaseModel):
    host: str
    port: str
    user: str
    name: str
    password: str
    driver: str = "postgresql+asyncpg"


class Settings(BaseSettings):
    db: DatabaseSettings

    class Config:
        env_nested_delimiter = DELIMITER

    def get_dsn(self, protocol=None) -> str:
        protocol = protocol or self.db.driver
        return f'{protocol}://{self.db.user}:{self.db.password}@{self.db.host}:{self.db.port}/{self.db.name}'


settings = Settings()
