from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://parser:parserPass-tsum_126@db:5432/parsing")
Base = declarative_base()


class DB(Base):
    __tablename__ = "keng_ru"

    date = Column("date", Date, nullable=False, primary_key=True)
    brand = Column("brand", String, nullable=False, primary_key=True)
    article = Column("article", String, nullable=False, primary_key=True)
    size = Column("size", String, nullable=False, primary_key=True)

    title = Column("title", String)
    category = Column("category", String)

    current_price = Column("current_price", Integer)
    first_price = Column("first_price", Integer)
    price_classic = Column("price_classic", Integer)
    price_celebrity = Column("price_celebrity", Integer)
    price_prestige = Column("price_prestige", Integer)
    price_platinum = Column("price_platinum", Integer)
    price_elite = Column("price_elite", Integer)
    price_brilliant = Column("price_brilliant", Integer)
    qty = Column("qty", Integer)
    url = Column("url", String, nullable=False, primary_key=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def insert(item) -> None:
    with Session() as session:
        session.add(item)
        session.commit()
