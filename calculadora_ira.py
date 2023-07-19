from os import system, name
lista_de_cadeiras = []

# Funções.
# Responsável por limpar o terminal.
def limpar():
    # Windows
    if name == "nt":
        system("cls")

    # Outros
    else:
        system("clear")

# Função que será responsável pela criação dos dicionários das disciplinas
def nova_disciplina():
    codigo = input("Digite o Código da disciplina: ")
    status = (
        (
            input(
                "Qual o Status da disciplina? \n[A]Aprovada [B]Reprovada por nota [C]Reprovada por falta [D]Trancada \n"
            )
        )
        .strip()
        .title()
    )
    carga = int(input("Digite a carga horária da disciplina ao todo no semestre: "))
    periodo = int(
        input(
            "Digite o semestre (adotando o semestre 1 o que foi de seu ingresso na UFC) em que fez essa disciplina: "
        )
    )
    if status.startswith("A"):
        status = "Aprovado"
    elif status.startswith("B"):
        status = "Reprovado por nota"
    elif status.startswith("C"):
        status = "Reprovado por falta"
    elif status.startswith("D"):
        status = "Trancado"
    if status != "Trancado":
        nota = float(input("Digite a nota final na disciplina: "))

    disciplina = {
        "Código": codigo,
        "Status": status,
        "Carga Horária": carga,
        "Período": periodo,
        "Nota Final": "Trancado" if status == "Trancado" else nota,
    }
    lista_de_cadeiras.append(disciplina)


# Função que fará o calculo do IRA
def calcula_IRA():
    def somatorio_de_chave(chave):
        somatorio = 0
        if chave == "trancadas":
            for cadeira in lista_de_cadeiras:
                if cadeira["Status"] == "Trancado":
                    somatorio += cadeira["Carga Horária"]

        elif chave == "carga":
            for cadeira in lista_de_cadeiras:
                somatorio += cadeira["Carga Horária"]

        elif chave == "nota final * periodo * carga horaria":
            for cadeira in lista_de_cadeiras:
                if (
                    cadeira["Status"] != "Reprovado por falta"
                    and cadeira["Status"] != "Trancado"
                ):
                    somatorio += (
                        min(cadeira["Período"],6)
                        * cadeira["Carga Horária"]
                        * cadeira["Nota Final"]
                    )

        elif chave == "carga horaria * periodo":
            for cadeira in lista_de_cadeiras:
                if cadeira["Status"] != "Trancado":
                    somatorio += min(cadeira["Período"],6) * cadeira["Carga Horária"]

        elif chave == "carga":
            for cadeira in lista_de_cadeiras:
                somatorio += cadeira["Carga Horária"]

        return somatorio

    t = somatorio_de_chave("trancadas")
    c = somatorio_de_chave("carga")
    s1 = somatorio_de_chave("nota final * periodo * carga horaria")
    s2 = somatorio_de_chave("carga horaria * periodo")

    # Formula dada pelo proprio site da UFC
    ira = (1 - 0.5 * (t / c)) * (s1 / s2) * 1000

    return ira


# Código principal
while True:
    nova_disciplina()
    decisao = (
        (input("Existe alguma outra disciplina a ser adicionada?\n [S]Sim [N]Nao: "))
        .strip()
        .title()
        .startswith("N")
    )
    limpar()
    print("DISCIPLINAS:")
    print()
    for disciplina in lista_de_cadeiras:
        print(disciplina)
        print()
    if decisao == True:
        break

ira = calcula_IRA()
# Adoto que a ideia de multiplicar por 1000 é para desconsiderar casas decimais.
print(f"Seu IRA é de {round(ira)}")
