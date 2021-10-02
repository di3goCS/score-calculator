def calcular_score(notas, cargas_horarias):
  print("Notas inseridas: ", len(notas))
  numerador = 0
  denominador = 0
  for i in range(len(notas)):
    fator = notas[i]*cargas_horarias[i]
    numerador += fator
    denominador += cargas_horarias[i]
  return numerador/denominador

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)
    
print("Calculo de score")
print("Insira uma nota negativa para finalizar a inserção")
notas = []
pesos = []
while True:
  try:
    nota = float(input("Digite a nota da disciplina: "))
    if (nota < 0):
      score = round(calcular_score(notas, pesos), 2)
      print(bordered(f"Score: {score}"))
      print("Muito bem! Continue assim!" if score >= 7 else "Oh Shit! Melhor correr atrás do preju, brother!")
      break
    notas.append(nota)
    carga_horaria = int(input("Digite a carga horária: "))
    pesos.append(carga_horaria)
  except:
    print("Erro: Insira um número válido")
