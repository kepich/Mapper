from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker
from itertools import product
from os import remove
import random

class DB():
    Base = declarative_base()

    class Situation(Base):
        """
            Database
        """
        __tablename__ = 'Situations'
        id = Column(Integer, primary_key=True)
        env = Column(String)    #Environment
        route = Column(String)  # Route

        def __init__(self, env, route):
            self.env = env
            self.route = route

        def __repr__(self):
            return "<Situation('%s', '%s')>" % (self.env, self.route)

    def __init__(self, is_new_db):
        """
            is_new_db - True - create new database, False - use old database
        """
        if is_new_db:
            remove('myDb.db')
        engine = create_engine('sqlite:///myDb.db', echo=False)
        self.Base.metadata.create_all(engine)
        MySes = sessionmaker(bind=engine)
        self.session = MySes()
        if is_new_db:
            self.Generator()

    def Add_Entry(self, env, route):
        new_entry = self.Situation(env, route)
        self.session.add(new_entry)
        self.session.commit()

    def Get_By_Env(self, envo):
        rec = self.session.query(self.Situation).filter_by(env=envo).first()
        return ('N' + envo) if rec == None else ('F' + rec.route)

    # \/ \/ \/ This methods used to generate random envs and routs \/ \/ \/
    def Generate_Route(self):
        path = ''
        rotations = ['L', 'R', 'T', 'B']
        am_of_rot = random.randint(10, 30)
        last_rot = None
        temp_rot = None
        for j in range(am_of_rot):
            while temp_rot == last_rot:
                temp_rot = random.randint(0,3)
            last_rot = temp_rot
            path += rotations[temp_rot] + str(random.randint(1,100000))
        return path

    def Generate_Situation(self):
        objects = ['T', 'F', 'R', 'L', 'H', 'S', 'P', 'E']
        situation = ''
        while True:
            situation = ''
            for k in range(8):
                temp_el = random.randint(0,10)
                if temp_el > 6:
                    temp_el = 7
                situation += objects[temp_el]
            
            if (self.Get_By_Env(situation))[0] == 'N':
                break
        return situation

    def Generator(self):
        amount_of_sits = 400000

        def_sits = ['E', 'T', 'P']
        default_sits = list(map(lambda t: ''.join(t), list(product(def_sits, def_sits, repeat=4))))
        
        for i in default_sits:
            new_entry = self.Situation(i, self.Generate_Route())
            self.session.add(new_entry)
        self.session.commit()

        for i in range(amount_of_sits):
            if (i % (amount_of_sits / 100)) == 0:
                print(str(i * 100 // amount_of_sits) + '%')
                self.session.commit()
            new_entry = self.Situation(self.Generate_Situation(), self.Generate_Route())
            self.session.add(new_entry)
        self.session.commit()
