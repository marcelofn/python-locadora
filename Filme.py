from Programa import Programa


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "Nome: {} - Ano: {} - Duração: {} - Likes: {}"\
            .format(self._nome, self.ano, self.duracao, self._likes)
