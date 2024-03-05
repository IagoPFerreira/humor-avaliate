from fastapi import FastAPI

app = FastAPI()


def avaliar_humor(string: str) -> int:
    """
    Função para avaliar o humor de uma string.
    
    Args:
        string (str): A string a ser avaliada.
    
    Returns:
        int: O humor avaliado em uma escala de 1 a 10.
    """
    palavras_chave_positivas = [
      "feliz", "alegre", "amor", "ótimo", "adoro", "bom", "ótimo",
      "maravilhoso", "boa", "Adoro"
      ]
    palavras_chave_negativas = [
      "raiva", "triste", "chateado", "frustrado", "irritado"
      ]

    pontuacao = 5  # Inicialmente, pontuação neutra

    for palavra in palavras_chave_positivas:
        if palavra in string:
            pontuacao += 2  # Adiciona 2 pontos se uma palavra-chave positiva for encontrada

    for palavra in palavras_chave_negativas:
        if palavra in string:
            pontuacao -= 2  # Subtrai 2 pontos se uma palavra-chave negativa for encontrada

    # Garantindo que a pontuação esteja dentro do intervalo de 1 a 10
    pontuacao = max(1, min(pontuacao, 10))

    return pontuacao


@app.get("/")
async def root():
    """
    Endpoint para a raiz da API.

    Args:
        nenhum

    Returns:
        dict: Um dicionário contendo a mensagem "Hello World".
    """
    return {"message": "Hello World"}


@app.get("/avaliar-humor/{texto}")
async def calcular_humor(texto: str):
    """
    Endpoint para calcular o humor de uma string.

    Args:
        texto (str): A string cujo humor será calculado.

    Returns:
        dict: Um dicionário contendo o humor avaliado.
    """
    humor = avaliar_humor(texto)
    print(humor)
    return {"humor": humor}
