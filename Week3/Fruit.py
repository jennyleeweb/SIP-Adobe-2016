class Fruit():

	def __init__(self, color, shape, seedSize, taste):
		self.color= color
		self.shape =shape
		self.seedSize=seedSize
		self.taste= taste

	def rot(self):
		print("I am rotten ):")

	def ripen(self):
		print("I am ready to eat!")

Strawberry= Fruit("red", "triangular", "minuscule", "sweet")

Strawberry.rot()
Strawberry.ripen()




#attributes: color, shape, seedSize, taste
#methods: rotting, ripening, 