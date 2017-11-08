# Usando @property para chamar funcao sem usar os parenteses

class Animal():
	name = "Amy"
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"
	def get_color(self):
		return self.color

	@property
	def make_noise(self):
		return self.noise

dog = Animal()
# se chamar com parenteses diz que nao é callable
#print(dog.make_noise())
#print()

print(dog.make_noise)