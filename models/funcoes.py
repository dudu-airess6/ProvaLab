"""
Módulo de Gestão e Inspeção de Segurança - Abordagem 2 (Bloqueio / Validação)
Contém as rotinas para cadastro de setores, registro de equipamentos e geração de relatórios.
"""

__version__ = "1.2.0"
__author__ = "Sua Equipe"

# Estado Global / Lista de Resultados
relatorio_final = []


def ler_inteiro_valido(mensagem):
    """
    Lê uma entrada do usuário e garante que seja um número inteiro válido (>= 0).
    Utiliza .isdigit() para validação sem lançar exceções.
    """
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit():
            return int(entrada)
        print("Entrada inválida! Por favor, digite apenas números inteiros (ex: 0, 1, 2...).")


def gerar_relatorio_extintor(setor, numero, status_ok):
    """Registra um Extintor no relatório final."""
    status = "APROVADO" if status_ok else "REPROVADO"
    linha = f"{setor} | Extintor #{numero:02d} | Status: {status}"
    relatorio_final.append(linha)


def gerar_relatorio_sensor(setor, numero, status_ok):
    """Registra um Sensor de Fumaça no relatório final."""
    status = "VERIFICADO" if status_ok else "NÃO VERIFICADO"
    linha = f"{setor} | Sensor Fumaça #{numero:02d} | Status: {status}"
    relatorio_final.append(linha)


def criar_setor():
    """
    Cadastra um novo setor no sistema e realiza a inspeção dos equipamentos.
    Se o usuário informar 0 extintores e 0 sensores, o cadastro é cancelado
    por uma validação de regra de negócio (exige pelo menos 1 equipamento).
    """
    print("\n--- [1] CRIAR E INSPECCIONAR SETOR ---")
    nome = input("Insira o nome do setor: ").strip()
    if not nome:
        print("Nome de setor inválido!")
        return

    setor_nome = f"Setor {nome}"

    extintores = ler_inteiro_valido(f"Quantidade de extintores no {setor_nome}: ")
    sensores = ler_inteiro_valido(f"Quantidade de sensores no {setor_nome}: ")

    # Validação de regra de negócio
    if extintores == 0 and sensores == 0:
        print(f"\nErro: O '{setor_nome}' deve possuir pelo menos 1 equipamento (extintor ou sensor).")
        print("Cadastro do setor cancelado.")
        return

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


def excluir_setor():
    """Exclui todos os registros associados a um determinado setor."""
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


def apresentar_resumo_relatorio():
    """
    Analisa a lista relatorio_final, exibe o total de itens inspecionados
    e lista as falhas de segurança encontradas usando enumerate().
    """
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
        for i, falha in enumerate(falhas, start=1):
            print(f"{i}. {falha}")
    else:
        print("\nTODOS OS EQUIPAMENTOS ESTÃO EM CONFORMIDADE (OK).")
