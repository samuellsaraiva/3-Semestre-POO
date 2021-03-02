''' Atalho de taclado: ctlr + <d>, duplica linha ou bloco.  ctrl + </>, comenta linha ou bloco.
- Acrescente o atributo número do CPF na subclasse Conta_PF                   - Prof. Barbosa
- Acrescente o atributo  número CNPJ na subclasse Conta_PJ
- Atualizar o construtor das duas subclasses
- Atualize o objeto da Conta_PF, no método main
- Crie  o objeto da Conta_PJ, no método main
- Rode (teste) o programa e com os objetos criados das subclasses Conta_PF e Conta_PJ
- A política do sistema bancário mudou:
- Depósito não cobra taxa, somente saque. Então, substitua os dois métodos movimentação
por um método deposito e dois métodos saque (pessoa fixa tem taxa de 5 reais e pessoa jurídica de 10).
    DICAS: Não apaque os métodos movimentação, apenas comente.
   DICAS: Crie um método deposito na superclasse e dois métodos saque, um em cada subclasse
- Teste a alteração anterior.
- Agora, substitua os dois métodos saque das subclasses por apenas um método saque na superclasse.
  Use o método do Python isinstance(objeto, Classe) na superclasse. Ele retorna True ou false.        
- Teste a alteração anterior.
- Crie um atributo de classe para armazenar a quantidade de contas (objetos) criados.        
- Onde colocar o contador (a atualização)? 
- Crie o método estático get_qtd_contas.
- Teste as alterações anteriores e o método estático get_qtd_contas.
- Crie o atributo de classe para armazenar o valor total que o banco tem armazenado.
- Crie os método estático get_total para retornar o valor total armazenado no banco.
- Crie o método estático atualiza_total para atualizar o valor total armazenado no banco
que muda em cada movimentação que os clientes realizarem.                                         '''
class Conta(object):
    qtd_conta = 0                     # Atributo de classe (comum para todos os objetos)
    def __init__(self, nome):
        self._saldo = 0                 # Atributos de instância (objeto)
        self._nome = nome
        Conta.qtd_conta += 1
    def get_saldo(self):
        return self._saldo
    def retorna_atributos(self):
        s = self._nome + ' ' + str(self._saldo)
        return s
    @staticmethod                          # decorators
    def get_qtd_conta():
        return Conta.qtd_conta
    def __str__(self):
        s = self._nome + ' ' + str(self._saldo)
        return s
    def deposito(self, valor):
        self._saldo += valor
    def saque(self, valor):                                # pf1.saque(100)   No main
        if (isinstance(self, Conta_PF)):   # Resultado True ou False
            print("Conta_PF")
            self._saldo -= valor
            self._saldo -= 5
        elif (isinstance(self, Conta_PJ)):             # pj1.saque(100)   No main
            print("Conta_PJ")
            self._saldo -= valor
            self._saldo -= 10
class Conta_PF(Conta):                   # Subclasse Conta_PF, herda da superclasse Conta
    def __init__(self, nome, cpf):
        self._cpf = cpf
        super().__init__(nome)
    # def movimentacao(self, valor):
    #     self._saldo += valor  - 5
    # def saque(self, valor):
    #     self._saldo -= valor
    #     self._saldo -= 5
class Conta_PJ(Conta):
    def __init__(self, nome, cnpj):
        self._cnpj = cnpj
        # Conta.__init__(self, nome)
        # Conta.__init__(nome)                 # Erro
        # super(Conta_PF, self).__init__(nome)
        # super(Conta_PF, self).__init__(self, nome)     # Erro
        super().__init__(nome)
    # def movimentacao(self, valor):
    #     self._saldo += valor - 10
    # def saque(self, valor):
    #     self._saldo -= valor
    #     self._saldo -= 10
if __name__ == '__main__':
    c1 = Conta('Paulo')
    print(c1.retorna_atributos())       # Chama o método retrona_atributos
    print(c1)                                   # Chama o método __str__()
    print(vars(c1))                           # Usa o método vars do Python
    pf1 = Conta_PF('Ana', "1")
    print(pf1.retorna_atributos())
    print(pf1)
    print(vars(pf1))
    pf1.deposito(100)
    print(pf1.get_saldo())
    pf1.saque(10)
    # pf1.saque(10, pf1)
    print(pf1.get_saldo())
    pj1 = Conta_PJ('Locadora', "2")
    print(pf1.retorna_atributos())
    print(pj1)
    print(vars(pj1))
    pj1.deposito(200)
    print(pj1.get_saldo())
    pj1.saque(10)
    # pj1.saque(10, pj1)
    print(pj1.get_saldo())

'''
- Crie um atributo de classe para armazenar a quantidade de contas (objetos) criados.
class Conta(object):
    qtd_conta = 0
    def __init__(self, nome):
        self._saldo = 0
        self._nome = nome
        Conta.qtd_veiculo += 1
    ...
- Crie o método estático get_qtd_contas.
@staticmethod
def get_qtd_conta():
    return Conta.qtd_conta

--

https://www.pythonprogressivo.net/2018/11/Como-Usar-Fazer-Heranca.html

'''
