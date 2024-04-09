# trabalho sobre pesso 
peso = float(input('escreva o seu peso '))
altura = float(input('escreva a sua altura '))
imc = (peso/(altura*altura))
if imc <= 18.5:
    print ("vc esta muito magro ")
elif imc <= 24.9:
    print ("vc esta bem saudave ")
elif imc <= 29.9:
    print ("vc esta ficando acima do peso ")
elif imc <= 34.9:
    print("vc esta no grau de obesidade 1")
elif imc <= 39.9:
    print ("vc esta no grau de obesidade 2")
else :
    print ("vc precisa de ajuda rapido ") 
