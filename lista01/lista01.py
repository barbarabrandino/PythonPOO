#Exercíco 01
preco_produto=float(input("Digite o valor do produto"))
numero_parecelas= float(input("Digite a quantidade de parcelas"))
valortotal= preco_produto * 1.1
valorparecela= valortotal / numero_parecelas
print("O valor de cada parecela é igual a",valorparecela,"e o valor total da compra é igual a",valortotal)

#Exercício 02
quantidade_inicial= float(input("Digite a quantidade inicial"))
quantidade_recebida= float(input("Digite o valor da quantidade recebida"))
quantidade_vendida= float(input("Digite a quantidade vendida"))
quantidade_final= quantidade_recebida + quantidade_inicial - quantidade_vendida
print(" A quantidade inicial é", quantidade_inicial)
print(" A quantidade recebida é", quantidade_recebida)
print("A quantidade vendida foi de", quantidade_vendida)
print("A quantidade total/final é de", quantidade_final)
#Exercicio 03
vitorias=float(input("Digite a quantidade de vitorias"))
derrotas= float (input("Digite a quantidade de derrotas"))
empates= float (input("Digite a quantidade de empates"))
pontosvitorias= vitorias*10
pontosempates= empates *5
pontosderrotas =  derrotas*0
pontuçãototal= pontosvitorias + pontosderrotas + pontosempates
print("O total de pontos foram de", pontuçãototal, "pontos!")

#Exercicio 04
venda = float(input("Digite o valor da(s) venda(s) em reais: "))
comissao = venda * 0.05

if venda >= 10000:
    comissao += 200

print("Comissão total:", comissao, "reais")

#Exercício 05
salario_bruto = float(input("Digite o valor do seu salário bruto: R$ "))
inss = salario_bruto * 0.10

if salario_bruto <= 2000:
    imposto = 0
elif 2001 <= salario_bruto <= 5000:
    imposto = salario_bruto * 0.10
else:
    imposto = salario_bruto * 0.20

salario_liquido = salario_bruto - imposto - inss

print("O seu salário líquido é de", salario_liquido, "reais")

#Exercício 6
compra = float(input("Digite o valor da compra em reais:  "))

if compra < 500:
    desconto = compra * 0.10
elif 500 <= compra <= 1000:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

valor_final = compra - desconto

print("Seu desconto foi de", desconto,"reais")
print("O valor final da compra é ", valor_final,"reais")

#Exercício 7
tabuada= int(input("Digite o numero da tabuada que deseja descobrir"))
for i in range(1,11):
  resultado= tabuada * i
  print("O valor da tabuda (1 ao 10) do:",tabuada,"é", resultado)

#Exercício 8
for i in range(10,0,-1):
  print(i)

print("Feliz ano novo")

#Exercício 9
soma_pares = sum(range(2, 101, 2))
print(soma_pares)

#Exercício 10
palavra= input("Digite uma palavra para saber quanras vogais há")
vogais = 'aeiouAEIOU'
contagem_vogais = sum(1 for letra in palavra if letra in vogais)
print("A palavra",palavra,"tem" ,contagem_vogais,"vogais.")

#Exercício 11
num= int(input("Digite um numero para descobir se é primo"))
primo= num> 1 and all (num % i for i in range (2,num))
if primo:
  print("É primo")
else:
  print("Não é primo")

# Exercício 12
import random

numero_secreto = random.randint(1, 10)

while True:
    resposta= int(input("Adivinhe o número entre 1 e 10: "))

    if resposta == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Errou, tente novamente.")

#Exercicio 13
import random

numero_secreto = random.randint(1, 10)


tentativas = 0


while True:
    resposta= int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1

    if resposta == numero_secreto:
        print("Parabéns! Você acertou em", tentativas, "tentativas!")
        break
    else:
        print("Errou, tente novamente.")

#Exercício 14
num = int(input("Digite um número positivo: "))

while num < 0:
    num = int(input("Por favor, digite um número positivo: "))

print("Você digitou o número positivo:", num)

#Exercício 15
while True:
    print("\nMenu de Cores:")
    print("1 - Vermelho")
    print("2 - Azul")
    print("3 - Verde")
    print("4 - Amarelo")
    print("5 - Sair")

    escolha = int(input("Escolha uma opção (1-5): "))

    if escolha == 1:
        print("Você escolheu a cor Vermelho.")
    elif escolha == 2:
        print("Você escolheu a cor Azul.")
    elif escolha == 3:
        print("Você escolheu a cor Verde.")
    elif escolha == 4:
        print("Você escolheu a cor Amarelo.")
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Exercício 16
def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")


resultado = calculadora(a, b, operacao)
print("Resultado:", resultado)


#Exercício 17
numero = float(input("Digite um número para descobrir se é par ou ímpar:"))

def eh_par(numero):
    if numero % 2 == 0:
        print("É par")
        return True
    else:
        print("Não é par")
        return False
eh_par(numero)

#Exercício 18
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas = input("Digite as notas separadas por espaço: ").split()

notas = [float(nota) for nota in notas]

resultado = calcular_media(notas)
print(resultado)


 #Exercício 19
nota1= float(input("Digite a primeira nota:"))

nota2= float(input("Digite a segunda nota:"))

nota3= float(input("Digite a terceira nota:"))

notas= [nota1,nota2,nota3]

media= sum(notas) / 3

print("Sua média é igual a:", media)

#Exercício 20
numeros= range(1,11)
par=[]
for num in numeros:
 if num % 2 ==0:
    par.append(num)
print(par)

#Exercício 21
listadecompras=[]
while True:
  compra= input("Adicione a sua lista de compra aqui:")

  if compra.lower()== 'sair':
      break

  listadecompras.append(compra)

print("Sua lista de compras:")
for compra in listadecompras:
  print(compra)

# Exercício 22
telefone = []

while True:
    adicionar = input("Adicione o nome e o contato (ou 'sair' para encerrar): ")

    if adicionar.lower() == 'sair':
        break

    telefone.append(adicionar)

print("\nSeus contatos:")
for contato in telefone:
    print(contato)

#Exercício 23
notas_alunos={}
while True:
  nome_aluno= input("Digite o nome do aluno:")
  if nome_aluno.lower():
    break
  elif nome_aluno:
    nota= float(input("digite a nota do(a)",nome_aluno,":"))
    notas_alunos[nome_aluno]= nota
  else:
     print("Nome do aluno não pode ser vazio. Tente novamente.")

print("Alunos e suas notas:")
for nome_aluno,nota in notas_alunos.items():
    print(nome_aluno, ":",nota)

# Exercício 24
dicionario = {
    "olá": "hello",
    "mundo": "world",
    "obrigado": "thank you",
    "amor": "love",
    "por favor": "please",
    "desculpe": "sorry",
}

while True:
    palavra = input("Digite uma palavra em português para traduzir (ou 'sair' para encerrar): ").lower()

    if palavra == 'sair':
        print("Saindo do tradutor.")
        break

    if palavra in dicionario:
        print("A tradução de", palavra, "é", dicionario[palavra])
    else:
        print("Desculpe, não encontrei a tradução para", palavra)






        