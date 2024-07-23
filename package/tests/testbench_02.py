from package.maths.terms import Reta

def workspace():
    #criando a Reta
    reta1 = Reta(2,5)
    #Características 
    reta1.toPrint()
    #interpolando 
    print(f'Interpolando o valor 4: y = {reta1.interpolar(4)}') 
    #verificação certa
    reta1.estaNaReta(1,7)
    #calcula Distancia (zero)
    reta1.caculaDistancia(1,7)
    #verificação errada
    reta1.estaNaReta(1,4)
    #calcula Distancia
    reta1.caculaDistancia(1,4)
    #atualização 
    reta1.atualizar(3,6)
    #verificação certa
    reta1.estaNaReta(2,12)
    #calcula Distancia
    reta1.caculaDistancia(2,12)
    #verificação errada
    reta1.estaNaReta(5,2)
    #calcula Distancia
    reta1.caculaDistancia(5,2)

if __name__ == "__main__":

    workspace()

else:

    workspace()

