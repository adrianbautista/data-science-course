class data_scientist:
	name = "nerd"
	yearsofexperience = 20
	def obfuscate(self):
		print "I'd recommend using a support vector machine"

Dave = data_scientist()

print "This data scientist's name is %s and years of experience is %s" % (Dave.name,Dave.yearsofexperience)