import math
from datetime import datetime

# -----------------------------
# Função para calcular distância entre dois pontos usando a fórmula de Haversine
# -----------------------------
def calcular_distancia_km(lat1, lon1, lat2, lon2):
    R = 6371  # Raio médio da Terra em quilômetros
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Fórmula de Haversine para calcular a distância geográfica
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # Retorna a distância em km

# -----------------------------
# Lista global que armazena os relatos
# -----------------------------
relatos = []

# -----------------------------
# Função para cadastrar um novo relato
# -----------------------------
def cadastrar_relato(ponto_central):
    print("\n--- Cadastro de Relato ---")

    # Coleta de dados pessoais do relator
    nome = input("Nome completo: ")
    documento = input("Documento: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    # Coleta de informações do relato
    tipo = input("Tipo de catástrofe (ex: enchente, incêndio): ")
    descricao = input("Descrição: ")
    data = input("Data (DD-MM-AAAA): ")
    hora = input("Hora (HH:MM): ")
    lat = float(input("Latitude do relato: "))
    lon = float(input("Longitude do relato: "))

    # Calcula a distância do relato em relação ao ponto central
    distancia = calcular_distancia_km(ponto_central[0], ponto_central[1], lat, lon)

    # Validação: só salva relatos dentro de um raio de 10 km
    if distancia > 10:
        print(f"\nRelato fora do raio de 10 km ({distancia:.2f} km). Não será salvo.")
        return

    # Estrutura do relato
    relato = {
        "relator": {
            "nome": nome,
            "documento": documento,
            "email": email,
            "telefone": telefone,
            "localizacao": (lat, lon)
        },
        "tipo": tipo,
        "descricao": descricao,
        "data": data,
        "hora": hora,
        "coordenadas": (lat, lon)
    }

    # Adiciona o relato à lista global
    relatos.append(relato)
    print("Relato cadastrado com sucesso!\n")

# -----------------------------
# Função para buscar relatos com base no tipo de catástrofe
# -----------------------------
def buscar_por_tipo():
    tipo = input("\nDigite o tipo de catástrofe para buscar: ").lower()

    # Filtra relatos que correspondem ao tipo informado
    encontrados = [r for r in relatos if r['tipo'].lower() == tipo]

    # Exibe os resultados encontrados
    if not encontrados:
        print("Nenhum relato encontrado.")
    else:
        for i, r in enumerate(encontrados, 1):
            print(f"\nRelato {i} - {r['tipo'].capitalize()} em {r['data']} às {r['hora']} por {r['relator']['nome']}")
            print(f"Descrição: {r['descricao']}")
            print(f"Coordenadas: {r['coordenadas']}")

# -----------------------------
# Função principal com menu de navegação do sistema
# -----------------------------
def menu():
    print("""
============================
   GEORELATO - CLI SISTEMA
============================
    """)
    # Definição do ponto central com base no input do usuário
    lat_central = float(input("Digite a latitude do ponto central: "))
    lon_central = float(input("Digite a longitude do ponto central: "))
    ponto_central = (lat_central, lon_central)

    # Loop do menu
    while True:
        print("""
Opções:
1 - Cadastrar novo relato
2 - Buscar relatos por tipo
3 - Sair
        """)
        opcao = input("Escolha uma opção: ")

        # Tratamento da opção escolhida
        if opcao == '1':
            cadastrar_relato(ponto_central)
        elif opcao == '2':
            buscar_por_tipo()
        elif opcao == '3':
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# -----------------------------
# Ponto de entrada do programa
# -----------------------------
if __name__ == "__main__":
    menu()
