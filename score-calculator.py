def calcular_score(notas, cargas_horarias):
  print("Notas inseridas: ", len(notas))
  numerador = 0
  denominador = 0
  for i in range(len(notas)):
    fator = notas[i]*cargas_horarias[i]
    numerador += fator
    denominador += cargas_horarias[i]
  return numerador/denominador


print("Calculo de score")
print("Insira uma nota negativa para finalizar a inserção")
notas = []
pesos = []
while True:
  nota = float(input("Digite a nota da disciplina: "))
  if (nota < 0):
    print("Score: ", round(calcular_score(notas, pesos), 2))
    print("Vlw, flw!")
    break
  notas.append(nota)
  carga_horaria = int(input("Digite a carga horária: "))
  pesos.append(carga_horaria)
