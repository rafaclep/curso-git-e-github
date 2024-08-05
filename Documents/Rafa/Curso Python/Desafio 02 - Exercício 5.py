#5. Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
#equilátero: todos os lados com o mesmo valor
#isósceles: dois lados com o mesmo valor
#escaleno: todos os lados com medidas distintas.

#tipos de triângulo

def tipos_de_triang(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'Equilátero'
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return 'Isósceles'
    else:
        return 'Escaleno'

#solicita ao usuário tipos do triângulo

print('Classificador de Triângulos')

lado1 = float(input('Qual a medida do lado 01? '))
lado2 = float(input('Qual a medida do lado 02? '))
lado3 = float(input('Qual a medida do lado 03? '))

#classifica o tipo de triângulo

classifica = tipos_de_triang(lado1, lado2, lado3)

print(f'O triângulo é: {classifica}!')









