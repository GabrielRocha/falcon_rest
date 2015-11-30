import math


def orm_to_json(objects):
    return {key:objects.__dict__[key] for key in objects.__dict__ if not key.startswith('_')}


def get_three_closer_friends(voce, amigos):
    return sorted([(amigo.id, get_hypotenuse(voce, amigo)) for amigo in amigos], key=lambda valor:valor[1])[:3]


def get_hypotenuse(voce, amigo):
    return math.sqrt((int(voce.latitude) - int(amigo.latitude))**2 + (int(voce.longitude) - int(amigo.longitude))**2)