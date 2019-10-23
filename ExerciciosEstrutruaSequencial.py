'''
#1) Faça um programa que msotre a mensagem "Alo mundo".

print ("Alo mundo")
'''

'''
#2) Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = int(input("Digite um numero: "))
print("O numero digitado é: ", numero)
'''

'''
#3) Faça um Programa que peça dois números e imprima a soma.

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

soma = primeiro_numero + segundo_numero

print(soma)
'''

'''
4)Faça um Programa que peça as 4 notas bimestrais e mostre a média.


nota_primeiro_bimestre = int(input("Digite a nota do primeiro bimestre: "))
nota_segundo_bimestre = int(input("Digite a nota do segundo bimestre: "))
nota_terceiro_bimestre = int(input("Digite a nota do terceiro bimestre: "))
nota_quarto_bimestre = int(input("Digite a nota do quarto bimestre: "))

media = (nota_primeiro_bimestre + nota_segundo_bimestre + nota_terceiro_bimestre + nota_quarto_bimestre)/4

print("A media anual é: ", media)
'''

'''
5) Faça um Programa que converta metros para centímetros.


metros = int(input("Digite a quantidade em metros: "))
centimetros = metros*100

print("A medida em cemtimetros é: ", centimetros, "cm")
'''

'''
6) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input("Digite o raio: "))
area = raio*3.14**2
print("A area é: ", area, "m2")

'''
'''

7)Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.



largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

area = largura * altura

print("O dobra da área é: ", area*2, "m2")

'''

'''
8)Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.


valor_hora = int(input("Digite o valor da hora trabalhada: "))
horas_mes = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_mes = valor_hora * horas_mes

print("O salário do mês é : R$ ", salario_mes)
'''

'''
9) Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).


temp_farenheit = int(input("Digite a temperatura em Farenheit: "  ))

temp_celsius = (5 * (temp_farenheit - 32) / 9)

print("A temperatura em Celsius é : ", temp_celsius, "Cº")

'''
'''
10) Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.


temp_celsius = float(input("Digite a temperatura em graus Celsius : "))

temp_farenheit = ((temp_celsius/5)*9)+32

print ("Temperatura em Farenheit é: ", temp_farenheit)
'''


'''
11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.



num_int1 = int(input("Digite o primeiro numero inteiro: "))
num_int2 = int(input("Digite o segundo numero inteiro: "))
num_real = float(input("Digite um numero real: "))

a = (num_int1*2)*(num_int2/2)
print("O produto do dobro do primeiro com a metado do segundo é: ", a)

b = (num_int2*3) + num_real
print("A soma do triplo do primeiro com o terceiro é: ", b)

c = num_real**3
print(" O Terceiro numero ao cubo é: ",c)
'''

'''
12) Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58


altura = float(input("Digite sua altura: "))

peso_ideal = (72.7 * altura)-58

print("Seu peso ideal é: ", peso_ideal)
'''

'''
13)Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7


sexo = input("Digite o sexo. masculino ou feminino: ")
altura = float(input("Digite a sua altura: "))

if sexo == "masculino":
    peso_masc = (72.7 * altura) - 58
    print("Seu peso ideal é: ", peso_masc)
else:
    peso_fem = (62.1 * altura) - 44.7
    print("Seu peso ideal é: ", peso_fem)

'''

'''
14) João Papo-de-Pescador, homem de bem,
comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável
peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("Entre com o peso do peixe: "))

peso_regulado = 50
peso_excesso = peso_peixe - peso_regulado

multa = peso_excesso * 40
print("Peso total: ", peso_peixe, "kg")
print("O limite de peso por peixe é: ", peso_regulado, "kg")
print("A multa por excesso de peso é R$ 40,00, por kilo excedido")
print("A multa a pagar é: R$", multa)
'''


'''
15 Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

salarioHora = float(input('Digite o valor recebido por hora: R$ '))
horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))

salarioBruto = salarioHora + horasTrabalhadas

impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = impostoRenda + inss + sindicato

salarioLiquido = salarioBruto - descontos

print('Salário Bruto : R$ ', salarioBruto)
print('IR (11%) : R$ ', impostoRenda)
print('INSS (8%) : R$ ', inss)
print('Sindicato (5%) : R$ ', sindicato)
print('Salário Liquido : R$ ', salarioLiquido)




















