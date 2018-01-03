
def enum(**enums):
    return type('Enum', (), enums)

eDataBase =  enum(GM_Tool=1, GM_Event=2,GM_Trace =3,GAME_EVENT=4,GAME_DB=5,GAME_TRACE=6)