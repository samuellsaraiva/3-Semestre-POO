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
- Use todos os métodos da classe Gerente para o gerente g2.   
- Conceito de herança. A subclasse Gerente herda da superclasse Funcionario
- Altere o construtor da subclasse Gerente.
- Crie outra instância (g3) da classe Gerente com os dados necessários.
- Use o método retorna_atributos para o gerente (objeto g1) instanciado.
- No fim de ano, os funcionários do banco recebem uma bonificação. Os funcionários 
comuns recebem 10% do valor do salário e os gerentes, 15%. Então: 
Crie o método bonificação, ele não recebe nada e retorna o valor da bonificação.
- Mostre a bonificacao das instâncias f1 e g1.
- A bonificação do objeto g1 está errada. Por quê?
- Crie o método bonificação para a classe Gerernte também, ele não recebe nada e 
retorna o valor da bonificação.
- Altere o nétodo bonificacao de um Gerente usando o método super(), chame o método bonificacao 
de Funcionario e acrescente o resto do cálculo
- Utilize o método vars() para acessar os atributos de Funcionario e Gerente. Ex.: print(vars(objeto))
- Crie o método salario_total, ele não recebe nada e retorna o salário total do funcionário, ou seja o 
valor do salário mais o valor da boninficação.
- Use o método salario_total para o objeto f1 e o objeto g1."""
class Funcionario(object):                        # Nome de classe começa com letra maiúscula.
    def __init__(self, nome, cpf, salario):    # Método dunders
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    def retorna_atributos(self):
        s = self._nome + " " + str(self._cpf) + " " +str(self._salario)
        return s
def bonificacao(self):                            # Classe Funcionario
    return self._salario * 0.10
class Gerente(Funcionario):                  # Nome de classe começa com letra maiúscula.
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios
    def bonificacao(self):                        # Classe Gerente
        #return self._salario * 0.15                                         # Solução 1
        return super().bonificacao() + self._salario * 0.05       # Solução 2
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
    g1.retorna_atributos()
    g1.autentica('s1')
    bonificacao_f1 = f1.bonificacao()
    print("Bonificação de f1", bonificacao_f1)
    bonificacao_g1 = g1.bonificacao()
    print("Bonificação de g1", bonificacao_g1)
    print(vars(f1))
    print(vars(g1))
'''
class Gerente(object):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados
---

reescrever (sobrescrever, override)

# https://www.caelum.com.br/apostila-python-orientacao-objetos/heranca-e-classes-abstratas/#repetindo-cdigo
'''