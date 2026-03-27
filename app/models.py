from sqlalchemy import Column, Integer, Text
from app.database import Base

class Contract(Base):
    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    analysis = Column(Text)
    