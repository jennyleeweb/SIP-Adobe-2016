class Dog():

	#Constructor function
	def _init_(self, furColor, eyeColor, name):
		self.furColor = furColor
		self.eyeCOlor= eyeColor
		self.name= name

	#Functions
	def bark(self):
		print("Woof!")

	def wag(self):
		print("Wagging Tail")

	def run(self):
		print("Your dog is running away")


Toto = Dog("Brown", "Blue", "Toto")

Toto.bark()
Toto.run()
