from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    RABBITMQ_HOST: str
    RABBITMQ_PORT: str
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RESEND_EVENT_INTERVAL_SECONDS: float

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()