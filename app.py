print ("Python caralhoo")

#Váriaveis

student_count = 1000 #int
rating = 4.99 #float
is_published = False #boolean
course_name1 = "String" 
course_name2 = """
String
Multi
Line
"""  #Pode se usar """ aspas triplas para dividir em várias linhas.

print(course_name2)

#Atribuição de váriavel multipla:

x = 1
y = 2

#Pode ser também:

x,y = 1,2

#Várias variaveis a uma:

x = y = 1

print(x)

#Para obter o endereço de memória:

print(id(x))


#Para obter tamanho de strings ou arrays

print(len(course_name2))

#Como pegar apenas um número de caracteres de uma string:

stringtest = 'Teste'
print(stringtest[0]) #Pega só o primeiro indice
print(stringtest[0:3]) #O valor a esquerda é onde ele deverá começar, o da direita onde termina

#Formatação de String:

primeiro_nome = 'Matheus'
sobrenome = 'Aparecido'

Nome_Completo = f"{primeiro_nome} {sobrenome}"

print(Nome_Completo)

#Funções e Métodos de Strings

print(Nome_Completo.upper()) #Para uppercase

print(Nome_Completo.find('t')) #Para achar o index da String

print(Nome_Completo.replace("M", "J")) #Para sobrepor um index de string, sendo o valor da esquerda o que você deseja sobrepor e o da direita o novo valor.

print("Matheus" in Nome_Completo)  #Para retornar um true ou false se o valor de string passado existe na variável de string. Também existe o not in.



#Números:

x = 10
x = 0b10 #Para utilizar valores binários, pode-se passar 0b de inicio e logo em seguida o valor desejado em binário
print(x)

print(bin(x)) #Utiliza-se o bin() para repassar o binário em sua forma original

x = 0x12c #Para passar valores hexadecimais, utiliza-se o 0x e logo em seguida o valor.

print(x)
print(hex(x))

#Para criar numeros complexos:

x = 1 + 2j #Utiliza-se o j

print (x)

#Operadores aritmeticos como em qualquer outra linguagem + - * / % **, unica mudança é que para obter-se valores INT em divisões pode-se utilizar //

x = 10 // 2
print(x)

x = x + 1
x += 1

#Funções e métodos de números

PI = 3.14 #Conveção em Python é de se utilizar uppercase para constantes

print(round(PI)) #Para retornar o numero INT

print(abs(PI)) #Para retornar o numero absoluto

import math #Importa uma biblioteca para funções de alta complexidade matematica

print(math.floor(PI))


#Tipos de listas:

#Listas normais, que são ordenadas e mutáveis e podem ter membros duplicados
#Tuple, coleção ordenada, não mutável e podem ter membros duplicados

lista = {"Matheus", "Ryan", "Gustavo"}
tuple1 = ("Matheus", "Ryan", "Gustavo")


#Condicionais

idade = int(input("Idade:"))

#if idade >= 18:
#    print("Adulto")
#elif idade >= 15:
#    print("Adolescente")
#else:
#    print("Criança")


#Operador Ternário, uma forma mais compacta de realizar um if/else. Exemplo:

#idade = 22
#if idade >= 18:
 #   print("Adulto")
#elif idade < 18:
 #   print("Menor de idade")

#Utilizando o ternário:

mensagem = "Adulto" if idade >=18  else "Menor de idade"

print(mensagem)


#For/while
lista = {1,2,3,4,5,6,7,8}
for x in lista:
    print(x)

for x in range(10):
    print(x)

conta = 0

while(conta <= 10):
    conta +=1

print(conta)    



#Ifs e for:

nomes = ['Jatheus', 'Ryan']
encontrado = False #O que é chamado de 'flag' para classificar momentos de uma condição
for nome in nomes:
    if nome.startswith('M'):
        print("Matheus na lista")
        encontrado = True
        break 
    if not encontrado:
        print("Não encontrado nenhum nome")
        break    

#Alternativa sem o flag:

nomes = ['Jatheus', 'Ryan']

for nome in nomes:
    if nome.startswith('M'):
        print("Matheus na lista")
       
        break 
   
else:                   #Este Else está ligado direto ao For, e não ao IF, portanto ele executará depois
                        #da iteração no for que não utilize break. Também pode ser utilizado no while.
    print("Não encontrado nenhum nome")
        

#Funções

def nome_funcao(lista_parametro):
    pass

def soma(a):
    somatoria = a+a
    return somatoria

def soma2(a,b=3):  #Passando um valor no parâmetro vc define um valor padrão para ele
    somatoria = soma(a) + soma(b)
    print(somatoria)


soma2(2,2)

#Definir restrições na função:

def funcao_teste(a: int, b: float) -> int: #A flecha se refere ao tipo de valor que será retornado
    soma = a + b
    print(soma)
    return soma

funcao_teste(1, 2.0)    


#Classes e Objetos

#Criar a classe:

class Robo:

    def __init__(self, nome, idade): #Construtores para melhor uso dos objetos, deve sempre se criar com __init__
        self.nome = nome
        self.idade = idade


    def se_apresente(self): #Obrigatório passar o self como argumento de funções em classes
        print("Meu nome é: " + self.nome + " e tenho " + self.idade + " anos de idade!") #Em Python, self é como this em java.

#Criar objeto em classes:
r1 = Robo("Matheus", "21") #r1 é o nome do objeto que quero criar relacionado a aquela classe.
r2 = Robo("Ryan", "13")

r1.se_apresente()
r2.se_apresente()






