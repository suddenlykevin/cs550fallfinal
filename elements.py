"""
Periodic Table Project
Knute & Kevin CS550 Healey
11/11/2018

This project transcribes a CSV file into a periodic table program
that can be accessed via user input through the command line.
It uses classes, functions, for loops, and 2D lists as learned in class.
CSV file name (if changed from default elements.csv) can be 
changed at the top of the program as variable, "filename".

Sources:
Splitting a String into Array: https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters
ANSI escape codes (for formatting and colors): http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
Opening and Reading CSV: https://docs.python.org/2/library/csv.html
Finding out if object is a string/int: https://stackoverflow.com/questions/4541155/check-if-a-number-is-int-or-float
Length of an Array: https://stackoverflow.com/questions/1712227/how-to-get-the-number-of-elements-in-a-list-in-python
Check if character is uppercase: https://stackoverflow.com/questions/45878324/how-to-check-if-string-has-lowercase-letter-uppercase-letter-and-number/
Check if variable exists: https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
Capitalize ONLY first letter and don't titlecase: https://stackoverflow.com/questions/46390374/changing-the-first-letter-of-a-string-into-upper-case-in-python

On My Honor, I have neither given nor received unauthorized aid
KEVIN XIE KNUTE BROADY
"""

# for opening CSV files
import csv 

# sets default CSV filename and error checking (if last query was error, error = True)
filename = "elements.csv"
error = False

# Class created to hold information on individual elements in periodic table
class Element: 
# Creates new element with no properties (properties are set by setters)
	def __init__(self): 
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
		try: # Only sets boil if boiling point is in CSV file (the subsequent values are never used, but can be used if class is needed in a different program)
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

# Class created to read CSV file, hold all elements, and execute functions based on user input
class PeriodicTable: 
	# New periodic table based on CSV entries
	def __init__(self): 
		# Initiates periodic table as a list
		self.element=[] 
		# opening CSV
		with open(filename) as csv_file: 
			# reads CSV file with commas as delimiters and then puts entries into 2D list
			csv_reader = list(csv.reader(csv_file, delimiter=",")) 
			# Goes through every row in the 2D list
			for x in range(len(csv_reader)):
				if x==0: # if x is 0, you are reading row 0, which is the column labels
					pass
				else:
					# adds new property-less element to periodic table list
					self.element.append(Element()) 
					# sets every possible property for new element using setters based on 2D list entries
					for n in range(len(csv_reader[x])):
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
	# Searches and returns properties of single elements based on user inputted values (can be number, weight, symbol, or name)
	def index(self,value): 
		global error
		# if value is an integer that exists within atomic numbers, indexed element is element with matching atomic number (otherwise, error is caught)
		try:
			indexed = self.element[int(value)-1] 
		except: 
			# else, if it is a float, then indexed element is element with matching atomic weight (otherwise, error is caught again)
			try:
				for element in self.element: 
					if float(element.getWeight()) == float(value):
						indexed = element
			except:
				pass 
		# Any input that is non-string, non-float, and below 2 characters long is idnetified and indexed as an atomic symbol
		if len(value)<=2: 
			for element in self.element:
				if element.getSymbol() == value:
					indexed = element
		# Otherwise, if string is longer than 2 characters, indexed element is element with matching name
		else: 
			for element in self.element:
				if element.getName() == value:
					indexed = element
		# Checks if indexed element has been set, if not, it means that value is not an existing property and returns to start() as error
		if 'indexed' in locals(): 
			return "\n\u001b[4mElement Name:\u001b[0m " + indexed.getName() + "\n\u001b[4mElement Symbol:\u001b[0m " + indexed.getSymbol() + "\n\u001b[4mAtomic Number:\u001b[0m " + str(indexed.getNumber()) + "\n\u001b[4mAtomic Weight:\u001b[0m " + str(indexed.getWeight())+" g/mol" # returns formatted response
		else:
			error = True
			start() 
	# Calculates total molecular weight of user inputted compound
	def parse(self,compound): 
		# Splits compound into list of characters
		compound = list(compound) 
		# sets initial values (total weight is 0) and keeps track of multipliers (number)
		totalweight = 0.0
		multiplier = [] 
		symbol = [] 
		# goes through each character in the compound and checks: if character is uppercase followed by lowercase or singular uppercase (set to symbol), then if following character(s) are digits (set to multiplier)
		for n in range(len(compound)): 
			# only "counts" if character is first letter of an atomic symbol
			if compound[n].isupper()==True: 
				# sets initial multiplier for each element to 1 and initial atomic symbol to character
				multiplier.append(1.0) 
				symbol.append(compound[n]) 
				try:
					# if next character is lowercase alpha, then that is combined with first character to form new atomic symbol, then check if following symbols are digits (for multiplier)
					if compound[n+1].islower()==True: 
						symbol[-1] = compound[n]+compound[n+1]
						if compound[n+2].isalpha()==False: 
							multiplier[-1] = float(compound[n+2])
							if compound[n+3].isalpha()==False: 
								multiplier[-1] = float(str(compound[n+2])+str(compound[n+3]))
					else:
						# same as above modifications to multiplier, but if atomic symbol is only one character
						if compound[n+1].isalpha()==False: 
							multiplier[-1] = float(compound[n+1])
							if compound[n+2].isalpha()==False:
								multiplier[-1] = float(str(compound[n+1])+str(compound[n+2]))
				 # catches errors if it is the last few characters and n+1/n+2 is out of range
				except IndexError:
					pass
				 # finds the corresponding element to atomic symbol and adds element's atomic weight (using Getter) scaled by multiplier to total weight
				for element in self.element:
					if element.getSymbol() == symbol[-1]: 
						totalweight += float(element.getWeight())*multiplier[-1] 
		return [totalweight, symbol, multiplier] # returns all values - total weight, list of elements involved, and corresponding multipliers
