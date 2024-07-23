formasGlobais = {}

class Formas():
    
    def __init__(self):
        global formasGlobais
        self.formas = formasGlobais

    def adicionar(self, forma):
        self.formas[forma.getTipo() + str(forma.getNumero())] = forma

    def deleta(self, forma):
        del self.formas[forma.getTipo() + str(forma.getNumero())]

    def mostrar(self):
        print(f'Este plano cartesiano possui as seguintes formas:')
        for forma in self.formas.keys():
            print(forma)
    
    def atualizar(self,forma):
        for key in self.formas.keys():
            if self.formas[key].getTipo() == forma.getTipo() and self.formas[key].getNumero() == int(forma.getNumero()):
                self.formas[key] = forma

    def detalhes(self):
        for key in self.formas.keys():
            self.formas[key].toPrint()

    def pegarForma(self, key):
        return self.formas[key]

    def pegarPorTipoENumero(self,tipo,numero):
        for key in self.formas.keys():
            if self.formas[key].getTipo() == tipo and self.formas[key].getNumero() == int(numero):
                return self.formas[key]
    
    def pegarPorTipo(self,tipo):
        retorno = []
        for key in self.formas.keys():
            if self.formas[key].getTipo() == tipo:
                retorno.append(self.formas[key])
        return retorno
        
    def quantidadeDeFiguras(self,tipo = None):
        if tipo == None:    
            return len(self.formas)
        else :
            contador = 0
            for key in self.formas.keys():
                if self.formas[key].getTipo() == tipo:
                    contador += 1
            return contador