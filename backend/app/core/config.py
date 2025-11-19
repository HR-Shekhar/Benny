from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_DB: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # SMTP settings for email
    SMTP_EMAIL: str
    SMTP_PASSWORD: str

    model_config = SettingsConfigDict(
        # Look for .env in backend root directory
        env_file=str(Path(__file__).resolve().parent.parent.parent / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
