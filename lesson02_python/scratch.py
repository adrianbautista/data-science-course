class data_scientist:
	tool = 'python'
	yearsofexperience = 20
	def obfuscate(self):
		print "I'd recommend using a support vector machine"

	def about(self):
		print "This data scientist's tool of choice is %s and years of experience is %s" % (self.tool,self.yearsofexperience)

class alien(data_scientist):
	superpower = 'teleportation'

def main():
	bug = alien()

	print "This alien's superpower is %s " % (bug.superpower)

	name = raw_input("Enter name of data scientist:")
	print "The Data Scientist's name is: %s" % (name)

if __name__ == "__main__":
	main()

