from pathlib import Path
from typing import Any

from pydantic import BaseSettings, validator, PostgresDsn


current_path = Path(__file__).parent.absolute()


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(cls, v: str | None = None, *, values: dict[str, Any] | None) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_HOST'),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    def get_db_uri(self, values_to_update: dict[str, Any] | None = None) -> str:
        """
        Returns a str with the database URI. Any of the URI components can be modified
        before returning it by passing the component name and its new value to values_to_update
        in a dict.
        Example: get_db_uri(values_to_update={'POSTGRES_HOST': '172.24.0.1'})
        """
        if values_to_update is None:
            values_to_update = {}

        return PostgresDsn.build(
            scheme='postgresql',
            user=values_to_update.get('POSTGRES_USER', self.POSTGRES_USER),
            password=values_to_update.get('POSTGRES_PASSWORD', self.POSTGRES_PASSWORD),
            host=values_to_update.get('POSTGRES_HOST', self.POSTGRES_HOST),
            path=f"/{values_to_update.get('POSTGRES_DB', self.POSTGRES_DB) or ''}"
        )

    class Config:
        env_file = f'{current_path}/dev.env'


settings = Settings()
