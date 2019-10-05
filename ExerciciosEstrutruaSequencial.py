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
'''

altura = float(input("Digite sua altura: "))

peso_ideal = (72.7 * altura)-58

print("Seu peso ideal é: ", peso_ideal)






















