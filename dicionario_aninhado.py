alunos = {
    "João": {
        "Matemática": 8.5,
        "Português": 9.0,
        "História": 7.5
    },
    "Maria":{
        "Matemática": 6.5,
        "Português": 8.0,
        "História": 9.5
    },
    "Tiago":{
        "Matemática": 8.5,
        "Português": 8.0,
        "História": 6.5,
        "Geografia": 9.0
    }
}

#ACESSANDO NOTAS DO JOÃO EM MATEMÁTICA

nota_joao_matematica = alunos["João"]["Matemática"]
print(f'A nota de João em Matemática é: {nota_joao_matematica}')

#MODIFICANDO A NOTA DE MARIA EM HISTORIA

alunos ["Maria"]["História"] = 10
print(f"Nota corrigida de Maria em História: {alunos['Maria']['História']}")

#ADICIONADO UMA NOTA DE QUIMICA PARA JOÃO
alunos ["João"]["Quimica"] = 8.8
print(f"Nota de João em Quimica: {alunos ['João']['Quimica']}")
