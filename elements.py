import csv
# from gtts import gTTS
import os
import time
import sys

class Element:
	def __init__(self):
		pass
	def setName(self,value):
		self.name = value
	def setNumber(self,value):
		self.number = int(value)
	def setSymbol(self,value):
		self.symbol = value
	def setWeight(self,value):
		self.weight = float(value)
	def setBoil(self,value):
		try:
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

	def __str__(self):
		return str(self.symbol)
	__repr__ = __str__ 

class PeriodicTable:
	def __init__(self):
		self.element=[]
		with open('elements.csv') as csv_file:
			csv_reader = list(csv.reader(csv_file, delimiter=","))
			for x in range(len(csv_reader)):
				if x==0:
					pass
				else:
					self.element.append(Element())
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
	def index(self,value):
		try:
			indexed = self.element[int(value)-1]
		except:
			try:
				for element in self.element:
					if float(element.getWeight()) == float(value):
						indexed = element
			except:
				pass
		if len(value)<=2:
			for element in self.element:
				if element.getSymbol() == value:
					indexed = element
		else:
			for element in self.element:
				if element.getName() == value:
					indexed = element
		return "Element Name: " + indexed.getName() + "\nElement Symbol: " + indexed.getSymbol() + "\nAtomic Number: " + str(indexed.getNumber()) + "\nAtomic Weight: " + str(indexed.getWeight())
	def parse(self,compound):
		compound = list(compound) # https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters
		totalweight = 0.0
		for n in range(len(compound)):
			if compound[n].isupper()==True:
				multiplier = 1.0
				symbol = compound[n]
				try:
					if compound[n+1].islower()==True:
						symbol = compound[n]+compound[n+1]
						if compound[n+2].isalpha()==False:
							multiplier = float(compound[n+2])
					else:
						if compound[n+1].isalpha()==False:
							multiplier = float(compound[n+1])
							if compound[n+2].isalpha()==False:
								multiplier = float(str(compound[n+1])+str(compound[n+2]))
				except IndexError:
					pass
				for element in self.element:
					if element.getSymbol() == symbol:
						totalweight += float(element.getWeight())*multiplier
		return totalweight
	def __str__(self):
		return str(self.element)
	__repr__ = __str__ 

def identify(response):
	responselist = list(response)
	elementcount=0
	number=0
	for n in range(len(responselist)):
		if responselist[n].isupper()==True:
			elementcount+=1
		elif responselist[n].isalpha()==False:
			if responselist[n]==" ":
				sys.exit()
			else:
				number+=1
	if (number>=1 and elementcount>=1) or (elementcount>1):
		return initPeriodicTable.parse(response)
	else:
		return initPeriodicTable.index(response)

initPeriodicTable=PeriodicTable()
print(identify(input("Please input\n>>> ")))