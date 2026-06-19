#Classe que representa um aluno da academia.
#Cada objeto criado a partir desta classe será um aluno com seus próprios dados.

class AlunoAcademia:

#Método construtor.
#é executado automaticamente quando um aluno é criado.
#recebe os dados dos alunos e os armazena em atributos privados de classe:
#def __init__, (self, nome, idade, peso e altura) __init__é a iniciação da classe. 

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__matriculado = False

#property é um getter, serve pra que a leitura do atributo privado nome seja feita sem acessar aluno.nome
#permite modificar o nome do aluno sem acessar diretamente o atributo privado.

    @property
    def nome(self):
        return self.__nome
    
#setter do atributo nome, permite alterar o nome do aluno de forma controlada, setter = definidor. 

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

#Marca o aluno como matriculado na acadêmia.

    def matricular(self):
        self.__matriculado = True

#permite atualizar o peso armazenado do aluno quando for necesssário.

    def atualizar_peso(self, novo_peso):
        self.__peso = novo_peso

#Faz o calculo de imc do aluno.
#com um método privado usado apenas internamente pela classe.

    def __calcular_imc(self):
        return self.__peso / (self.__altura ** 2)
    
#Método estático que calcula a quantidade de água que a pessoa precisa pelo peso.
#Não depende diretamente de um objeto da classe.

    @staticmethod
    def calcular_consumo_agua(peso):
        return peso * 0.035
    
#Esse método centraliza a exibição das informações dos alunos, além dos dados cadastrados, também 
#ultiliza o método privado de cálculo de imc e o método estático de consumo de água para mostrar 
#as informações ao usuário.

    def exibir_dados(self):

        print("\n===== DADOS DO ALUNO =====")

        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade} anos")
        print(f"Peso: {self.__peso:.1f} kg")
        print(f"Altura: {self.__altura:.2f} m")
        print(f"Matriculado: {self.__matriculado}")
        print(f"IMC: {self.__calcular_imc():.2f}")

        print(
            f"Meta de água: "
            f"{AlunoAcademia.calcular_consumo_agua(self.__peso):.2f} litros"
        )

#A classe academia funciona como um gerenciador de alunos. Ela armazena os objetos da classe AlunoAcademia
#em uma lista privada e possui métodos para adicionar, listar e contar alunos cadastrados
#funcionando de forma semelhante a um banco de dados.
class Academia:

    def __init__(self):
        self.__alunos = []

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def listar_alunos(self):

        if len(self.__alunos) == 0:
            print("\nNenhum aluno cadastrado.")
            return

        for aluno in self.__alunos:
            aluno.exibir_dados()

    def quantidade_alunos(self):
        return len(self.__alunos)

#Criei funções de validação para garantir que os dados fornecidos pelo usuário sejam válidos antes de 
#criar um objeto da classe AlunoAcademia, isso evita erros de cadastro e melhora a confiabilidade do 
#sistema.

def ler_nome():

    while True:

#O método strip funciona como uma borracha que apaga todos os espaços invisíveis ou caractéres
#indesejados. 

        nome = input("Nome: ").strip()

#Funciona como um formatador de nomes próprios, que automáticamente transforma a primeira letra
#de cada palavra em maiúscula e deixa o restante em minúsculo.

        if nome != "":
            return nome.title()

        print("Nome inválido.")


def ler_idade():

    while True:

        try:

            idade = int(input("Idade: "))

            if 10 <= idade <= 120:
                return idade

            print("Digite uma idade entre 10 e 120 anos.")

#execpt ValueError é um escudo de segurança no código que entra em ação para salvar o programa 
#caso o usuário digite um dado totalmente errado do que era esperado.

        except ValueError:

            print("Digite apenas números.")


def ler_peso():

    while True:

        try:

            peso = float(input("Peso (kg): "))

            if 20 <= peso <= 300:
                return peso

            print("Digite um peso entre 20 e 300 kg.")

        except ValueError:

            print("Digite apenas números.")


def ler_altura():

    while True:

        try:

            altura = float(input("Altura (m ou cm): "))

            if altura > 3:
                altura = altura / 100

            if 1 <= altura <= 2.5:
                return altura

            print("Digite uma altura entre 1,00 m e 2,50 m.")

        except ValueError:

            print("Digite apenas números.")

#Essa é a parte principal do sistema, ela cria a academia, exibe um menu interativo e permite ao usuário
#cadastrar alunos, listar os alunos cadastrados, consultar a quantidade de alunos e encerrar o programa.
#Quando um aluno novo é cadastrado, o sistema cria um objeto da classe AlunoAcademia e o armazena na 
#lista da classe Academia.
academia = Academia()

while True:

    print("\n===== SISTEMA DA ACADEMIA =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Quantidade de alunos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n===== CADASTRO DE ALUNO =====")

        nome = ler_nome()
        idade = ler_idade()
        peso = ler_peso()
        altura = ler_altura()

        aluno = AlunoAcademia(
            nome,
            idade,
            peso,
            altura
        )

        aluno.matricular()

        academia.adicionar_aluno(aluno)

        print("\nAluno cadastrado com sucesso!")

    elif opcao == "2":

        academia.listar_alunos()

    elif opcao == "3":

        print(
            f"\nQuantidade de alunos cadastrados: "
            f"{academia.quantidade_alunos()}"
        )

    elif opcao == "4":

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida.")