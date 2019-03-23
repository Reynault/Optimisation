"""
https://sourcemaking.com/design_patterns/composite/python/1
"""
'''
class BranchAndBound(object):
    """
    Classe modelisant un algo de B&B
    """
    def __init__(self, borneSup, valHeurestique, depth=0,neud = 0):
        super(BranchAndBound, self).__init__()
        self.depth = depth
        self.neud = neud
        self.borneSup = borneSup
        self.valHeurestique = valHeurestique

    def eval(self):

        pass

class Etat(object):
    """
    Classe Etat
    """
    def __init__(self, coutTotal, solution):
        super(Etat, self).__init__()
        self.coutTotal = coutTotal
        self.z = solution.evaluateZ()
        '''

class PL(object):
    """
    Classe modelisant un probleme de programation lineaire
    """
    def __init__(self, valMax, *params):
        super(PL, self).__init__()
        self.params = dict()
        self.valMax = valMax
        for param in params:
            self.params.update({param: 0})

    def reset(self):
        for param in self.params:
            self.params[param] = 0

    def evaluateZ(self):
        result = 0
        for param, coef in self.params.items():
            result = result + (param.duree * coef)
        return result

    def coutZ(self):
        result = 0
        for param, coef in self.params.items():
            result = result + (param.cout * coef)
        return result

    def affiche_heurestique1(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param: param.cout)
        string = ""
        for p in result:
            string += str(p.nom + " ")
        return string

    def affiche_heurestique2(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param: param.duree)[::-1]
        string = ""
        for p in result:
            string += str(p.nom + " ")
        return string

    def affiche_heurestique3(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param:
                        (param.cout / param.duree))
        string = ""
        for p in result:
            string += str(p.nom + " ")
        return string

    def evaluateZ_Heurestique1(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param: param.cout)

        i = -1
        while i < len(self.params):
            i += 1
            self.params[result[i]] = 1
            if (self.coutZ() > self.valMax):
                self.params[result[i]] = 0
                break

        if (i < len(self.params)):
            self.params[result[i]] = ((self.valMax - self.coutZ()) /
                                      float(result[i].cout))

    def evaluateZ_Heurestique2(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param: param.duree)[::-1]
        i = -1
        while i < len(self.params):
            i += 1
            self.params[result[i]] = 1
            if (self.coutZ() > self.valMax):
                self.params[result[i]] = 0
                break

        if (i < len(self.params)):
            self.params[result[i]] = ((self.valMax - self.coutZ()) /
                                      float(result[i].cout))

    def evaluateZ_Heurestique3(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param:
                        (param.cout / param.duree))
        i = -1
        while i < len(self.params):
            i += 1
            self.params[result[i]] = 1
            if (self.coutZ() > self.valMax):
                self.params[result[i]] = 0
                break

        if (i < len(self.params)):
            self.params[result[i]] = ((self.valMax - self.coutZ()) /
                                      float(result[i].cout))

    def __str__(self):
        string = ""
        for param, coef in self.params.items():
            string += str(param.nom) + " = " + str(coef) + "\n"
        string += "Duree de la solution = " + str(self.evaluateZ()) + "\n"
        string += "Cout de la solution = " + str(self.coutZ()) + "\n"
        return string

class Param(object):
    """
    Classe de representation d'un parametre de programmation lineaire
    """
    def __init__(self, nom, duree, cout):
        super(Param, self).__init__()
        self.nom = nom
        self.duree = duree
        self.cout = cout

    def __repr__(self):
        return repr((self.nom, self.duree, self.cout))

def main():
    p1 = Param("x1", 9, 450)
    p2 = Param("x2", 2, 700)
    p3 = Param("x3", 3, 350)
    p4 = Param("x4", 13, 500)
    p5 = Param("x5", 6, 450)
    p6 = Param("x6", 5, 100)
    plineaire = PL(1000, p1, p2, p3, p4, p5, p6)
    print("Heuristique 1 \n")
    print(plineaire.affiche_heurestique1())
    plineaire.evaluateZ_Heurestique1()
    print(plineaire)
    plineaire.reset()

    print("Heuristique 2 \n")
    print(plineaire.affiche_heurestique2())
    plineaire.evaluateZ_Heurestique2()
    print(plineaire)
    plineaire.reset()

    print("Heuristique 3 \n")
    print(plineaire.affiche_heurestique3())
    plineaire.evaluateZ_Heurestique3()
    print(plineaire)
    plineaire.reset()

if __name__ == '__main__':
    main()