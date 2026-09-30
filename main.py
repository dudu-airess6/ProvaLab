"""
Programa Principal - Sistema de Inspeção de Segurança
Gerencia o menu interativo e coordena as chamadas das funções do módulo funcoes.py.
"""

from funcoes import criar_setor, excluir_setor, apresentar_resumo_relatorio


def main():
    while True:
        print("\n=================================================")
        print("SISTEMA DE INSPEÇÃO DE SEGURANÇA")
        print("=================================================")
        print("1 - Criar setor")
        print("2 - Excluir setor")
        print("3 - Exibir relatório")
        print("0 - Sair")
        print("=================================================")

        opcao = input("Escolha uma opção: ").strip()

        # Validação com .isdigit() ensinada na Aula de Strings
        if not opcao.isdigit():
            print("\n[Erro] Entrada inválida! Por favor, digite um número (0, 1, 2 ou 3).")
            continue

        if opcao == "1":
            criar_setor()
        elif opcao == "2":
            excluir_setor()
        elif opcao == "3":
            apresentar_resumo_relatorio()
        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha entre 0, 1, 2 ou 3.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
