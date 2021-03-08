from Prancha import Prancha

class Surfista:
    def __init__(self,nome, idade, pranchas = [], campeonatos = [],total_ganho = 0):
        self._nome = nome #String
        self._idade = idade #int
        self._campeonatos = campeonatos #litaCampeonatos
        self._pranchas = pranchas #listaPranchas
        self._total_ganho = total_ganho #float

    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    @property
    def lst_campeonato(self):
        return self._campeonatos
    @property
    def total_ganho(self):
      return self._total_ganho
    @property
    def pranchas(self):
        return self._pranchas

    @nome.setter
    def nome(self, novo):
        self._nome = novo
    @idade.setter
    def idade(self, novo):
        self._idade = novo
    @lst_campeonato.setter
    def lst_campeonato(self, campeonatos):
        self._campeonatos = campeonatos
    @total_ganho.setter
    def total_ganho(self, novo_total):
        return self._total_ganho
    @pranchas.setter
    def pranchas(self, novas_pranchas):
      self._pranchas = novas_pranchas

    def add_campeonato(self, c):
        if c not in self._campeonatos:
            self._campeonatos.append(c)

    def add_premio(self, premio):
      self._total_ganho += premio

    def pranchas_marca(self, marca):
        list_p = 'Nenhuma'
        for i in self._pranchas:
            if i.marca == marca:
                list_p = list_p.replace('Nenhuma', '')
                list_p += '--------------------------\n' 
                list_p += f'{i}'        
        return list_p

    def total_ganho(self):
        return self._total_ganho

    def str_campeonatos(self):
      nome = '\nCAMPEONATOS DISPUTADOS:\n'
      for i in self._campeonatos:
        if(i.campeao == self):
            nome += f'- {i.nome} *\n'
        else:
            nome += f'- {i.nome}\n'
      return nome

    def add_prancha(self,p):
        if p not in self._pranchas:
            self._pranchas.append(p)

    def __str__(self):
        prancha = ''
        for i in self._pranchas:
            prancha += f'# {i.marca} #'

        return f'''NOME: {self._nome}
IDADE: {self._idade} anos
PRANCHA(S): 
{prancha}'''


if __name__ == "__main__":
    #PRANCHAS
    pr1 = Prancha('Y', 2.1, 'Vermelho e branco', 432.5, 'Africa do Sul')
    pr2 = Prancha("Y", 2.34, "Azul e verde", 430.0, 'Portugal')
    pr3 = Prancha("Z", 2.0, "Verde", 400.0, 'Brasil')

    #SURFISTAS
    s1 = Surfista('Douglas', 33)
    s2 = Surfista('Amanda', 25)
    
    s1.add_prancha(pr1) 
    s2.add_prancha(pr2) #s1.add_campeonato('y')
    s2.add_prancha(pr3)

    print(s1)
    '''
    marca = input('Marca da prancha: ').upper()
    print(s2.pranchas_marca(marca))
    '''
    

