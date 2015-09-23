from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=255)),
    Column('begin', DateTime),
    Column('end', DateTime),
    Column('user_id', Integer),
    Column('date_created', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.current_timestamp at 0x7f108c71c450; current_timestamp>)),
    Column('date_modified', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.current_timestamp at 0x7f108c71c790; current_timestamp>), default=ColumnDefault(<sqlalchemy.sql.functions.current_timestamp at 0x7f108c71c650; current_timestamp>)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].columns['date_created'].create()
    post_meta.tables['event'].columns['date_modified'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].columns['date_created'].drop()
    post_meta.tables['event'].columns['date_modified'].drop()
