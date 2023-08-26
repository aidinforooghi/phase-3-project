from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///enrollment.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    __tablename__ = 'students'
        id = Column(Integer, primary_key=True)
    name = Column(String)
    enrollments = relationship("Enrollment", back_populates="student")


class Course(Base):
    __tablename__ = 'courses'