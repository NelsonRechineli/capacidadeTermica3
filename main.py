#recebe a quantidade de calor
quantidadeCalor = float(input("Quantidade de calor em Calorias: ")) 
#recebe a temperatura inicial
tempInicial = float(input("Temperatura inicial: ")) 
#recebe a temperatura final
tempFinal = float(input("Temperatura final: ")) 

#fórmula da variação de temperatura
variacaoTemperatura = tempFinal - tempInicial

#função pra trazer a capacidade termica
def obterCapacidadeTermica(quantidadeCalor):
#capacidade térmica = quantidade de calor/variação da temperatura
  return quantidadeCalor / variacaoTemperatura

print(f"A capacidade térmica do corpo foi de : {obterCapacidadeTermica(quantidadeCalor):,.2f} calorias por grau Celsius (cal/Cº)")