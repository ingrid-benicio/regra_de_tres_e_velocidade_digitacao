def numeroDesconhecido (numerador1,denominador1,denominador2):
    conta1 = str(denominador1) + 'x'
    conta2 = numerador1 * denominador2
    contaFeita = conta1 + ' = ' + str(conta2)
    resultado = conta2 / denominador1

    print(contaFeita)
    return resultado
    


print(numeroDesconhecido(1,2,3))



    