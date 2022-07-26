from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from .configuration import settings


engine = create_engine(url=settings.POSTGRES_URI)
default_session = sessionmaker(bind=engine)
