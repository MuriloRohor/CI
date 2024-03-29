from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[1] / '.env', 
        env_file_encoding='utf-8',
        extra="ignore"
    )

    DATABASE_PASSWORD: str
    DATABASE_USER: str
    DATABASE_DB: str
    
    @property
    def DATABASE_URL(self):
        
        return f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@localhost:5432/{self.DATABASE_DB}"
