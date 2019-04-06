"""
https://sourcemaking.com/design_patterns/composite/python/1
"""

import time

"""
Classe modelisant un algo de B&B
"""
class BranchAndBound(object):

    pbactuel = None
    nbnoeuds = 0
    
    """
        Constructeur qui prend un problème en paramètre
    """
    def __init__(self, pbactuel):
        super(BranchAndBound, self).__init__()
        self.borneSup = pbactuel

    """
        Méthode évaluer qui permet d'évaluer le problème en appliquant l'algorithme
        de branch and bound
    """
    def evaluer(self):
        debut = time.time()
        # Description du noeud
        print("Noeud racine :")
        print("Borne superieure : " + str(self.borneSup.evaluateZ()))
        print("Solution relaxée : \n\n" + str(self.borneSup) + "\n\n")
        # On trouve la variable réelle
        reelle = self.borneSup.getVariableReelle()
        if reelle != None :
            parametres = []
            for self.borneSup.param in self.borneSup.params:
                parametres.append(self.borneSup.param)
            # création du problème de gauche
            pb = PL(self.borneSup.valMax - (reelle.cout), parametres)
            pb.enleverParametre(reelle)
            solGauche = Solution(pb)
            solGauche.evaluer(self.borneSup)
            # création du problème de droite
            pb = PL(self.borneSup.valMax, parametres)
            pb.enleverParametre(reelle)
            soldroite = Solution(pb)
            soldroite.evaluer(self.borneSup)
        fin = time.time()
        print("Fin du branch and bound")
        print("Nombre de noeuds : " + str(BranchAndBound.nbnoeuds))
        print("Temps de calcul : " + str(fin - debut))
        print("Solution optimale : \n\n" + str(BranchAndBound.pbactuel))

class Solution(object):
    def __init__(self, probleme):
        self.probleme = probleme
        self.probleme.evaluateZ_Heurestique3()

    def evaluer(self, borneSup):
        BranchAndBound.nbnoeuds += 1
        # Description du noeud
        print("Noeud courant : " + str(BranchAndBound.nbnoeuds))
        print("Borne superieure : " + str(borneSup.evaluateZ()))
        print("Solution relaxée : \n\n" + str(self.probleme) + "\n\n")
        # Vérification de la satisfaction de la contrainte
        if self.probleme.coutZ() <= 1000 :
            # Comparaison entre la valeur actuelle et la valeur du noeud courant
            if BranchAndBound.pbactuel == None or BranchAndBound.pbactuel.evaluateZ() < self.probleme.evaluateZ() :
                # Récupération de la variable réelle
                reelle = self.probleme.getVariableReelle()
                print(reelle)
                if reelle != None :
                    # Si il y a une valeur réelle, séparation en deux sous problème
                    parametres = []
                    for self.probleme.param in self.probleme.params:
                        parametres.append(self.probleme.param)
                    # création du problème de gauche
                    pb = PL(self.probleme.valMax - (reelle.cout), parametres)
                    pb.enleverParametre(reelle)
                    solGauche = Solution(pb)
                    solGauche.evaluer(borneSup)
                    # création du problème de droite
                    pb = PL(self.probleme.valMax, parametres)
                    pb.enleverParametre(reelle)
                    soldroite = Solution(pb)
                    soldroite.evaluer(borneSup)
                else:
                    print("Meilleure solution trouvee : " + str(self.probleme))
                    BranchAndBound.pbactuel = self.probleme
        else:
            print("Coupe du noeud : non respect de la contrainte")

