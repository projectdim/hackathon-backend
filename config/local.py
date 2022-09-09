from pydantic import BaseSettings, Field, SecretStr


class DbSettings(BaseSettings):
    user: str = Field("postgres")
    password: SecretStr = Field("password")
    host: str = Field("db")
    database: str = Field("dim_db")
    port: int = Field("5432")

    class Config:
        env_prefix = "postgres_"


c = DbSettings()

config = {
    'database': 'dim_db',
    'user': c.user,
    'host': c.host,
    'password': c.password.get_secret_value(),
    'port': 5432
}
