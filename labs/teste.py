from decimal import Decimal as dec

cambio_eur_usd = dec('1.10')

while True:

    # 1. Exibimos menu (ie, as opções)

    print("Escolha o sentido da conversão:")

    print("1. Euros -> Dólares")

    print("2. Dólares-> Euros")

    print("T. Terminar")

    # 2. Ler a opcao

    opcao = input("> ")

    # 3. Analisar e executar a opção

    if opcao == '1':

        montante = dec(input("Montante em euros: "))

        print(f'Dólares -> {montante * cambio_eur_usd:.2f}')

        # out.printf("Dólares -> %.2f\n", montante.multiply(cambioEurUsd))

    elif opcao == '2':

        montante = dec(input("Montante em dólares: "))

        print(f'Euros -> {montante / cambio_eur_usd:.2f}')

    elif opcao == 'T':

        break

    else:

        print(f"Opção <{opcao}> inválida!")

# JS : import {Decimal} from 'decimal'

# tipos primitivos / built-in: int, float, str, bool,

# str(23)