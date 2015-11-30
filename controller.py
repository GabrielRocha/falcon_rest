import json
import falcon
from sqlalchemy.orm import sessionmaker
from models import Amigo, Base, engine
from helper import orm_to_json, get_three_closer_friends

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Amigos(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        if req.get_param("id"):
            result = {'amigo': orm_to_json(session.query(Amigo).get(req.get_param("id")))}
        else:
            amigos = [orm_to_json(amigo) for amigo in session.query(Amigo).all()]
            result = {'amigos': amigos}
        resp.body = json.dumps(result)

    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            for amigo in result['amigos']:
                amigo = Amigo(nome=amigo['nome'],
                              latitude=amigo['latitude'],
                              longitude=amigo['longitude'])
                session.add(amigo)
                session.commit()
            resp.body = 'Amigo(s) adicionado(s)'
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, ex.message)


class Proximidade(object):

    def on_get(self, req, resp):
        if req.get_param("id"):
            voce = session.query(Amigo).get(req.get_param("id"))
            amigos = session.query(Amigo).filter(Amigo.id != voce.id)
            amigos = [orm_to_json(session.query(Amigo).get(id))
                      for id, hipotenusa in get_three_closer_friends(voce, amigos)]
            resp.body = json.dumps({'amigos': amigos})
        else:
            resp.body = "Informe o id do amigo a ser analisado"
