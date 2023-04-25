#  Formula para  WPM ou PPM (Palavras por Minuto) é calculado com a quantidade total de palavras dividido pelo tempo gasto na digitação

def palavrasPorMinuto (contagemDePalavras,inicioDigitacao,fimDigitacao):
    return contagemDePalavras / (fimDigitacao - inicioDigitacao)

def tempoGasto(inicioTempo,finalTempo):
    return finalTempo - inicioTempo

print(round(palavrasPorMinuto(1797,30,18)))

print(round(tempoGasto(18,30)))

