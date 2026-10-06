"""
Programa Principal - Sistema de Inspeção de Segurança
Gerencia o menu interativo e coordena as chamadas das funções do módulo funcoes.py dentro do pacote models.
"""

from models.funcoes import criar_setor, excluir_setor, apresentar_resumo_relatorio, buscar_setor, listar_setores_cadastrados


def main():
    while True:
        print("\n=================================================")
        print("SISTEMA DE INSPEÇÃO DE SEGURANÇA")
        print("=================================================")
        print("1 - Criar setor")
        print("2 - Excluir setor")
        print("3 - Exibir relatório de falhas")
        print("4 - Buscar setor específico")
        print("5 - Listar setores cadastrados")
        print("0 - Sair")
        print("=================================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_setor()
        elif opcao == "2":
            excluir_setor()
        elif opcao == "3":
            apresentar_resumo_relatorio()
        elif opcao == "4":
            buscar_setor()
        elif opcao == "5":
            listar_setores_cadastrados()
        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()