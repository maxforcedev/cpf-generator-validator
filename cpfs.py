import random

def gerar_cpf(numero_de_cpfs):
    cpf_numero = 1
    for _ in range(numero_de_cpfs):
        numero_gerado = []

        # Gerando os 9 primeiros dígitos aleatórios
        while len(numero_gerado) < 9:
            numero_gerado.append(random.randint(0, 9))

        # Calculando o primeiro dígito verificador
        soma = sum(numero_gerado[i] * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        digito1 = 0 if resto == 10 else resto
        numero_gerado.append(digito1)

        # Calculando o segundo dígito verificador
        soma = sum(numero_gerado[i] * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        digito2 = 0 if resto == 10 else resto
        numero_gerado.append(digito2)

        # Formatando e salvando o CPF gerado
        cpf = f'{"".join(map(str, numero_gerado[:3]))}.{"".join(map(str, numero_gerado[3:6]))}.{"".join(map(str, numero_gerado[6:9]))}-{"".join(map(str, numero_gerado[9:]))}'

        with open('CFPs.txt', encoding='utf-8', mode='a') as file:
            file.write(f'CPF {cpf_numero}: {cpf}\n')
            cpf_numero += 1

def validar_cpf(cpf_inicial):
    try:
        if cpf_inicial.isdigit() and len(cpf_inicial) == 11:
            cpf = list(map(int, cpf_inicial[:9]))

            # Calculando o primeiro dígito verificador
            soma = sum(cpf[i] * (10 - i) for i in range(9))
            resto = (soma * 10) % 11
            digito1 = 0 if resto == 10 else resto
            cpf.append(digito1)

            # Calculando o segundo dígito verificador
            soma = sum(cpf[i] * (11 - i) for i in range(10))
            resto = (soma * 10) % 11
            digito2 = 0 if resto == 10 else resto
            cpf.append(digito2)

            # Verificando se o CPF é válido
            if cpf[9] == int(cpf_inicial[9]) and cpf[10] == int(cpf_inicial[10]):
                print(f'O CPF: {cpf_inicial} é válido.')
            else:
                print(f'O CPF: {cpf_inicial} NÃO é válido.')
        else:
            print('Erro na formatação do CPF. Certifique-se de inserir apenas os números e que o CPF tenha 11 dígitos.')
    except ValueError:
        print('Erro na formatação do CPF. Certifique-se de inserir apenas os números e que o CPF tenha 11 dígitos.')

def main():
    menu = int(input('Digite uma opção:\n[ 1 ] - Gerar CPFs:\n[ 2 ] - Validar CPF\n\n==>'))

    try:
        if menu == 1:
            numero_de_cpfs = int(input('Quantos CPFs deseja gerar? '))
            gerar_cpf(numero_de_cpfs)
        elif menu == 2:
            cpf = input('Digite o CPF que deseja validar:\n\nExemplo 1: 000.000.000-40\nExemplo 2: 00000000040\n\n==> ').replace('.', '').replace('-', '')
            validar_cpf(cpf)
        else:
            print('Digite somente as opções acima.')

    except ValueError:
        print('Digite um número inteiro para selecionar a opção do menu.')
    except Exception:
        print('Erro inesperado.')


if __name__ == "__main__":
    main()
