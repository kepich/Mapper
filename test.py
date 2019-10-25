from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker

Base = declarative_base()

class Situation(Base):
    __tablename__ = 'Situations'
    id = Column(Integer, primary_key=True)
    env = Column(String)
    route = Column(String)

    def __init__(self, env, route):
        self.env = env
        self.route = route

    def __repr__(self):
        return "<Situation('%s', '%s')>" % (self.env, self.route)

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

MeSession = sessionmaker(bind=engine)
ses = MeSession()

first_sit = Situation('00000001', 'L100B10T10B100500')
ses.add(first_sit)
ses.commit()
ses.flush()

recieve = ses.query(Situation).filter_by(env='00000011').first()
print(recieve.route) if recieve != None else print('NoMatches')