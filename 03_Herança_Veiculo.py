''' - Crie a superclasse Veiculo com os atributos valor, modelo (celta, palio, honda etc)
e km que indica a quilometragem do veículo.
- Crie o construtor da classe Veiculo (def __init___ (self, ...):
- No main, crie uma instância (v1) da classe com os dados necessários (v1 = Veiculo ( ... ) )
- Mostre todos os dados (atributos) do objeto v1
- Antes do método main, crie a subclasse Carro, que vai herdar a classe Veiculo.
Ela recebe os atributos tipo, modelo, km e portas.
- Crie uma instância (c1) da classe Carro com os dados necessários
- Mostre todos os dados (atributos) do objeto c1
- Sobreescreva o método exibe_atributos de Veiculo para mostrar também as portas.
- Antes do método main, crie a subclasse Moto, que herda a superclasse Veiculo e deve
ter um atributo novo, cilindradas.
- Crie a instância m1 da classe Moto com os dados necessários.
- Mostre todos os dados (atributos) do objeto m1
- Sobreescreva o método exibe_atributos de Veiculo para mostrar também as cilindradas.
- Utilize o método vars() para acessar os atributos de Veiculo, Carro e Moto. Ex.: print(vars(objeto))
- Crie o atributo de classe qtd_veiculo para armazenar a quantidade de veiculos instanciados
- Crie o método atualiza_valor, ele recebe um valor em reais e não retorna nada. O objetivo do
método é acrescentar o valor recebido ao valor original de qualquer veículo. 
Faça uma crítica dentro do método.
- Crie o método que permita consultar o valor do veiculo. Ele não recebe nada e retorna
o valor atual do veiculo.
- Crie o método atualiza_valor_pct, ele recebe uma porcentagem (ex.: 5, 10, 20 etc) e não retorna nada. 
O objetivo do método é atualizar o valor de qualquer veículo. Faça uma crítica dentro do método.
- Verifique se o item anterior foi bem-sucedido.
- Crie um método para verificar se o veículo é um veículo zero, veículo seminovo ou veículo usado.
O veiculo zero tem km igual a zero, seminovo se tiver até 20000 Km e veículo usado se tiver
mais que 20000 Km.
- Use o método anterior com os objetos criados.
'''
class Veiculo(object):                        # Nome de classe começa com letra maiúscula.
    qtd_veiculo = 0                                    # Atributo de classe
    def __init__(self, valor, modelo, km):    # Método dunders
        self._valor = valor                            # Atributos de instância
        self._modelo= modelo
        self._km = km
        Veiculo.qtd_veiculo += 1          # Atributo de classe, não tem self.
    def exibe_atributos(self):
        s = "Valor: " + str(self._valor)+ ", Modelo: "+ self._modelo + ", Km: " + str(self._km)
        print(s)
    def get_valor(self):
        return self._valor
    def atualiza_valor(self, valor):
        if valor > 0:
            self._valor += valor
    @staticmethod
    def get_qtd_veiculo ():             # Método estático, método de classe, não tem self.
        return Veiculo.qtd_veiculo
class Carro (Veiculo):
    def __init__(self, valor, modelo, km, portas):
        super().__init__(valor, modelo, km)
        # Veiculo.__init__(valor, modelo, km)                  # Erro
        # Veiculo.__init__(self, valor, modelo, km)
        self._portas = portas
    def exibe_atributos(self):
        super().exibe_atributos()
        print("Portas: " + str(self._portas))
class Moto(Veiculo):
    def __init__(self, valor, modelo, km, cilindradas):
        super().__init__(valor, modelo, km)
        self._cilindradas = cilindradas
    def exibe_atributos(self):
        super().exibe_atributos()
        print("Cilindradas: " + str(self._cilindradas))
if __name__ == '__main__':
    v1 = Veiculo (40000, "Celta", 1000)
    v1.exibe_atributos()
    c1 = Carro (80000, "Honda", 100, 4)
    c1.exibe_atributos()
    m1 = Moto (22000, "CBS", 12000, 400)
    m1.exibe_atributos()
    v = v1.get_qtd_veiculo()
    print('Quantidade: ', v)
    v = c1.get_qtd_veiculo()
    print('Quantidade: ', v)
    v = m1.get_qtd_veiculo()
    print('Quantidade: ', v)
    v = Veiculo.get_qtd_veiculo()
    print('Quantidade: ', v)
    # . . .



'''

https://www.pythonprogressivo.net/2018/11/Como-Usar-Fazer-Heranca.html
'''
