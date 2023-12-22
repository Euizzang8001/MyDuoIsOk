from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.sql.functions import current_timestamp
from config.database import Base

class Player(Base):
    __tablename__ = "players"
    
    player_id = Column( 
        String(255),
        primary_key=True,
        unique = True,
        comment='Player ID',
    )
    datetime = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
    )