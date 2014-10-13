from bs4 import BeautifulSoup
import numpy as np
from indicoio import sentiment

class Person(object):
	def __init__(firstName, lastName, email):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.emails = list()
	
	def addEmail(email):
		self.emails += email

class Date(object):
	def __init__(self, day=None, month=None, year=None, dayOfWeek=None):
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
	def __str__(self):
		return "Subject: " + self.subject + "\nDate: " + self.date.day + "\nSender: " + self.sender + "\nText: " + self.text + "\n"


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

			emailTextContent = ""
			finishedReading = False
			
			while(not finishedReading):
				emailLine = myFile.readline()
				# print emailLine
				if("-- next part ---" in emailLine or emailLine == ""):	
					finishedReading = True
				if emailLine[0:8] == "Subject:":
					newEmail.subject = emailLine[8:]
					continue
				if emailLine[0:5] == "Date:" or emailLine[0:5] == "Sent:":
					newEmail.date = getDateObjectFromString(emailLine)
					continue
				if emailLine[0:12] != "In-Reply-To:" and emailLine[0:11] != "References:" and emailLine[0:11] != "Message-ID:" and emailLine[0:39] != "-------------- next part --------------" and emailLine[0:1] != ">" and emailLine[0:1] != "<" and emailLine[0:5] != "From:" and emailLine[0:3] != "Cc:" and emailLine[0:3] != "To:" and emailLine[0:26] != "-----Original Message-----":
					emailTextContent += emailLine
			newEmail.text = emailTextContent
			emails += [newEmail]

	# print  data

	# soup = BeautifulSoup(data)
	# print(soup.get_text())
	allEmailContent = ""
	for anEmail in emails:
		allEmailContent += anEmail.text

	print allEmailContent
	print sentiment(allEmailContent)

def main():
	cleanData("octover2014.txt")


if __name__ == '__main__':
	main()