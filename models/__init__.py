"""
Pacote Models - Sistema de Inspeção de Segurança
Contém os submódulos de funções e regras de negócio do sistema.
"""

# Importa as funções do módulo local 'funcoes.py'
from .funcoes import (
    criar_setor,
    excluir_setor,
    apresentar_resumo_relatorio
)

# Define os símbolos públicos do pacote
__all__ = [
    "criar_setor",
    "excluir_setor",
    "apresentar_resumo_relatorio"
]
