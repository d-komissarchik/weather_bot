from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(String(60), nullable=False)
    title = Column(String(30), nullable=False)
    author = Column(String(30), nullable=False)
    rewiews = relationship('Reviews', backref='book', lazy=True)

    def __repr__(self):
        return self.title
