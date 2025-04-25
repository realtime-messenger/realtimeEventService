from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    RABBITMQ_HOST: str
    RABBITMQ_PORT: str
    STOMP_PORT: str
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    PROTO_PORT: str

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()