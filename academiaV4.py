
# Classe pai que representa uma pessoa.
# Cada objeto criado a partir desta classe terá seus próprios dados.


# A classe Pessoa representa o conceito de herança para as classes AlunoAcademia e Personal.
# Como os dois são pessoas, a classe Pessoa passa características e propriedades
# para as outras classes. Isso facilita a organização do código,
# deixando o código mais limpo e evitando repetições.


class Pessoa:

    # Bloco novo.
    # Criei o __init__ para receber os dados que são comuns entre as pessoas.
    # Nesse caso, o nome e a idade.
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # Bloco novo.
    # O property permite acessar o nome de forma controlada,
    # sem precisar acessar diretamente o atributo privado.
    @property
    def nome(self):
        return self.__nome

    # Bloco novo.
    # O setter permite modificar o nome de forma controlada.
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    # Bloco novo.
    # Criei esse método para mostrar os dados que são comuns a qualquer pessoa.
    def exibir_dados_pessoa(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade} anos")


# Classe AlunoAcademia agora herda de Pessoa.
# Cada objeto criado a partir desta classe será um aluno com seus próprios dados.


# Isso significa basicamente que o Aluno vai herdar características da classe Pessoa.
# É uma forma de deixar claro que um aluno é uma pessoa,
# facilitando a organização e evitando repetir código.

class AlunoAcademia(Pessoa):

    # Bloco novo.
    # O __init__ recebe os dados necessários para criar um aluno.
    def __init__(self, nome, idade, peso, altura):

        # Eu uso super() para acessar o método da classe pai.
        # Nesse caso, estou chamando o __init__ de Pessoa para que ela
        # inicialize o nome e a idade, enquanto AlunoAcademia
        # inicializa os atributos específicos de um aluno.
        super().__init__(nome, idade)

        self.__peso = peso
        self.__altura = altura
        self.__matriculado = False

# Marca o aluno como matriculado na academia.

    def matricular(self):
        self.__matriculado = True

# Permite atualizar o peso armazenado do aluno quando for necessário.

    def atualizar_peso(self, novo_peso):
        self.__peso = novo_peso

# Faz o cálculo de IMC do aluno.
# Com um método privado usado apenas internamente pela classe.

    def __calcular_imc(self):
        return self.__peso / (self.__altura ** 2)

# Método estático que calcula a quantidade de água que a pessoa precisa pelo peso.
# Não depende diretamente de um objeto da classe.

    @staticmethod
    def calcular_consumo_agua(peso):
        return peso * 0.035

# Esse método centraliza a exibição das informações dos alunos.

    def exibir_dados(self):

        print("\n===== DADOS DO ALUNO =====")

        self.exibir_dados_pessoa()

        print(f"Peso: {self.__peso:.1f} kg")
        print(f"Altura: {self.__altura:.2f} m")
        print(f"Matriculado: {self.__matriculado}")
        print(f"IMC: {self.__calcular_imc():.2f}")

        print(
            f"Meta de água: "
            f"{AlunoAcademia.calcular_consumo_agua(self.__peso):.2f} litros"
        )


# Bloco novo.
# A classe Personal representa o profissional de Educação Física que trabalha na academia.
# A altura representa a altura do profissional.
# O CREF representa o número de registro profissional.
# A experiência representa o tempo de experiência profissional.
# O valor_hora representa o valor que a academia paga por hora trabalhada.

class Personal(Pessoa):

    # O __init__ recebe os valores dos atributos e inicializa o objeto Personal.
    def __init__(self, nome, idade, altura, cref, experiencia, valor_hora):

        # Uso super() novamente para utilizar o __init__ da classe Pessoa
        # e inicializar o nome e a idade.
        super().__init__(nome, idade)

        # Esses atributos são específicos do Personal
        # e ficam armazenados como atributos privados.
        self.__altura = altura
        self.__cref = cref
        self.__experiencia = experiencia
        self.__valor_hora = valor_hora

    # Criei esse método para mostrar os dados específicos do Personal.
    def exibir_dados(self):

        print("\n===== DADOS DO PERSONAL =====")

        # Reaproveito o método da classe Pessoa para mostrar nome e idade.
        self.exibir_dados_pessoa()

        print(f"Altura: {self.__altura:.2f} m")
        print(f"CREF: {self.__cref}")
        print(f"Experiência: {self.__experiencia} anos")
        print(f"Valor da hora: R$ {self.__valor_hora:.2f}")


# A classe Academia funciona como um gerenciador de alunos.
# Ela armazena os objetos da classe AlunoAcademia
# em uma lista privada e possui métodos para adicionar, listar e contar alunos cadastrados.

