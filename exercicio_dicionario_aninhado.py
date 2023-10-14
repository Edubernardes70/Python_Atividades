estacionamento = {
    "A1": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "dono": "Sr. Silva"},

    "B2": {
        "marca": "Honda",
        "modelo": "Civic",
        "dono": "Dona Maria"},

    "C3": {
        "marca": "Ford",
        "modelo": "Mustang",
        "dono": "Sr. José"},

}

print('O modelo estacionado na vaga B2 é:',estacionamento["B2"]["modelo"])
estacionamento ["A1"]["dono"] = "Sra. Lúcia"
print(f'O carro na vaga A1 pertence a',estacionamento["A1"]["dono"])
estacionamento.update({"D4":{"marca": "Chevrolet", "modelo": "Onix", "dono": "Sr. Roberto"}})
print(estacionamento)
print(f'A marca do carro da Sra. Lucia é: ',estacionamento["A1"]["modelo"])