## 📘 GeoRelato – Interface de Cadastro de Relatos de Catástrofes Naturais  
### 📚 Disciplina: Data Structures and Algorithms – Global Solution 2025.1

---

### 👨‍💻 Integrantes do Grupo

| Nome Completo         | RM       |
|------------------------|----------|
| Pietro Mauer Godoy     | RM564345 |
| João Pedro Daniel      | RM565783 |
| Fernando Antonio       | RM562549 |

---

### 📌 Descrição

Este projeto tem como objetivo criar uma **interface de linha de comando (CLI)** em **Python** que permita o cadastro e a consulta de relatos sobre **catástrofes naturais** (como enchentes, incêndios, deslizamentos, etc.) ocorridas **dentro de um raio de 10 km** de um ponto central fornecido pelo usuário.

---

### 🎯 Funcionalidades

- Cadastro de **dados pessoais do relator**
- Registro de **relatos geolocalizados**
- Validação da **distância** entre o relato e o ponto central (máx. 10 km)
- Organização dos dados em estrutura de lista
- Busca de relatos por **tipo de catástrofe**

---

### 🧪 Estruturas de Dados Utilizadas

- `list`: para armazenar os relatos como dicionários em memória.
- Justificativa: a lista é suficiente para volumes pequenos/médios de dados e permite percorrer, inserir e filtrar os elementos com facilidade.

---

### 📥 Entradas esperadas

- Latitude e longitude do ponto central (definido pelo usuário)
- Nome completo, documento, e-mail, telefone
- Tipo da catástrofe, descrição, data, hora
- Coordenadas geográficas do relato

---

### ✅ Regras de validação

- O sistema **só armazena relatos cuja distância até o ponto central seja ≤ 10 km**, com base na fórmula de Haversine.
- Dados pessoais devem estar completos.

---
### 🧠 Explicação do Código com Código-Fonte