"""
Classe modelisant un probleme de programation lineaire
"""
class PL(object):
    """
        Constructeur qui prend l'ensemble des paramètres et la valeur max correspondant à la contrainte
        (1000 pour le problème)
    """
    def __init__(self, valMax, params):
        super(PL, self).__init__()
        self.params = dict()
        self.valMax = valMax
        for param in params:
            self.params.update({param: 0})

    """
        Méthode qui permet d'enlever un paramètre au problème linéaire
    """
    def enleverParametre(self, param):
        self.params.pop(param)

    """
        Méthode qui remet les variables à zero
    """
    def reset(self):
        for param in self.params:
            self.params[param] = 0

    def getVariableReelle(self):
        """
            Méthode qui permet de récupérer la variable réelle du problème
        """
        for param in self.params:
            resultat = param
            # Si on trouve une variable réelle, on la retourne
            if round(self.params[param]) != self.params[param]:
                return resultat
        return None    
            
    """
        Méthode qui permet de récupérer la durée totale
    """
    def evaluateZ(self):
        result = 0
        for param, coef in self.params.items():
            result = result + (param.duree * coef)
        return result

    """
        Méthode qui permet de récupérer le coût total
    """
    def coutZ(self):
        result = 0
        for param, coef in self.params.items():
            result = result + (param.cout * coef)
        return result

    """
        Méthode qui permet de récupérer l'ordre des variables en fonction de la première heuristique
    """
    def affiche_heurestique1(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param: param.cout)
        string = ""
        for p in result:
            string += str(p.nom + " ")
        return string
    
    """
        Méthode qui permet de récupérer l'ordre des variables en fonction de la deuxième heuristique
    """
    def affiche_heurestique2(self):
        resulttemp = []
        for param, coef in self.params.items():
            resulttemp.append(param)
        result = sorted(resulttemp, key=lambda param: param.duree)[::-1]
        string = ""
        for p in result:
            string += str(p.nom + " ")
        return string

    """
        Méthode qui permet de récupérer l'ordre des variables en fonction de la troisième heuristique
    """
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

    """
        Méthode d'évaluation du problème linéaire avec la première heuristique
    """
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
    """
        Méthode d'évaluation du problème linéaire avec la deuxième heuristique
    """
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
    """
        Méthode d'évaluation du problème linéaire avec la troisième heuristique
    """
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
    """
        Méthode toString pour afficher les informations du problème linéaire
    """
    def __str__(self):
        string = "Valeurs : \n\n"
        for param, coef in self.params.items():
            string += str(param.nom) + " = " + str(coef) + "\n"
        string += "\nDuree de la solution = " + str(self.evaluateZ()) + "\n"
        string += "Cout de la solution = " + str(self.coutZ()) + "\n"
        return string

"""
Classe de representation d'un parametre de programmation lineaire
"""
class Param(object):
    """
        Constructeur qui init le nom, la durée et le coût
    """
    def __init__(self, nom, duree, cout):
        super(Param, self).__init__()
        self.nom = nom
        self.duree = duree
        self.cout = cout

    def __repr__(self):
        return repr((self.nom, self.duree, self.cout))

"""
    Méthode main qui va afficher les données voulues
"""
def main():
    # Initialisation du problème linéaire
    parametres = []
    parametres.append(Param("x1", 9, 450))
    parametres.append(Param("x2", 2, 700))
    parametres.append(Param("x3", 3, 350))
    parametres.append(Param("x4", 13, 500))
    parametres.append(Param("x5", 6, 450))
    parametres.append(Param("x6", 5, 100))
    plineaire = PL(1000, parametres)
    # Affichage des réponses Questions 2 et 3
    affichageHeuristiques(plineaire)
    # Affichage du branch and bound
    applicationBranchAndBound(plineaire)
    
    

"""
    Méthode d'application de branch and bound sur le problème relaxé
    avec la troisième heuristique
"""
def applicationBranchAndBound(plineaire):
    print("Méthode de branch and bound \n")
    branch = BranchAndBound(plineaire)
    branch.evaluer()

"""
    Méthode d'affichage des résultats du problème relaxé avec les trois heuristiques
"""
def affichageHeuristiques(plineaire):
    print("Heuristique 1 \n")
    print("Ordre : " + plineaire.affiche_heurestique1())
    plineaire.evaluateZ_Heurestique1()
    print(plineaire)
    plineaire.reset()
    
    print("Heuristique 2 \n")
    print("Ordre : " + plineaire.affiche_heurestique2())
    plineaire.evaluateZ_Heurestique2()
    print(plineaire)
    plineaire.reset()

    print("Heuristique 3 \n")
    print("Ordre : " + plineaire.affiche_heurestique3())
    plineaire.evaluateZ_Heurestique3()
    print(plineaire)

    
if __name__ == '__main__':
    main()
