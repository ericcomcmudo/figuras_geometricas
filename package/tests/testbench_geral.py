from package.maths.terms import Ponto,Reta, Circulo, Retangulo, Quadrado, Triangulo, TrapezioRet, Losango, Pentagono
from package.maths.formas import Formas

def workspace():
    p1 = Ponto(1,2)
    p1.toPrint()

    r1 = Reta(1,2)
    r1.toPrint()

    c1 = Circulo(1,2,3)
    c1.toPrint()

    q1 = Quadrado(1,2,3,4,5,6,7,8)
    q1.toPrint()

    rt1 = Retangulo(1,2,3,4,5,6,7,8)
    rt1.toPrint()

    tr1 = Triangulo(1,2,3,4,5,6)
    tr1.toPrint()

    t1 = TrapezioRet(1,2,3,4,5,6,7,8)
    t1.toPrint()

    l1 = Losango(1,2,3,4,5,6,7,8)
    l1.toPrint()

    pt1 = Pentagono(1,2,3,4,5,6,7,8,9,1,2)
    pt1.toPrint()

    dashboard = Formas()
    dashboard.adicionar(p1)
    dashboard.adicionar(c1)
    dashboard.adicionar(r1)
    dashboard.adicionar(q1)
    dashboard.adicionar(rt1)
    dashboard.adicionar(tr1)
    dashboard.adicionar(t1)
    dashboard.adicionar(l1)
    dashboard.adicionar(pt1)

    dashboard.mostrar()

    print("Detalhes:")
    dashboard.detalhes()

    print("Remove uma:")
    dashboard.deleta(p1)
    dashboard.mostrar()

    print("Atualizando forma:")
    copiac1 = dashboard.pegarForma('Círculo1')
    copiac1.atualizar(4,5,6)
    copiac1.toPrint()
    
    print('Finalizado com sucesso!')

if __name__ == "__main__":
    workspace()

else:
    workspace()