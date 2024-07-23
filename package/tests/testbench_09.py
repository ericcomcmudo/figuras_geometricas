from package.maths.terms import Pentagono

def workspace():
    #cria pentagono
    pentagono1 = Pentagono(1,2,3,4,5,6,7,8,9,8,5)
    #caracteristicas
    pentagono1.toPrint()
    #atualizando
    pentagono1 = Pentagono(0, 0, 1, 0, 1.309, 0.951, 0.721, 1.76, -0.279, 1.76, 1)

    #caracteristicas
    pentagono1.toPrint()
    #verifica
    pentagono1.verificaPosicao(2,2)
    pentagono1.verificaPosicao(0.55, 0.8942)
    pentagono1.verificaPosicao(1, 0)

if __name__ == "__main__":
    workspace()

else:
    workspace()