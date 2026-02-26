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
