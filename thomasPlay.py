from bs4 import BeautifulSoup

class Person(object):
	def __init__(firstName, lastName, email):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.emails = list()
	
	def addEmail(email):
		self.emails += email

class Date(object):
	def __init__(day, month=None, year=None, dayOfWeek=None):
		self.day = day
		self.month = month
		self.year = year
		self.dayOfWeek = dayOfWeek

class Email(object):
	def __init__(self, sender=None, date=None, subject=None, text=None):
		self.sender = sender
		self.date = date
		self.subject = subject
		self.text = text

def getDateObjectFromString(dateString):
	newDate = Date()
	newDate.day = dateString
	return newDate

def cleanData(fileName):
	emails = list()
	people = list()

	didEmailEnd = False
	# for myLine in open("october2014.txt", 'r'):

	myFile = open('october2014.txt', 'r')

	while(True):
		myLine = myFile.readline()
		if(myLine == ""):
			break

		if myLine[0:5] == "From:":
			# Start analysizing new email
			wasLastLineFrom = False

			newEmail = Email(sender = myLine)
			
			newEmail.date = getDateObjectFromString(myFile.readline())

			isReadingNewEmail = True
			while(isReadingNewEmail):
				emailLine = myFile.readline()
				if("-- next part ---" in myLine or myLine != ""):	
					isReadingNewEmail = False


	# print  data

	# soup = BeautifulSoup(data)
	# print(soup.get_text())

def main():
	cleanData("octover2014.txt")


if __name__ == '__main__':
	main()