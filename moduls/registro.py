from core import Checkfile,Readfile,NewFile

def REGISTRO(nombre,nickname):
    data=Readfile()
    play = data.get('jugadores',{})

    if nickname in play:
        print(f"el nombre de usuario que desea ya se encuentra ocupado : {nickname}")
        return None
    
    player ={
        'nombre': nombre,
        'nickname': nickname,
        'games' : 0,
        'games-win' : 0,
        'loses-games': 0,
        'games-machine' : 0,
        'games-win-machine' : 0,
        'loses-games-machine': 0,
        'games-player': 0,
        'games-win-player' : 0,
        'loses-games-player': 0,

    }
    data.setdefault('jugadores',{})[nickname] = player
    NewFile(data)
    print(f"jugador{nombre} con nickname {nickname} registrado de manera exitosa")
   



    