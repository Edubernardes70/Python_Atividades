aluno ={
    "matricula":"A12345",
    "nome": "João Silva",
    "curso": "Engenharia da computação",
    "semestre": 5,
    "cr": 8.5
}
print(aluno)
print("\n")
aluno ["Hobbies"] = "Leitura", "Corrida", "Xadrez"
aluno ["Idade"]= 22
aluno ["semestre"] = 6
aluno ["cr"] = 8.7
print(aluno)
print("\n")
del aluno["Idade"]
print(aluno)
print("\n")
hobbies_removido = aluno.pop("Hobbies")
print(hobbies_removido)
print("\n")
metodo_popitem = aluno.popitem()
print(metodo_popitem)
print("\n")
copia1 = aluno.copy()
copia2 = dict(aluno)
print("Cópia 1", copia1)
print("Copia 2", copia2)