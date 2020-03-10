```python

# Les différentes fonctions que Mac_gyver emprunte

def bottom(self):
	self.mac_gyver.coordinates[0] += 1

def top(self):
	self.mac_gyver.coordinates[0] -= 1

def left(self):
	self.mac_gyver.coordinates[1] -= 1

def right(self):
	self.mac_gyver.coordinates[1] += 1

# Une fonction qui récupère, trouve les nouvelles coordonées de macgyver et de sa position initiale et de sa direction et renvoie ses nouvelles coordonnées

def find_new_coo(self, direction=False):
	m_c = self.mac_gyver.coordinates

	if direction == "bottom":
		m_c[0] += 1

	if direction == "top":
		m_c[0] -= 1

	if direction == "left" :
		m_c[1] -= 1

	if direction == "right":
		m_c[1] += 1

		return m_c

def check_move(self, direction=None):
	case = self.find_new_coo()
	if direction == case:
		return True
	else:
		return False
```