```c
#include <stdio.h>   // Biblioteca para entrada e saída padrão (printf, scanf)
#include <stdlib.h>  // Biblioteca geral, aqui não é usada diretamente, mas pode ser útil
#include <string.h>  // Biblioteca para manipulação de strings (strcmp, strcasecmp)
#include <math.h>    // Biblioteca matemática para funções trigonométricas e constantes

#define MAX_RELATOS 100        // Define o número máximo de relatos que o programa pode armazenar
#define RAIO_TERRA_KM 6371.0   // Raio da Terra em quilômetros para cálculo de distância

// Estrutura que representa uma pessoa que faz o relato
typedef struct {
    char nome[100];       // Nome completo do relator
    char documento[50];   // Documento de identificação
    char email[100];      // Email do relator
    char telefone[20];    // Telefone do relator
    float lat;            // Latitude da localização do relator
    float lon;            // Longitude da localização do relator
} Relator;

// Estrutura que representa um relato de catástrofe
typedef struct {
    Relator relator;      // Informações do relator
    char tipo[50];        // Tipo de catástrofe (ex: enchente, terremoto)
    char descricao[200];  // Descrição detalhada do ocorrido
    char data[11];        // Data do relato no formato DD-MM-AAAA (10 caracteres + '\0')
    char hora[6];         // Hora do relato no formato HH:MM (5 caracteres + '\0')
    float lat;            // Latitude do local do relato
    float lon;            // Longitude do local do relato
} Relato;

// Array para armazenar todos os relatos cadastrados
Relato relatos[MAX_RELATOS];
int total_relatos = 0;    // Contador da quantidade de relatos cadastrados

// Função que converte graus para radianos (necessário para cálculos trigonométricos)
double graus_para_radianos(double grau) {
    return grau * M_PI / 180.0;
}

// Função que calcula a distância entre dois pontos geográficos usando a fórmula de Haversine
double calcular_distancia_km(float lat1, float lon1, float lat2, float lon2) {
    double phi1 = graus_para_radianos(lat1);                 // Latitude 1 em radianos
    double phi2 = graus_para_radianos(lat2);                 // Latitude 2 em radianos
    double delta_phi = graus_para_radianos(lat2 - lat1);     // Diferença das latitudes em radianos
    double delta_lambda = graus_para_radianos(lon2 - lon1);  // Diferença das longitudes em radianos

    // Fórmula de Haversine
    double a = sin(delta_phi / 2) * sin(delta_phi / 2) +
               cos(phi1) * cos(phi2) * sin(delta_lambda / 2) * sin(delta_lambda / 2);

    double c = 2 * atan2(sqrt(a), sqrt(1 - a));

    // Retorna a distância em km multiplicando pelo raio da Terra
    return RAIO_TERRA_KM * c;
}

// Função para cadastrar um novo relato, validando se está dentro do raio de 10 km do ponto central
void cadastrar_relato(float lat_central, float lon_central) {
    // Verifica se o limite de relatos já foi atingido
    if (total_relatos >= MAX_RELATOS) {
        printf("Limite de relatos atingido.\n");
        return;
    }

    Relato novo;

    // Entrada dos dados do relator
    printf("Nome completo: ");
    scanf(" %[^\n]", novo.relator.nome);         // Lê uma linha inteira até o '\n'
    printf("Documento: ");
    scanf(" %[^\n]", novo.relator.documento);
    printf("Email: ");
    scanf(" %[^\n]", novo.relator.email);
    printf("Telefone: ");
    scanf(" %[^\n]", novo.relator.telefone);

    // Entrada dos dados do relato
    printf("Tipo de catástrofe: ");
    scanf(" %[^\n]", novo.tipo);
    printf("Descrição: ");
    scanf(" %[^\n]", novo.descricao);
    printf("Data (DD-MM-AAAA): ");
    scanf(" %[^\n]", novo.data);
    printf("Hora (HH:MM): ");
    scanf(" %[^\n]", novo.hora);
    printf("Latitude do relato: ");
    scanf("%f", &novo.lat);
    printf("Longitude do relato: ");
    scanf("%f", &novo.lon);

    // Atualiza latitude e longitude do relator com as do relato
    novo.relator.lat = novo.lat;
    novo.relator.lon = novo.lon;

    // Calcula distância do relato para o ponto central
    double distancia = calcular_distancia_km(lat_central, lon_central, novo.lat, novo.lon);

    // Se o relato estiver fora do raio de 10 km, não é salvo
    if (distancia > 10.0) {
        printf("Relato fora do raio de 10 km (%.2f km). Não será salvo.\n", distancia);
        return;
    }

    // Salva o relato e incrementa o contador
    relatos[total_relatos++] = novo;
    printf("Relato cadastrado com sucesso!\n");
}

// Função para buscar relatos cadastrados por tipo de catástrofe
void buscar_por_tipo() {
    char tipo_busca[50];
    printf("Digite o tipo de catástrofe para buscar: ");
    scanf(" %[^\n]", tipo_busca);

    int encontrados = 0;
    // Percorre todos os relatos cadastrados
    for (int i = 0; i < total_relatos; i++) {
        // Compara o tipo do relato ignorando maiúsculas/minúsculas
        if (strcasecmp(relatos[i].tipo, tipo_busca) == 0) {
            encontrados++;
            // Exibe os detalhes do relato encontrado
            printf("\nRelato %d - %s em %s às %s por %s\n",
                   encontrados, relatos[i].tipo, relatos[i].data,
                   relatos[i].hora, relatos[i].relator.nome);
            printf("Descrição: %s\n", relatos[i].descricao);
            printf("Coordenadas: (%.4f, %.4f)\n", relatos[i].lat, relatos[i].lon);
        }
    }

    // Caso não encontre nenhum relato do tipo buscado
    if (encontrados == 0) {
        printf("Nenhum relato encontrado.\n");
    }
}

// Função principal do programa
int main() {
    float lat_central, lon_central;

    // Entrada da localização central para o filtro de relatos
    printf("Digite a latitude do ponto central: ");
    scanf("%f", &lat_central);
    printf("Digite a longitude do ponto central: ");
    scanf("%f", &lon_central);

    int opcao;
    do {
        // Menu principal do sistema
        printf("\n===== GEORELATO - CLI SISTEMA =====\n");
        printf("1 - Cadastrar novo relato\n");
        printf("2 - Buscar relatos por tipo\n");
        printf("3 - Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        // Executa a ação conforme a opção escolhida
        switch (opcao) {
            case 1:
                cadastrar_relato(lat_central, lon_central);
                break;
            case 2:
                buscar_por_tipo();
                break;
            case 3:
                printf("Encerrando o sistema. Até mais!\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }
    } while (opcao != 3);  // Continua até o usuário escolher sair

    return 0;  // Fim do programa
}


```



### 📁 Arquivos

| Nome do Arquivo       | Descrição                                         |
|------------------------|--------------------------------------------------|
| `README.md`            | Documentação do projeto                          |
| `geo_relato.c`        | Código-fonte principal do sistema CLI            |
| `geo_relato.py`        | Código em Python         |
| `integrantes.txt`      | Lista com nome e RM dos integrantes              |
| `link_repositorio.txt`      | Link do repositório           |
---

**Desenvolvido para a disciplina de Data Structures and Algorithms - Global Solution 2025.1 - FIAP**