# return as string instead of __repr__
	def __str__(self):
		return str(self.element)
	__repr__ = __str__ 

# user input prompt loop
def start(): 
	global error
	# if an error occured in previous query, inform user and return to no errors
	if error == True: 
		print("\n\n\u001b[31mAn error occured. Please try again with correct formatting.\u001b[0m")
		error = False
	print(identify(input("\n\nPlease input an \u001b[34;1matomic symbol, \u001b[32;1matomic weight, \u001b[33;1matomic name or \u001b[35;1matomic number\u001b[0m to recieve more information on that element. If you would like to reveive more information on a \u001b[36mmolecular compound\u001b[0m please input the formula\n\u001b[35m>>>\u001b[0m ")))
	start() # loop around for next query

# differentiates between single element user input and compound and send to either index or parse
def identify(response): 
	global error
	# turns response and adds first character capitalization (for flexibility) into list of characters to search through
	response = response[0].upper() + response[1:]
	responselist = list(response) 
	# sets initial number of elements and digits in input
	elementcount=0 
	number=0 
	# search through list
	for n in range(len(responselist)): 
		 # adds 1 to element count for each uppercase character
		if responselist[n].isupper()==True:
			elementcount+=1
		# adds 1 to number count for each digit character (and returns error if there is a non-digit other than a period for floats)
		elif responselist[n].isalpha()==False: 
			if responselist[n].isdigit()==False and responselist[n]!=".":
				error = True
				start()
			else:
				number+=1
	# if user input is compound (more than one element or element with digit exists), input is sent to parse
	if (number>=1 and elementcount>=1) or (elementcount>1): 
		# parse returns list of values [total weight, element symbols, element multipliers]
		variables = initPeriodicTable.parse(response) 
		# returns all values from parse in a readable manner (which varies in length due to compound complexity using for loop)
		response = "\n\u001b[4mTotal Molecular Weight\u001b[0m: "+ str(variables[0]) + "g/mol. \n\nElements Present:\n\n"
		for i in range(len(variables[1])):
			response+= str(int(variables[2][i-1])) + "x \n" + initPeriodicTable.index(variables[1][i-1]) + "\n\n"
		return  response
	# if user input is element (only one element and no digits or multiple digits but no element), input is sent to index and result returned
	else: 
		return initPeriodicTable.index(response)

# generates initial periodic table
initPeriodicTable=PeriodicTable() 
# let the fun begin!
start() 