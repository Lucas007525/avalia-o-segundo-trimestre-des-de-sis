#Criei um modelo de aluno, toda informação e comportamento do aluno
#ficarão dentro dessa classe.
class AlunoAcademia:

#Executa quando um aluno é criado, recebe os dados inicais.
#Os atributos começam com .__ tornando-os privados.
    class AlunoAcademia:
        def __init__(self, nome, idade, peso, altura):
            self.__nome = nome 
            self.__idade = idade
            self.__peso = peso 
            self.__altura = altura
            self.__matriculado = False 
#aqui permite o acesso a: print(aluno.nome) sem acesar: aluno.__nome
@property
def nome(self):
    return self.__nome

#permite a alteração dos nomes como por exemplo: aluno.nome = Lucas
@nome.setter
def nome(self, novo__nome):
    self.__nome =  novo__nome

#Marca o aluno como matriculado.
def matricular(self): 
    self.__matriculado = True 
    print(f"{self.__nome} foi matriculado.")

#Permite que uma matrícula seja cancelada.
def cancelar_matricula(self):
    self.__matriculado = False
    print(f"{self.__nome} teve a matrícula cancelada")

#Aqui permite que o peso do aluno seja atualizado.
def atualizar_peso(self, novo_peso):
    self.__peso = novo_peso

#Um calculo de IMC o __ torna o método privado.
def __calcular_imc(self):
    return self.__peso /(self.__altura ** 2)

#Calcula a quantidade ideal de água, métodos estatisticos não dependem de
#um objeto.
@staticmethod
def calcular_consumo_agua(peso):
    return peso * 0.035

#Mostra todos os dados do aluno e chama o calculo de IMC e de consumo
#de água.
def exibir_dados(self):
    print("==== DADOS DO ALUNO ====")
    print(f"Nome: {self.__Nome}")
    print(f"Idade:{self.__Idade}")
    print(f"Peso: {self.__Peso}Kg")
    print(f"Altura:{self.__Idade}m")
    print(f"Matriculado:{self.__matriculado}")
    print(f"Matriculado:{self.__calcular_imc():.2f}")
    print(f"Meta de água:")
    f"{AlunoAcademia.calcular_consumo_agua(self.__peso):.2f}litros"

#Criei o objeto aluno com algumas de suas características.
aluno1 = AlunoAcademia("Lucas",
    18,
    83,
    1.75
    )

aluno1.matricular()
aluno1.atualizar_peso(82)
aluno1.exibir_dados()





    
               


            
 