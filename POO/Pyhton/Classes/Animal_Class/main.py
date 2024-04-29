from cachorro import Cachorro
from gato import Gato

def fazer_barulho(animal):
    print(animal.get_som())

cachorro = Cachorro("Kleber vai ou voa", "Viralata Camarelo")
gato = Gato("Jhones trupica ou cai", "Azul")


print(cachorro.name, "", cachorro.race)
fazer_barulho(cachorro)
print(gato.name, "", gato.color)
fazer_barulho(gato)