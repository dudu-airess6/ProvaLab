#Prova de Lab. Sistema de Gerenciamento de Setor 
# ----------------------------------------------------------------------
# Estado Global / Lista de Resultados
# (Listas são mutáveis: usamos .append() e modificamos em funções)
# ----------------------------------------------------------------------
relatorio_final = []


# ----------------------------------------------------------------------
# PROCEDIMENTO 1: Registra um Extintor no relatório
# ----------------------------------------------------------------------
def gerar_relatorio_extintor(setor, numero, status_ok):
    status = "APROVADO" if status_ok else "REPROVADO"
    # f-string com :02d para formatar o número com dois dígitos (ex: #01)
    linha = f"{setor} | Extintor #{numero:02d} | Status: {status}"
    relatorio_final.append(linha)


# ----------------------------------------------------------------------
# PROCEDIMENTO 2: Registra um Sensor de Fumaça no relatório
# ----------------------------------------------------------------------
def gerar_relatorio_sensor(setor, numero, status_ok):
    status = "VERIFICADO" if status_ok else "NÃO VERIFICADO"
    linha = f"{setor} | Sensor Fumaça #{numero:02d} | Status: {status}"
    relatorio_final.append(linha)


# ----------------------------------------------------------------------
# PROCEDIMENTO 3: Criar um novo setor e realizar inspeção
# ----------------------------------------------------------------------
def criar_setor():
    print("\n--- [1] CRIAR E INSPECCIONAR SETOR ---")
    nome = input("Insira o nome do setor: ").strip()
    if not nome:
        print("Nome de setor inválido!")
        return

    setor_nome = f"Setor {nome}"

    extintores = int(input(f"Quantidade de extintores no {setor_nome}: "))
    sensores = int(input(f"Quantidade de sensores no {setor_nome}: "))

    print(f"\n-> Iniciando inspeção do {setor_nome}...")

    # Inspeção dos Extintores
    for j in range(1, extintores + 1):
        resposta = input(f"  O extintor {j} foi testado? (s/n): ").strip().lower()
        status_ok = (resposta == "s")
        gerar_relatorio_extintor(setor_nome, j, status_ok)

    # Inspeção dos Sensores
    for k in range(1, sensores + 1):
        resposta = input(f"  O sensor {k} foi testado? (s/n): ").strip().lower()
        status_ok = (resposta == "s")
        gerar_relatorio_sensor(setor_nome, k, status_ok)

    print(f"\nSetor '{setor_nome}' inspecionado e cadastrado com sucesso!")


# ----------------------------------------------------------------------
# PROCEDIMENTO 4: Excluir todos os registros de um setor
# ----------------------------------------------------------------------
def excluir_setor():
    print("\n--- [2] EXCLUIR SETOR ---")
    if not relatorio_final:
        print("Nenhum setor cadastrado no relatório!")
        return

    nome = input("Insira o nome do setor a ser excluído: ").strip()
    setor_alvo = f"Setor {nome}"

    novos_registros = []
    removidos = 0

    for item in relatorio_final:
        if setor_alvo.lower() in item.lower():
            removidos += 1
        else:
            novos_registros.append(item)

    if removidos > 0:
        relatorio_final.clear()
        relatorio_final.extend(novos_registros)
        print(f"\nSetor '{setor_alvo}' excluído com sucesso! ({removidos} registros removidos)")
    else:
        print(f"\nNenhum registro encontrado para '{setor_alvo}'.")


# ----------------------------------------------------------------------
# PROCEDIMENTO 5: Analisa a lista relatorio_final e exibe o resumo
# ----------------------------------------------------------------------
def apresentar_resumo_relatorio():
    print("\n" + "=" * 50)
    print(f"RELATÓRIO FINAL: {len(relatorio_final)} ITENS INSPECIONADOS")
    print("=" * 50)

    if not relatorio_final:
        print("Nenhum item cadastrado no relatório até o momento.")
        return

    falhas = []
    for item in relatorio_final:
        if "REPROVADO" in item or "NÃO VERIFICADO" in item:
            falhas.append(item)

    if falhas:
        print(f"\n--- DETECTADAS {len(falhas)} FALHAS DE SEGURANÇA ---")
        for falha in falhas:
            print(falha)
    else:
        print("\nTODOS OS EQUIPAMENTOS ESTÃO EM CONFORMIDADE (OK).")
