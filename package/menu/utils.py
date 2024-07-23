import os
import time
import sys

class Utils:

    def menuInicial():
        from package.menu.menuPrincipal import Menu
        menu = Menu()
        menu.printMenuInicial()

    def clearScreen():
        if os.name == 'nt':
           os.system('cls')
        else:  # Para sistemas Unix-like
           os.system('clear')
    
    def ehNumero(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def opcaoNaoDisponivel():
        Utils.clearScreen()
        print('Opção não disponível.')
        time.sleep(2)
        Utils.clearScreen()
        return
    
    def naoNumerico():
        Utils.clearScreen()
        print('Valor não numérico, tente outro valor!')
        time.sleep(2)
        Utils.clearScreen()
        return

    def sair():
        Utils.clearScreen()
        print("Programa encerrado!")
        sys.exit()

    def verificaInputDeCoordenadas(coordenadas,numero,objeto,telaDeRetorno):
        metodoDeRetorno = getattr(objeto, telaDeRetorno, None)
        numerosDescricao = {
            1: "uma",
            2: "dois",
            3: "três",
            4: "quatro",
            5: "cinco",
            6: "seis",
            7: "sete",
            8: "oito",
            9: "nove",
            10: "dez",
            11: "onze",
            12: "doze"
        }

        if len(coordenadas) != numero:
            Utils.clearScreen()
            print(f'Deve-se fornecer exatamente {numerosDescricao[numero]} números separados por vírgula.')
            time.sleep(3)
            Utils.clearScreen()
            metodoDeRetorno()

        retorno = []    
        for value in coordenadas:
            value = value.strip()
            if Utils.ehNumero(value) != True:
                Utils.clearScreen()
                print(f'O input possui valore(s) não numéricos. Tente novamente.')
                time.sleep(3)
                Utils.clearScreen()
                metodoDeRetorno()
            else: 
                value = float(value)
                if value.is_integer():
                    retorno.append(float(value))
                else:
                    retorno.append(float(value))
        return retorno

    def autor():
        Utils.clearScreen()
        # Códigos de cores ANSI
        GREEN_PHOSPHOROUS = '\033[92m'  # Verde brilhante
        RESET = '\033[0m'

        # ASCII art para "Marina"
        ascii_art = [
            " ##   ##    ##     ######    ####    ##   ##    ##",
            " ### ###   ####     ##  ##    ##     ###  ##   ####",
            " #######  ##  ##    ##  ##    ##     #### ##  ##  ##",
            " #######  ##  ##    #####     ##     ## ####  ##  ##",
            " ## # ##  ######    ## ##     ##     ##  ###  ######",
            " ##   ##  ##  ##    ##  ##    ##     ##   ##  ##  ##",
            " ##   ##  ##  ##   #### ##   ####    ##   ##  ##  ##"
        ]

        green_color = GREEN_PHOSPHOROUS
        for line in ascii_art:
            print(f"{green_color}{line}{RESET}")

        time.sleep(2)
        Utils.clearScreen()

    def verificaArea(area,objeto,telaDeRetorno):
        metodoDeRetorno = getattr(objeto, telaDeRetorno, None)
        if area <= 0 :
            Utils.clearScreen()
            print('Essa figura é impossível de ser criada, pois sua área é igual a zero. Por favor, envie outros dados.')
            time.sleep(3)
            Utils.clearScreen()
            metodoDeRetorno()
        else: 
            pass

    def formatarNumero(num):
        if isinstance(num, float):
            if num.is_integer():
                return f"{int(num)}"
            else:
                return f"{num:.2f}"
        else:
            return str(num)
