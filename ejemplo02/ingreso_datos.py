from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos
import codecs

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Importacion de datos, clubs
archivo = codecs.open("data/datos_clubs.txt", "r", encoding='utf-8')
lin = archivo.readlines()
# Tratamiento de datos, clubs
data1 = list(map(lambda x: x.split(";"), lin))
limpia = list(map(lambda x: x[len(x)-1].split("\r\n"), data1))
limpia = list(map(lambda x: x[0], limpia))
var = 0
for x in data1: 
        session.add(Club(nombre= x[0], deporte=x[1], fundacion=limpia[var]  ) )
        var+=1

# Se extrae el id y el nombre del club en una consulta
llaves = session.query(Club).all()

# Importacion de datos, jugadores
archivo = codecs.open("data/datos_jugadores.txt", "r", encoding='utf-8')
lin = archivo.readlines()
# Tratamiento de datos, jugadores
data2 = list(map(lambda x: x.split(";"), lin))
limpia = list(map(lambda x: x[len(x)-1].split("\r\n"), data2))
limpia = list(map(lambda x: x[0], limpia))
var = 0
for x in data2: 
        x[len(x)-1] = limpia[var]
        var = var+1

        # Se itera para comparar el nombre de la consulta y determinar el id del club al que pertenece el jugador
        for i in llaves:
                if x[0] == i.nombre:
                        session.add(Jugador(nombre=x[3], dorsal=x[2], posicion=x[1], club_id=i.id ) )

session.commit()