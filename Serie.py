from Programa import Programa


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "Nome: {} - Ano: {} - Temporadas: {} - Likes: {}"\
            .format(self._nome, self.ano, self.temporadas, self._likes)

