def divisaoFracao (denominador1,numerador1,denominador2,numerador2):
    resultado1 = denominador1 * numerador2
    resultado2 = denominador2 * numerador1
    total = "Resultado é: " + str(resultado1) + '/' + str(resultado2) 
    return total



print(divisaoFracao(1,5,2,4))


    