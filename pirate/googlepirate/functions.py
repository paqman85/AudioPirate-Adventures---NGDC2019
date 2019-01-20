from random import randint
from .models import UserSessionData

def Sail():
    randomEvent1= randint(0,4)
    randomEvent2= randint(0,4)
    radomEvent3= randint(0,4)
    radomIlands= randint(0,24)

def Explore():
    randomEvent1= randint(0,9)
    randomEvent2= randint(0,9)
    radomEvent3= randint(0,9)
    radomMorality= randint(0,10)

def decision(answer):
    if answer==True:
        randomTrueOutcome=randint(0,10)
    else:
        randomFalseOutcome=randint(0,10)

def GameStatus():

    if UserSessionData.loottotal >= 1000 | UserSessionData.reknown >= 100:
        winstatus=True
    elif UserSessionData.loottotal <= 0 | UserSessionData.reknown <= 0:
        winstatus=False

