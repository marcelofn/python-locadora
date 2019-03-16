from Filme import Filme
from Playlist import Playlist
from Serie import Serie


class Teste(Serie, Filme, Playlist):
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    tmep = Filme('todo mundo em panico', 1999, 100)
    demolidor = Serie('demolidor', 2016, 2)

    vingadores.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()
    atlanta.dar_likes()
    atlanta.dar_likes()
    tmep.dar_likes()
    tmep.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()

    listinha = [atlanta, vingadores, demolidor, tmep]
    minha_playlist = Playlist('fim de semana', listinha)

    for programa in minha_playlist.listagem:
        print(programa)

    print(f'Tamanho: {len(minha_playlist.listagem)}')
