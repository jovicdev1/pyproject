print("Olá esté programa tem como objetivo testar algumas funções como if else loops e também inputs de dados.")

print("Primeiro iremos testar um input")
nome = string(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade <= 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")