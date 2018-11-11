"""
Periodic Table Project
Knute & Kevin CS550 Healey
11/11/2018

This project transcribes a CSV file into a periodic table program
that can be accessed via user input through the command line.
CSV file name (if changed from default elements.csv) can be 
changed at the top of the program as variable, "filename".

Sources:
Splitting a String into Array: https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters
ANSI escape codes (for formatting and colors): http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
Opening and Reading CSV: https://docs.python.org/2/library/csv.html
Finding out if object is a string/int: https://stackoverflow.com/questions/4541155/check-if-a-number-is-int-or-float
Length of an Array: https://stackoverflow.com/questions/1712227/how-to-get-the-number-of-elements-in-a-list-in-python
Check if character is uppercase: https://stackoverflow.com/questions/45878324/how-to-check-if-string-has-lowercase-letter-uppercase-letter-and-number/

On My Honor, I have neither given nor received unauthorized aid
KEVIN XIE KNUTE BROADY
"""

import csv # for opening CSV files

filename = "elements.csv" # sets default CSV filename

class Element: # Class created to hold information on individual elements in periodic table
	def __init__(self): # Creates new element with no information
		pass
# SETTERS - sets values based on CSV file entries for elemental properties
	def setName(self,value): 
		self.name = value
	def setNumber(self,value):
		self.number = int(value)
	def setSymbol(self,value):
		self.symbol = value
	def setWeight(self,value):
		self.weight = float(value)
	def setBoil(self,value):
		try: # Only sets boil if boiling point is in CSV file
			self.boil = float(value)
		except:
			pass
	def setMelt(self,value):
		try:
			self.melt = float(value)
		except:
			pass
	def setDensity(self,value):
		try:
			self.density = float(value)
		except:
			pass
	def setFusion(self,value):
		try:
			self.density = float(value)
		except:
			pass
# GETTERS - returns values for elemental properties
	def getName(self):
		return self.name
	def getNumber(self):
		return self.number
	def getSymbol(self):
		return self.symbol
	def getWeight(self):
		return self.weight
	def getBoil(self):
		return self.boil
	def getMelt(self):
		return self.melt
	def getDensity(self):
		return self.density
	def getFusion(self):
		return self.fusion
# return as string instead of __repr__
	def __str__(self):
		return str(self.symbol)
	__repr__ = __str__ 

class PeriodicTable: # Class created to read CSV file, hold all elements, and execute functions based on user input
	def __init__(self): # New periodic table based on CSV entries
		self.element=[] # periodic table list
		with open(filename) as csv_file: # opens CSV file as csv_file
			csv_reader = list(csv.reader(csv_file, delimiter=",")) # reads csv file with commas as delimiters and then puts entries into 2D list
			for x in range(len(csv_reader)): # goes through every row of 2D list
				if x==0: # if x is 0, you are reading row 0, which is the column labels
					pass
				else:
					self.element.append(Element()) # adds new element to periodic table list
					for n in range(len(csv_reader[x])): # sets every possible value for new element using setters based on 2D list entries
						if n==0:
							self.element[x-1].setName(csv_reader[x][n])
						elif n==1:
							self.element[x-1].setNumber(csv_reader[x][n])
						elif n==2:
							self.element[x-1].setSymbol(csv_reader[x][n])
						elif n==3:
							self.element[x-1].setWeight(csv_reader[x][n])
						elif n==4:
							self.element[x-1].setBoil(csv_reader[x][n])
						elif n==5:
							self.element[x-1].setMelt(csv_reader[x][n])
						elif n==6:
							self.element[x-1].setDensity(csv_reader[x][n])
						elif n==7:
							self.element[x-1].setFusion(csv_reader[x][n])
	def index(self,value): # searches and returns single elements based on user inputted values (can be number, weight, symbol, or name)
		try:
			indexed = self.element[int(value)-1] # if value is an integer that exists within atomic numbers, indexed element is element with matching atomic number
		except: # catches errors if value is not an int
			try:
				for element in self.element: # else, if it is a float, then indexed element is element with matching atomic weight
					if float(element.getWeight()) == float(value):
						indexed = element
			except:
				pass # catches errors if value is not a float
		if len(value)<=2: # if length 2 or less and value is a string, indexed element is element with matching atomic symbol
			for element in self.element:
				if element.getSymbol() == value:
					indexed = element
		else: # otherwise, if string is longer than 2 characters, indexed element is element with matching name
			for element in self.element:
				if element.getName() == value:
					indexed = element
		return "\u001b[4mElement Name:\u001b[0m " + indexed.getName() + "\n\u001b[4mElement Symbol:\u001b[0m " + indexed.getSymbol() + "\n\u001b[4mAtomic Number:\u001b[0m " + str(indexed.getNumber()) + "\n\u001b[4mAtomic Weight:\u001b[0m " + str(indexed.getWeight())+" g/mol" # returns formatted response
	def parse(self,compound): # calculates total molecular weight of user inputted compound
		compound = list(compound) # splits compound into list of characters
		totalweight = 0.0 # sets beginning total weight
		for n in range(len(compound)): # goes through each character in the compound
			if compound[n].isupper()==True: # if character is upper-case alpha, it is an atomic symbol
				multiplier = 1.0 # sets initial multiplier (number of atoms in compound for each element) to 1
				symbol = compound[n] # sets element atomic symbol to character
				try:
					if compound[n+1].islower()==True: # if next character is lowercase alpha, then that is combined with first character to form new atomic symbol
						symbol = compound[n]+compound[n+1]
						if compound[n+2].isalpha()==False: # if next character is a digit, new multiplier is set to that number
							multiplier = float(compound[n+2])
							if compound[n+3].isalpha()==False: # if next character is another digit, new multiplier is that number concatenated with previous digit to create new multiplier
								multiplier = float(str(compound[n+2])+str(compound[n+3]))
					else:
						if compound[n+1].isalpha()==False: # same as above modifications to multiplier, but if atomic symbol is only one character
							multiplier = float(compound[n+1])
							if compound[n+2].isalpha()==False:
								multiplier = float(str(compound[n+1])+str(compound[n+2]))
				except IndexError: # if any of these values don't exist in the list, it is disregarded
					pass
				for element in self.element: # finds the corresponding element to atomic symbol
					if element.getSymbol() == symbol: 
						totalweight += float(element.getWeight())*multiplier # finds weight of corresponding element and adds (with multiplier) to total molecular weight
		return "\u001b[4mTotal Molecular Weight\u001b[0m: "+ str(totalweight)+ " g/mol" # returns weight
# return as string instead of __repr__
	def __str__(self):
		return str(self.element)
	__repr__ = __str__ 

def identify(response): # differentiates between single element user input and compound and acts accordingly
	responselist = list(response) # turns response into list of characters
	elementcount=0 # number of elements in response
	number=0 # number of numbers in response
	for n in range(len(responselist)): # goes through each character
		if responselist[n].isupper()==True: # adds 1 to element count for each uppercase character
			elementcount+=1
		elif responselist[n].isalpha()==False: # adds 1 to number count for each digit character (and returns error if there is a space)
			if responselist[n]==" ":
				return "Please try again"
			else:
				number+=1
	if (number>=1 and elementcount>=1) or (elementcount>1): # if user input is compound (more than one element or digit exists)
		return initPeriodicTable.parse(response)
	else: # if user input is element (only one element and no digits or multiple digits but no element)
		return initPeriodicTable.index(response)

while True:
	initPeriodicTable=PeriodicTable()
	print(identify(input("\nPlease input\n>>> ")))