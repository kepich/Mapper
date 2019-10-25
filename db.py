from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker

class DB():
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

    def __init__(self):
        engine = create_engine('sqlite:///:memory:', echo=True)
        self.Base.metadata.create_all(engine)
        MySes = sessionmaker(bind=engine)
        self.session = MySes()

        first_sit = self.Situation('00000001', 'L100B10T10B100500')
        self.session.add(first_sit)
        self.session.commit()

    def Add_Entry(self, env, route):
        new_entry = self.Situation(env, route)
        self.session.add(new_entry)
        self.session.commit()

    def Get_By_Env(self, envo):
        rec = self.session.query(self.Situation).filter_by(env=envo).first()
        return 'NoMatches' if rec == None else rec.route