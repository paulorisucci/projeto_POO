class Praia:
    def __init__(self, nome, num_campeonatos, pais = None):
        self._nome = nome #String
        self._num_campeonatos = num_campeonatos #int
        self._pais = pais #Pais

    @property
    def nome(self):
        return self._nome
    @property
    def num_campeonatos(self):
        return self._num_campeonatos
    @property
    def pais(self):
        return self._pais

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    @num_campeonatos.setter
    def num_campeonatos(self, novo_num):
        self._num_campeonatos = novo_num
    @pais.setter
    def pais(self, novo_pais):
        self._pais = novo_pais

    def add_camp(self):
      self._num_campeonatos += 1