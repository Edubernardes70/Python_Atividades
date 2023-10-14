frutas_chaves ={"maça", "cereja", "banana","uva", "laranja"}
print(frutas_chaves)
print("\n")

frutas_lista = set(["uva", "manga", "manga", "uva"])
print(frutas_lista)
print("\n")

frutas_funcao=frutas_lista.copy()
print(frutas_funcao)
print("\n")

intercessao = frutas_chaves.intersection(frutas_funcao)

if intercessao:
    print(f"As frutas em comum são {intercessao}")
else:
    print("Não existe frutas em comum")
