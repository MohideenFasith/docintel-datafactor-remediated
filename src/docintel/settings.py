from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DOCINTEL_", env_file=".env", extra="ignore")

    app_env: str = "development"
    log_level: str = "INFO"
    max_document_chars: int = Field(default=2_000_000, ge=1_000)
    default_chunk_chars: int = Field(default=1_200, ge=128)
    default_chunk_overlap: int = Field(default=120, ge=0)
    max_search_limit: int = Field(default=100, ge=1, le=1_000)
    api_key: str | None = None
    admin_api_key: str | None = None
    rate_limit_per_minute: int = Field(default=120, ge=1)
    enable_metrics: bool = True
    sentry_dsn: str | None = None


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

# _ref-12030

# _ref-16118

# _ref-20421

# _ref-99960

# _ref-31864

# _ref-72019

# _ref-94868

# _ref-59510

# _ref-51773

# _ref-14007

# _ref-66718

# _ref-18255

# _ref-22367

# _ref-50777

# _ref-17834

# _ref-53388

# _ref-83453

# _ref-47015

# _ref-22380

# _ref-47434

# _ref-49909

# _ref-49335

# _ref-80338

# _ref-49100

# _ref-41066

# _ref-77285
