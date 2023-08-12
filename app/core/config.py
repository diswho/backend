import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    EmailStr,
    HttpUrl,
    PostgresDsn,
    validator,
)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./xokthavy01.db"
    PROJECT_NAME: str = "xokthavy"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    # SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_KEY: str = "95f88b07ba43a7d438617ac171cb1b5e89a9bc716663405a2f5bb3851ef39f39"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    FIRST_SUPERUSER: str = "admin@xokthavy.com"

    FIRST_SUPERUSER_PASSWORD: str = (
        "95f88b07ba43a7d438617ac171cb1b5e89a9bc716663405a2f5bb3851ef39f39"
    )


# class Config:
#     env_file = ".env"

# SERVER_NAME: str
# SERVER_HOST: AnyHttpUrl
# SENTRY_DSN: Optional[HttpUrl] = None
# POSTGRES_SERVER: str
# POSTGRES_USER: str
# POSTGRES_PASSWORD: str
# POSTGRES_DB: str

# SMTP_TLS: bool = True
# SMTP_PORT: Optional[int] = None
# SMTP_HOST: Optional[str] = None
# SMTP_USER: Optional[str] = None
# SMTP_PASSWORD: Optional[str] = None
# EMAILS_FROM_EMAIL: Optional[EmailStr] = None
# EMAILS_FROM_NAME: Optional[str] = None
# EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
# EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
# EMAILS_ENABLED: bool = False
# EMAIL_TEST_USER: EmailStr = "test@example.com"
# FIRST_SUPERUSER: EmailStr
# FIRST_SUPERUSER_PASSWORD: str
# USERS_OPEN_REGISTRATION: bool = False


settings = Settings()
