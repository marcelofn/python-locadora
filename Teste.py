from Filme import Filme
from Serie import Serie


class Teste(Serie, Filme):

    vingadores = Filme('vingadores', 2018, 150)
    atlanta = Serie('atlanta', 2019, 2)
    vingadores.dar_likes()
    vingadores.dar_likes()
    atlanta.dar_likes()
    atlanta.dar_likes()
    atlanta.dar_likes()

    lista_programas = [vingadores, atlanta]

    for programas in lista_programas:
        print(programas)




