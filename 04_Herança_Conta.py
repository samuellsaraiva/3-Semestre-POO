/'''- Diagrama de classe com hierarquia                                 - Prof. Barbosa
-- Superclasse Conta atributos nome e saldo
- Método construtor
- Método get_saldo
- Método retorna_atributos
- Método __str__
- Crie uma instância (objeto) de Conta
- Use o método vars. Ex.: print(vars(objeto)) 
- Use os três métodos da classe
-- Subclasse Conta_PF
- Método construtor
- Método movimentacao:
- Crie uma instância (objeto) de Conta_PF
- Use os métodos da classe.
- Faça um depósito de 100 e consulte o saldo
- Faça uma retirada de 10 e consulte o saldo
-- Subclasse Conta_PJ
- Método construtor
- Método movimentacao
- Crie uma instância (objeto) de Conta_PJ
- Use os métodos da classe.
- Faça um depósito de 100 e consulte o saldo
- Faça uma retirada de 10 e consulte o saldo '''
class Conta(object):
    def __init__(self, nome):
        self._saldo = 0
        self._nome = nome
    def get_saldo(self):
        return self._saldo
    def retorna_atributos(self):
        s = self._nome + ' ' + str(self._saldo)
        return s
    def __str__(self):
        s = self._nome + ' ' + str(self._saldo)
        return s
class Conta_PF(Conta):
    def __init__(self, nome):
        super().__init__(nome)
    def movimentacao(self, valor):
        self._saldo += valor  - 5
class Conta_PJ(Conta):
    def __init__(self, nome):
        super().__init__(nome)
    def movimentacao(self, valor):
        self._saldo += valor - 10
if __name__ == '__main__':
    c1 = Conta('Paulo')
    print(c1.retorna_atributos())       # Chama o método retrona_atributos
    print(c1)                                   # Chama o método __str__()
    print(vars(c1))                           # Usa o método vars do Python
    pf1 = Conta_PF('Ana')
    print(pf1.retorna_atributos())
    print(pf1)
    print(vars(pf1))
    pf1.movimentacao(100)
    print(pf1.get_saldo())
    pf1.movimentacao(-10)
    print(pf1.get_saldo())

'''

class Conta_PJ(Conta):
    def __init__(self, nome):
        # Conta.__init__(self, nome)
        # Conta.__init__(nome)                 # Erro
        # super(Conta_PF, self).__init__(nome)
        # super(Conta_PF, self).__init__(self, nome)     # Erro
        super().__init__(nome)
    def movimentacao(self, valor):
        self._saldo += valor - 10


- Método movimentacao:
    def movimentacao(self,  valor):
        self._saldo += valor - 5


https://www.pythonprogressivo.net/2018/11/Como-Usar-Fazer-Heranca.html
'''
