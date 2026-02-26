'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

# Mini projeto em Python: Calculadora de IMC
print("---CALCULADORA DE IMC---")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Qual a sua altura (m): "))

imc = peso / (altura * altura)

print("Seu IMC é:", round (imc, 2))

if imc < 18.5: 
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação acima do peso")
else: 
    print("Classsificação abaixo do peso")