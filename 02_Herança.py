"""  - Crie a classe Funcionario com os atributos nome, cpf, salario
- Crie o construtor da classe Funcionario (def __init___ (self, ...):
- Crie uma instância (f1) da classe com os dados necessários (f1 = Funcionario ( ... ) ) 
- Mostre todos os dados (atributos) do objeto f1
- Crie o método retorna_atributos. Ele não recebi nada e retorna todos os dados
do funcionário criado.                                                                                    
- Antes do método main, crie a classe Gerente com os atributos nome, cpf,  
salario, senha, qt_funcionários
- Crie uma instância (g1) da classe Gerente com os dados necessários
- Mostre todos os dados (atributos) do objeto g1       
- Crie o método autentica dentro da classe Gerente. Ele recebe a senha e 
imprime: Acesso permitido ou negado e retorna True ou False. 
- Use o método autentica para o gerente (objeto g1) instanciado.
- Use o método autentica para o funcionario (objeto f1) instanciado.       
- Use o método retorna_atributos para o gerente (objeto g1) instanciado.
- Crie outra instância (g2) da classe Gerente com os dados necessários.
- Use todos os métodos da classe Gerente para o gerente g2.   """
class Funcionario(object):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    def retorna_atributos(self):
        s = self._nome + " " + str(self._cpf) + " " +str(self._salario)
        return s
class Gerente(object):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados
    def autentica(self, senha):
        if self._senha == senha:
            print("Acesso permitido")
            return True
        else:
           print("Acesso negado")
           return False
if __name__ == '__main__':
    f1 = Funcionario('Paulo', 123, 1000)
    print(f1._nome)
    print(f1._cpf)
    print(f1._salario)
    r = f1.retorna_atributos()
    print (r)
    g1 = Gerente('Paula', 234, 3000, 's1', 5)
    print(g1._nome)
    #g1.retorna_atributos()
    g1.autentica('s1')
