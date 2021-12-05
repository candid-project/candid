from sqlalchemy import Column, Integer, String  # ForeignKey

from .database import Base

# from sqlalchemy.orm import relationship


class PoliticalBody(Base):
    __tablename__ = "political_bodies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    # politicians = relationship("Politician", back_populates="political_body")


class PoliticalParty(Base):
    __tablename__ = "political_parties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    # politicians = relationship("Politician", back_populates="political_party")


class Politician(Base):
    __tablename__ = "politicians"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state = Column(String)
    # political_body_id = Column(Integer, ForeignKey("political_bodies.id"))
    # political_party_id = Column(Integer, ForeignKey("political_parties.id"))

    # political_body = relationship("PoliticalBody", back_populates="politicians")
    # political_party = relationship("PoliticalParty", back_populates="politicians")
