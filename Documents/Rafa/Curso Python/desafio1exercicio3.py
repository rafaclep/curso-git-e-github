# Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

print('Conversor de quilômetros em metros, centímetros e milímetros')

#Solicita ao usuário que coloque a quantidade de quilômetros

quilo = float(input('Digite a quantidade de quilômetros: '))

#Converte quilômetros para metros, centímetros e milímetros

metros = float(quilo * 1000)
centimetros = float(metros * 100)
milimetros = float(centimetros * 10)

#Demonstra o resultado ao usuário

print(f'Metros = {metros}')
print(f'Centímetros = {centimetros}')
print(f'Milímetros = {milimetros}')







