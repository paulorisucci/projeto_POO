class Prancha:
    def __init__(self, marca, comprimento, cor, valor, fabricacao):
        self._marca = marca #(string)
        self._comprimento = comprimento #(float)
        self._cor = cor #(string)
        self._valor = valor #R$(float)
        self._fabricacao = fabricacao #Pais

    @property
    def marca(self):
        return self._marca
    @property
    def comprimento(self):
        return self._comprimento
    @property
    def cor(self):
        return self._cor
    @property
    def valor(self):
        return self._valor
    @property
    def fabricacao(self):
        return self._fabricacao
    
    @marca.setter
    def marca(self, novo):
        self._marca = novo
    @comprimento.setter
    def comprimento(self, novo):
        self._comprimento = novo
    @cor.setter
    def cor(self, novo):
        self._cor = novo
    @valor.setter
    def valor(self, novo):
        self._valor = novo
    @fabricacao.setter
    def fabricacao(self, novo):
        self._fabricacao = novo

    def __str__(self):
        return f'''Marca: {self._marca}
COMPRIMENTO: {float(self._comprimento)}
COR: {self._cor}
VALOR: R$ {float(self._valor)}
FABRICAÇÂO: {self._fabricacao.nome}
'''