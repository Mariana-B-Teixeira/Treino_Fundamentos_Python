# Input do usuário no sistema
import sys

# Requisições da API
import requests

def main():
    # Estabelece limite mínimo de Inputs
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        # Usuário insere quantidade de bitcoins (que deseja comprar, supostamente)
        n = float(sys.argv[1])

    # Trata erros de Input
    except ValueError:
        sys.exit("Command-line argument is not a number")

    except Exception as e:
        print("Missing command-line argument")


    try:
        # Requisição API
        r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=ff282cca2c7dbd24eae294657290575cfeade60bee1b25454f69443f17973818')
        # Erro de requisição HTTP
        r.raise_for_status()

        # Transfora texto puro em objeto nativo Python.
        price = r.json()

        # Guarda preço do bitcoin
        amount = price["data"]["priceUsd"]
        amount = float(amount)

        # Imprime custo total das bitcoins que o usuário inseriu
        print(f"${n * amount:,.4f}")

    # Tratamento de erros de requisição:
    except requests.RequestException:
        r.raise_for_status()

    except requests.exceptions.ConnectionError:
        print("Connection error.")

    except requests.exceptions.HTTPError:
        print("Invalid HTTP response")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.TooManyRedirects:
        print("Exceeded maximum number of redirects")

# Chama o main
if __name__ == "__main__":
    main()
