'''
Created on 18 fevr. 2019

@author: Denis
'''


class WorldView():
    
    def __init__(self, world, viewer):
        """world_view realise tout l'affichage de notre simulation
        arguments: world, le monde physique de notre simulation
                   viewer, pour l'affichage
        """
        self.viewer = viewer;
        
        self.robots = []  # tableau de robots physiques
        self.robots_view = dict()  # dictionnaire d'item canvas, pour garder un controle sur les dessins
                                    # NOTE : robots_view[i] doit correspondre a robots[i]
        for robot in world.robots:
            self.robots.append(robot)
        
        self.obstacles = []  # tableau d'obstacles physiques, on a pas besoin d'un stockage des item canvas
                            # vu qu'on est pas cense changer les dessins des obstacles
        for obstacle in world.obstacles:
            self.obstacles.append(obstacle)
            
        self.capteurs = []  # tableau de capteurs physiques
        self.capteurs_view = dict()  # les dessins des capteurs changeront donc dictionnaire
        for capteur in world.capteurs:
            self.capteurs.append(capteur)
        
        self.goal = world.goal
        self.world = world
    
    def draw_robots(self):
        
        i = 1
        for robot in self.robots:
            item = self.viewer.fenetre.create_polygon(robot.getCotes(), fill=robot.couleur)  # on dessine le robot
            self.robots_view["robot" + str(i)] = item  # on le stocke dans le dictionnaire de dessins
            i += 1
    
    def draw_obstacles(self):
        
        for obstacle in self.obstacles:
            self.viewer.fenetre.create_polygon(obstacle.getCotes(), fill='red')  # on dessine l'obstacle
    
    def draw_capteurs(self):
        
        i = 0
        for capteur in self.capteurs:
            item = self.viewer.fenetre.create_polygon(capteur.getCotes())  # on dessine le capteur
            self.capteurs_view["capteur" + str(i)] = item  # on le stocke dans le dictionnaire de dessins
            i += 1
    
    def draw_goal(self):
        self.viewer.fenetre.create_oval(self.goal.x, self.goal.y, self.goal.x1, self.goal.y1, fill='green')  # on dessine l'objectif
    
    def draw_world(self):
        
        self.viewer.afficher()
        self.draw_robots()
        self.draw_obstacles()
        self.draw_capteurs()
        self.draw_goal()
    
    # pour mettre a jour les dessins, pour que l'affichage reste coherente
    def update_robots(self):
        i = 0
        for item in self.robots_view.values():
            self.viewer.fenetre.coords(item , self.robots[i].A[0], self.robots[i].A[1], self.robots[i].B[0],
                                              self.robots[i].B[1], self.robots[i].C[0], self.robots[i].C[1])
            i += 1  # on met a jour le dessin avec les coordonnees du bon robot, d'ou l'importance que robots_view[i] doit correspondre a robots[i]
    
    def update_capteurs(self):
        i = 0
        for item in self.capteurs_view.values():
            self.viewer.fenetre.coords(item , self.capteurs[i].A[0], self.capteurs[i].A[1], self.capteurs[i].B[0],
                                              self.capteurs[i].B[1], self.capteurs[i].C[0], self.capteurs[i].C[1])
            
            if self.capteurs[i].detect_solides(self.world): #on rajoute de la complexite pour changer la couleur du capteur, worth ??
                self.viewer.fenetre.itemconfig(item, fill='orange')
            else:
                self.viewer.fenetre.itemconfig(item, fill='black')
                
            i += 1
    
    def update_world(self):
        self.update_robots()
        self.update_capteurs()
        self.viewer.actualiser()
