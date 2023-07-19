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


# Trata entrada para que seja uma letra entre A e D.
def isAD(entrada):
    OPCOES = ("A", "B", "C", "D")
    while entrada not in OPCOES:
        entrada = (
            input(
                " - ERROR - Digite as letras de acordo com a pergunta:\
                \n - Qual o Status da disciplina?\
                \n   [A]Aprovada [B]Reprovada por nota [C]Reprovada por falta [D]Trancada \n   "
            )
            .strip()
            .title()
        )
    return entrada


# Trata entrada para que seja um inteiro
def isInt(entrada):
    while not entrada.isdigit():
        entrada = input("Digite apenas números inteiros:")
    return int(entrada)


# Trata entrada para que seja um racional entre 0 e 10
def isFloat(entrada):
    while True:
        try:
            if float(entrada) > 10 or float(entrada) < 0:
                entrada = input(" - ERROR - Digite apenas números de 0 a 10:").replace(
                    ",", "."
                )
            else:
                return float(entrada)
        except ValueError:
            entrada = input(" - ERROR - Digite apenas números racionais:").replace(
                ",", "."
            )


# Função que será responsável pela criação dos dicionários das disciplinas:
def nova_disciplina():
    codigo = input(" - Digite o Código da disciplina: ")
    status = isAD(
        (
            input(
                " - Qual o Status da disciplina? \n   [A]Aprovada [B]Reprovada por nota [C]Reprovada por falta [D]Trancada \n   "
            )
        )
        .strip()
        .title()
    )
    carga = isInt(
        input(" - Digite a carga horária da disciplina ao todo no semestre: ")
    )
    periodo = isInt(
        input(
            " - Digite o semestre (adotando o semestre 1 o que foi de seu ingresso na UFC) em que fez essa disciplina: "
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
        nota = isFloat(
            input(" - Digite a nota final na disciplina: ").replace(",", ".")
        )

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
    # t = Carga horária das disciplinas trancadas
    t = sum(
        cadeira["Carga Horária"]
        for cadeira in lista_de_cadeiras
        if cadeira["Status"] == "Trancado"
    )
    # c = Carga horária total
    c = sum(cadeira["Carga Horária"] for cadeira in lista_de_cadeiras)
    # s1 = Somatório de (período * carga horária * nota) das disciplinas NÃO trancadas
    s1 = 0
    for cadeira in lista_de_cadeiras:
        if (
            cadeira["Status"] != "Reprovado por falta"
            and cadeira["Status"] != "Trancado"
        ):
            s1 += (
                min(cadeira["Período"], 6)
                * cadeira["Carga Horária"]
                * cadeira["Nota Final"]
            )
    # s2 = Somatório de (período * carga horária) das disciplinas NÃO trancadas
    s2 = 0
    for cadeira in lista_de_cadeiras:
        if (
            cadeira["Status"] != "Reprovado por falta"
            and cadeira["Status"] != "Trancado"
        ):
            s2 += min(cadeira["Período"], 6) * cadeira["Carga Horária"]

    # Fórmula dada pelo proprio site da UFC
    # https://prograd.ufc.br/pt/perguntas-frequentes/ira/
    ira = (1 - 0.5 * (t / c)) * (s1 / s2) * 1000

    return ira


# Código principal
while True:
    nova_disciplina()
    decisao = (
        (
            input(
                " - Existe alguma outra disciplina a ser adicionada?\n   [S]Sim [N]Nao\n   "
            )
        )
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
        ira = calcula_IRA()
        # Adoto que a ideia de multiplicar por 1000 é para desconsiderar casas decimais.
        print(f"Seu IRA é de {round(ira)}")
        break
