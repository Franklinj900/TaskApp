class organizar:
    def __init__(self, cuartos: int, muebles: list):
        self.cuartos = cuartos
        self.muebles = muebles
        self.cocina = []
        self.baño = []
        self.escritorio = []
        
    def organizar_cocina(self):
        for i in self.muebles:
            if i.tipo == "cocina":
                self.cocina.append(i)
        return self.cocina
    def organizar_baño(self):
        for i in self.muebles:
            if i.tipo == "baño":
                self.baño.append(i)
        return self.baño

    def organizar_escritorio(self):
        for i in self.muebles:
            if i.tipo == "escritorio":
                self.escritorio.append(i)
        return self.escritorio

    def organizar_muebles(self):
        self.organizar_cocina()
        self.organizar_baño()
        self.organizar_escritorio()
        return self.cocina, self.baño, self.escritorio