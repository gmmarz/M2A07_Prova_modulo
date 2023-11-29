def continuar_operacao()-> bool:
    while True:
        flg_op = input(f'Deseja repetir a operação (s)sim, (n)não ? ').lower()
        match flg_op:
            case 's':
                return True
            case 'n':
                return False
            case _:
                print('Digite apenas "s" para sim ou "n" para não')