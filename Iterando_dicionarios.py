notas = {
    "Matematica:": 8.5,
    "Português:": 9.0,
    "História:": 7.5,
    "Geografia:": 7.0,
    "Ciências:": 8.0
}
#ITERANDO SOBRE AS CHAVES DO DICIONARIO (chaves = Materias)
print("***Materias cursadas:***")
for materia in notas:
    print(materia)

print("\nMATERIA USANDO KEYS")
for materia in notas.keys():
    print(materia)

print("\nNotas do aluno:")
total = 0
for nota in notas.values():
    print(nota)


    total +=nota
media = total/len(notas)
print("\nMedia das notas: ", media)

#ITERANDO CHAVES E VALORES AO MESMO TEMPO

print("\nRELATÓRIO DE NOTAS")
for materia, nota in notas.items():
    print(materia, nota)
