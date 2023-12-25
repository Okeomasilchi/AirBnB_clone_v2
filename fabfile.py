from sqlalchemy import create_engine, MetaData
from models import *  # Import your models

# Define your database connection URL
database_url = 'mysql+mysqldb://root:Okeomasilachi1998##@localhost:3303/hbnb_dev_db'

# Create the SQLAlchemy engine
engine = create_engine(database_url, pool_pre_ping=True)

# Create a MetaData instance
metadata = MetaData()

# Bind the engine to the metadata
metadata.bind = engine

# Create all tables
metadata.create_all(bind=engine)