class Academia:

    def __init__(self):
        self.__alunos = []

        # Criei uma lista privada para armazenar os objetos dos Personais
        # cadastrados na academia, assim como já existe uma lista para armazenar os alunos.
        self.__personais = []

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    # Recebe um objeto Personal e coloca ele na lista privada __personais.
    def adicionar_personal(self, personal):
        self.__personais.append(personal)

    def listar_alunos(self):

        if len(self.__alunos) == 0:
            print("\nNenhum aluno cadastrado.")
            return

        for aluno in self.__alunos:
            aluno.exibir_dados()

    # O len() verifica o tamanho da lista.
    # O if verifica se não existe nenhum Personal.
    # O for percorre cada Personal cadastrado e chama o método exibir_dados().
    def listar_personais(self):

        if len(self.__personais) == 0:
            print("\nNenhum personal cadastrado.")
            return

        for personal in self.__personais:
            personal.exibir_dados()

    def quantidade_alunos(self):
        return len(self.__alunos)

    # Conta quantos elementos existem na lista de Personais.
    def quantidade_personais(self):
        return len(self.__personais)


# Criei funções de validação para garantir que os dados fornecidos pelo usuário sejam válidos antes de
# criar um objeto da classe AlunoAcademia, isso evita erros de cadastro e melhora a confiabilidade do
# sistema.

def ler_nome():

    while True:

        nome = input("Nome: ").strip()

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


# Criei uma função separada porque decidi que o Personal precisa ter pelo menos 18 anos,
# enquanto o aluno pode ter 10 anos.

def ler_idade_personal():

    while True:

        try:

            idade = int(input("Idade: "))

            if 18 <= idade <= 120:
                return idade

            print("Digite uma idade entre 18 e 120 anos.")

        except ValueError:

            print("Digite apenas números.")


# Essa função valida a altura do Personal.
# Assim como no aluno, ela aceita a altura em metros ou centímetros.
# Valores fora de 1,00 m até 2,50 m são rejeitados.

def ler_altura_personal():

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


# Criei uma validação para o CREF.
# Para simplificar o sistema, decidi aceitar somente 6 números.
# O len() verifica se existem exatamente 6 caracteres.
# O isdigit() verifica se todos os caracteres são números.

def ler_cref():

    while True:

        cref = input("CREF (6 dígitos): ").strip()

        if len(cref) == 6 and cref.isdigit():
            return cref

        print("CREF inválido. Digite exatamente 6 números.")


# Essa validação impede experiência negativa e limita a experiência
# de acordo com a idade do Personal, considerando o início profissional aos 18 anos.

def ler_experiencia(idade):

    while True:

        try:

            experiencia = int(input("Tempo de experiência (anos): "))

            if 0 <= experiencia <= idade - 18:
                return experiencia

            print(
                f"Digite uma experiência entre 0 e {idade - 18} anos."
            )

        except ValueError:

            print("Digite apenas números inteiros.")


# Essa função valida o valor da hora trabalhada.
# Decidi aceitar valores entre R$ 10,00 e R$ 10.000,00.

def ler_valor_hora():

    while True:

        try:

            valor = float(input("Valor da hora trabalhada (R$): "))

            if 10 <= valor <= 10000:
                return valor

            print("Digite um valor entre R$ 10,00 e R$ 10.000,00.")

        except ValueError:

            print("Digite um valor válido.")


# Essa é a parte principal do sistema, ela cria a academia, exibe um menu interativo e permite ao usuário
# cadastrar alunos, listar os alunos cadastrados, consultar a quantidade de alunos e encerrar o programa.
# Quando um aluno novo é cadastrado, o sistema cria um objeto da classe AlunoAcademia e o armazena na
# lista da classe Academia.

academia = Academia()

while True:

    print("\n===== SISTEMA DA ACADEMIA =====")
    print("1 - Cadastrar aluno")

    # Opção para cadastrar um Personal.
    print("2 - Cadastrar personal")

    print("3 - Listar alunos")

    # Opção para listar os Personais cadastrados.
    print("4 - Listar personais")

    print("5 - Quantidade de alunos")

    # Opção que mostra a quantidade de Personais cadastrados.
    print("6 - Quantidade de personais")

    print("7 - Sair")

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

    # Cadastro do Personal.
    elif opcao == "2":

        print("\n===== CADASTRO DE PERSONAL =====")

        nome = ler_nome()
        idade = ler_idade_personal()
        altura = ler_altura_personal()
        cref = ler_cref()
        experiencia = ler_experiencia(idade)
        valor_hora = ler_valor_hora()

        # Crio um objeto da classe Personal usando os dados validados.
        personal = Personal(
            nome,
            idade,
            altura,
            cref,
            experiencia,
            valor_hora
        )

        # Adiciono o objeto Personal à lista da Academia.
        academia.adicionar_personal(personal)

        print("\nPersonal cadastrado com sucesso!")

    elif opcao == "3":

        academia.listar_alunos()

    # Lista os Personais cadastrados.
    elif opcao == "4":

        academia.listar_personais()

    elif opcao == "5":

        print(
            f"\nQuantidade de alunos cadastrados: "
            f"{academia.quantidade_alunos()}"
        )

    # Mostra a quantidade de Personais cadastrados.
    elif opcao == "6":

        print(
            f"\nQuantidade de personais cadastrados: "
            f"{academia.quantidade_personais()}"
        )

    elif opcao == "7":

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida.")