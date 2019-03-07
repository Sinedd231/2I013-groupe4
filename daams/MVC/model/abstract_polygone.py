# CLASSE ABSTRAITE


class Polygone(object):
    
    # retourne a partir d'une liste de vecteurs, les cotes correspondants
    # vu que le code est le meme peu importe la classe qui l'utilise, on le
    # factorise ici
    def getCotes(self):
        """retourne un tableau
        """
        cotes = []
        vecteurs = self.getVecteurs()
        n = len(vecteurs)
        
        for i in range(n):
            cotes.append([ vecteurs[i], vecteurs[(i + 1) % n] ]) 
        
        return cotes
    
    def getVecteurs(self):
        raise NotImplementedError("oubli d'instanciation de get vecteur")   # pour forcer les classes filles a redefinir la fonction
                                                                            # mais c'est quand meme moins puissant que java
    def nbrCotes(self):
        raise NotImplementedError("oubli d'instanciation de nbr cotes")
