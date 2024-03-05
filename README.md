# Avaliação de Humor com FastAPI

Este é um exemplo simples de uma aplicação usando o FastAPI para avaliar o humor de uma string em uma escala de 1 a 10.

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema. Você pode fazer o download em <https://www.python.org/downloads/>.
2. Abra o terminal ou prompt de comando.
3. Instale os pacotes necessários usando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando a aplicação

Após instalar os pacotes, você pode executar a aplicação com o seguinte comando:

```bash
uvicorn main:app --reload
```

Isso iniciará o servidor FastAPI e sua aplicação estará pronta para receber solicitações.

## Uso

Você pode enviar uma solicitação GET para o endpoint `/avaliar-humor/{texto}` com uma string como parâmetro para calcular o humor da string.

Por exemplo, para avaliar o humor da string "Estou muito feliz hoje!", você pode enviar a seguinte solicitação:

```perl
GET /avaliar-humor/Estou%20muito%20feliz%20hoje!
```

A resposta será um JSON contendo o humor avaliado:

```json
{ "humor": 8 }
```

## Testes

Este projeto inclui testes unitários para a função avaliar_humor. Você pode executar os testes usando o seguinte comando:

```bash
python3 -m unittest test_main.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request com melhorias ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

```css
Este README fornece uma visão geral da instalação, execução, uso, testes, contribuições e licença da aplicação. Certifique-se de incluir informações relevantes para os usuários, como requisitos de instalação e uso básico da aplicação.
```
