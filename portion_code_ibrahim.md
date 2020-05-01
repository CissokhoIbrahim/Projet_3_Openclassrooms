```python
def top(self):
    self.check_move()
    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
    self.mac_gyver.coordinates[0] -= 1
    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

def check_move(self):
        objects = self.get_objects
        # Si c'est un chemin retourner vrai
        if self.mac_gyver.coordinates == 'c':
            return True
        if self.mac_gyver.coordinates == 'm':
            return False
        # Si l'object 't' est sur la case,  ramasser cet objet
        if self.mac_gyver.coordinates == 't':
            return True
        # Si l'object 'e' est sur la case, ramasser cet objet
        if self.mac_gyver.coordinates == 'e':
            return True
        # Si l'object 's' est sur la case, ramasser cet objet
        if self.mac_gyver.coordinates == 's':
            return True
        # Si le macgyver est sur la case du gardien et qu'il a ramasser les 3 objects, il aura gagné
        if self.mac_gyver.coordinates == 'g' and objects == 3:
            return True
        # Sinon tout ce qui sera endehors de ses diférentes conditions, sera False.
        return False



if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()

    print(m.parse_laby())
    m.top()
    print(m.parse_laby())
```