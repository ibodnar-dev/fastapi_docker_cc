from sqlalchemy_utils import database_exists, create_database

from app.core.configuration import settings

"""
Get the gateway IP from the docker network for the host value
"""

host = ''
uri = settings.get_db_uri(values={'POSTGRES_HOST': host})

if not database_exists(uri):
    create_database(uri)
