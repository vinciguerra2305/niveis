import colorama
from colorama import Fore, Style
colorama.init()

def obter_alerta_colorido(nivel):
    
 
    # Lista de situações
    situacoes = [
        {"msg": "Nível 1: Muito baixo (crítico)", "cor": Fore.RED},
        {"msg": "Nível 2: Baixo", "cor": Fore.YELLOW},
        {"msg": "Nível 3: Médio", "cor": Fore.GREEN},
        {"msg": "Nível 4: Alto", "cor": Fore.CYAN},
        {"msg": "Nível 5: Muito alto (alerta)", "cor": Fore.BLUE}
    ]

    # Validação simples para evitar erros de índice
    if 1 <= nivel <= 5:
        config = situacoes[nivel - 1]
        return f"{config['cor']}{config['msg']}{Style.RESET_ALL}"
    else:
        return "Nível inválido para o sistema."

def simular_monitoramento():
  
    
    print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---")
    
    niveis_para_teste = [1, 2, 3, 4, 5]

    for n in niveis_para_teste:
        mensagem = obter_alerta_colorido(n)
        print(f"Status Atual: {mensagem}")

if __name__ == "__main__":
    try:
        simular_monitoramento()
    finally:
        Style.RESET_ALL