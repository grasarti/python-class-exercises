#Exercícios da aula 23_04_2025

# Exercício 1.1
# Crie um programa que exiba a seguinte mensagem na tela:
# Bem-vindo ao mundo da programação!


# print("Bem-vindo ao mundo da programação!")


# Exercício 2.1
# Declare variáveis para armazenar:
# Seu nome
# Sua idade
# Sua altura
# Se você está estudando Python (valor booleano)
# Depois, exiba essas informações usando o comando print()


#nome = "Graciela"
#idade = "39"
#altura = "1.63"
#estudante_python = "True"
#print(nome, idade, altura, estudante_python)


# Crie duas variáveis com números inteiros, some-as e mostre o resultado.

#a = 5
#b = 5
#print(a + b)


# Exercício 3.1
# Solicite ao usuário que informe seu nome e idade. Em seguida, mostre a mensagem:
# Olá, [nome]! Você tem [idade] anos.


#nome = input("Qual é o seu nome?")
#idade = int(input("Qual é a sua idade?"))
#print(f"Olá, {nome}! Você tem {idade} anos.")


# Exercício 3.2
# Peça dois números ao usuário, some-os e exiba o resultado na tela.


#num1 = int(input("Digite o primeiro número: "))
#num2 = int(input("Digite o segundo número: "))
#soma = num1 + num2
#print(f"A soma dos números é: {soma}")


# Exercício 4.1
# Peça um número ao usuário e exiba:
# - O dobro
# - O triplo
# - A raiz quadrada


#import math

#numero = float(input("Digite um número: "))
#dobro = numero * 2
#triplo = numero * 3
#raiz_quadrada = math.sqrt(numero)

#print(f"O dobro de {numero} é {dobro}")
#print(f"O triplo de {numero} é {triplo}")
#print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")



# Exercício 4.2 com classificação
# Crie um programa que calcule o IMC (Índice de Massa Corporal).
# Fórmula: IMC = peso / altura ** 2


#peso = float(input("Informe seu peso (em kg): "))
#altura = float(input("Informe sua altura (em metros): "))
#imc = peso / (altura ** 2)

#print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
#if imc < 18.5:
#    print("Classificação: Abaixo do peso")
#elif 18.5 <= imc < 24.9:
#    print("Classificação: Peso normal")
#elif 25 <= imc < 29.9:
#    print("Classificação: Sobrepeso")
#elif 30 <= imc < 34.9:
#    print("Classificação: Obesidade grau I")
#elif 35 <= imc < 39.9:
#    print("Classificação: Obesidade grau II")
#else:
#    print("Classificação: Obesidade grau III (obesidade mórbida)")



# Exercício 5.1
# Peça a idade do usuário e classifique conforme a faixa etária:
# Criança (até 12 anos)
# Adolescente (13 a 17 anos)
# Adulto (18 a 59 anos)
# Idoso (60 anos ou mais)

#idade = int(input("Informe sua idade: "))

#if idade <= 12:
#    print("Classificação: Criança")
#elif 13 <= idade <= 17:
#    print("Classificação: Adolescente")
#elif 18 <= idade <= 59:
#    print("Classificação: Adulto")
#else:
#    print("Classificação: Idoso")



# Exercício 5.2
# Peça uma nota entre 0 e 10 e informe:
# Aprovado (nota maior ou igual a 7)
# Recuperação (nota entre 5 e 6.9)
# Reprovado (nota menor que 5)

#nota = float(input("Digite sua nota (entre 0 e 10): "))

#if nota < 0 or nota > 10:
#    print("Nota inválida! Por favor, insira um valor entre 0 e 10.")
#elif nota >= 7:
#    print("Resultado: Aprovado ✅")
#elif 5 <= nota < 7:
#    print("Resultado: Recuperação ⚠️")
#else:
#    print("Resultado: Reprovado ❌")



# Exercício 6.1 – While
# Faça um programa que conte de 1 a 10 utilizando o laço while.

#contador = 1

#while contador <= 10:
#    print(contador)
#    contador += 1



# Exercício 6.2 – For
# Solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando o laço for.

numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

