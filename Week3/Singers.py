class Singer():

	def __init__(self, skinTone, gender, vocalRange, hairLength, musicStyle, age, name):
		self.skinTone= skinTone
		self.gender= gender
		self.vocalRange=vocalRange
		self.hairLength=hairLength
		self.musicStyle=musicStyle
		self.age= age
		self.name= name
		self.pronoun = 'they'

	#Methods
	def pronouns():
		if (self.gender == 'female'):
			return self.pronoun = 'she'
		elif (self.gender == 'male'):
			return self.pronoun = 'he' 


	def singing(song):
		print("The famous" + self.name + " sings " + song + " in the range of " + self.vocalRange)

	def dancing(famousDancer):
		print("Whoa, " + self.name + " dances better than Beyonce. That's cray cray.")

