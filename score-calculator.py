def calc_score(notas, ch):
  print("Notas inseridas: ", len(notas))
  numerador = 0
  denominador = 0
  for i in range(len(notas)):
    denominador += ch[i]
    novo = notas[i]*ch[i]
    numerador += novo
  return numerador/denominador


print("Calculo de score")
print("Insira uma nota negativa para finalizar a inserção")
notas = []
pesos = []
while True:
  nota = float(input("Digite a nota da disciplina: "))
  if (nota < 0):
    print("Score: ", round(calc_score(notas, pesos), 2))
    print("Vlw, flw!")
    break
  notas.append(nota)
  ch = int(input("Digite a carga horária: "))
  pesos.append(ch)
