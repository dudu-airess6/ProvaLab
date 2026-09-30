"""
Módulo de Gestão e Inspeção de Segurança
Contém as rotinas para cadastro de setores, registro de equipamentos e geração de relatórios.
"""

__version__ = "1.1.0"
__author__ = "Eduardo Aires, Guilehrme Augusto, Erick, Neto e Bezerra"

# ----------------------------------------------------------------------
# Estado Global / Lista de Resultados
# (Listas são mutáveis: usamos .append() e modificamos em funções)
# ----------------------------------------------------------------------
relatorio_final = []


def gerar_relatorio_extintor(setor, numero, status_ok):
    """Registra o status de inspeção de um extintor no relatório final."""
    status = "APROVADO" if status_ok else "REPROVADO"
    # f-string com :02d para formatar o número com dois dígitos (ex: #01)
    linha = f"{setor} | Extintor #{numero:02d} | Status: {status}"
    relatorio_final.append(linha)


def gerar_relatorio_sensor(setor, numero, status_ok):
    """Registra o status de inspeção de um sensor de fumaça no relatório final."""
    status = "VERIFICADO" if status_ok else "NÃO VERIFICADO"
    linha = f"{setor} | Sensor Fumaça #{numero:02d} | Status: {status}"
    relatorio_final.append(linha)


def ler_inteiro_valido(mensagem):
    """Lê uma entrada do usuário e valida se é um número inteiro usando .isdigit()."""
    entrada = input(mensagem).strip()
    while not entrada.isdigit():
        print("  [Erro] Por favor, digite apenas um número inteiro válido.")
        entrada = input(mensagem).strip()
    return int(entrada)


def criar_setor():
    """Solicita os dados de um novo setor e realiza a inspeção de seus equipamentos."""
    print("\n--- [1] CRIAR E INSPECCIONAR SETOR ---")
    nome = input("Insira o nome do setor: ").strip()
    if not nome:
        print("Nome de setor inválido!")
        return

    setor_nome = f"Setor {nome}"

    # Validação com .isdigit() ensinada na Aula de Strings
    extintores = ler_inteiro_valido(f"Quantidade de extintores no {setor_nome}: ")
    sensores = ler_inteiro_valido(f"Quantidade de sensores no {setor_nome}: ")

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
    """Remove todos os registros associados a um setor do relatório final."""
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
    """Exibe a quantidade total de itens inspecionados e lista as falhas com enumerate()."""
    print("\n" + "=" * 50)
    print(f"RELATÓRIO FINAL: {len(relatorio_final)} ITENS INSPECIONADOS")
    print("=" * 50)

    if not relatorio_final:
        print("Nenhum setor cadastrado no relatório até o momento.")
        return

    falhas = []
    for item in relatorio_final:
        if "REPROVADO" in item or "NÃO VERIFICADO" in item:
            falhas.append(item)

    if falhas:
        print(f"\n--- DETECTADAS {len(falhas)} FALHAS DE SEGURANÇA ---")
        # Uso do enumerate() ensinado na Aula 04 para exibição numerada
        for i, falha in enumerate(falhas, start=1):
            print(f"{i}. {falha}")
    else:
        print("\nTODOS OS EQUIPAMENTOS ESTÃO EM CONFORMIDADE (OK).")
