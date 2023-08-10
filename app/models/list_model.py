import __init__

from sqlalchemy import Boolean, Column, Integer, String, JSON
from config.init_db import Base

class ListModel(Base):
    __tablename__ = "lists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    items = Column(JSON, index=True)
    is_active = Column(Boolean, default=True)