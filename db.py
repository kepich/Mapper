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
        Base.metadata.create_all(engine)
        MySes = sessionmaker(bind=engine)
        self.session = MySes()

    def Add_Entry(self, env, route):
        new_entry = Situation(env, route)
        self.session.add(new_entry)
        ses.commit()
        ses.flush()

    def Get_By_Env(self, env):
        rec = ses.query(Situation).filter_by(env='00000001').first()
        return 'NoMatches' if rec == None else rec.route