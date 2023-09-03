from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://admin:outside23@bifrost-dev.chwigxp9nbvl.us-east-1.rds.amazonaws.com:5432/PeopleCountingDB"

database = Database(DATABASE_URL)
metadata = MetaData()
