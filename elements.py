import csv
from gtts import gTTS
import os

class Element:
	def __init__(self,*argv):
		n=0
		for arg in argv[0]:
				if n==0:
					self.name = arg
				elif n==1:
					self.number = arg
				elif n==2:
					self.symbol = arg
				elif n==3:
					self.weight = arg
				elif n==4:
					self.boil = arg
				elif n==5:
					self.melt = arg
				elif n==6:
					self.density = arg
				elif n==7:
					self.fusion = arg
				n+=1
	def identify(self):
		text = "name: "+self.name+"\nnumber: "+self.number+"\nsymbol: "+self.symbol+"\nweight: "+self.weight
		language = 'en'
		myobj = gTTS(text=text, lang=language, slow=False) 
		myobj.save("sound.mp3") 
		os.system("afplay sound.mp3")
		return "name: "+self.name+"\nnumber: "+self.number+"\nsymbol: "+self.symbol+"\nweight: "+self.weight
	def __str__(self):
		return str(self.symbol)
	__repr__ = __str__ 

class PeriodicTable:
	def __init__(self):
		self.element=[]
		with open('elements.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=",")
			line_count=0
			for row in csv_reader:
				if line_count==0:
					line_count+=1
				else:
					self.element.append(Element(row))
					line_count +=1
	def index(self,value):
		try:
			return self.element[int(value)-1].identify()
		except:
			pass
		if len(value)<=2:
			for element in self.element:
				if element.symbol == value:
					return element.identify()
		else:
			for element in self.element:
				if element.name == value:
					return element.identify()
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
				except IndexError:
					pass
				for element in self.element:
					if element.symbol == symbol:
						totalweight += float(element.weight)*multiplier
		return totalweight
	def __str__(self):
		return str(self.element)
	__repr__ = __str__ 

initPeriodicTable=PeriodicTable()
print(initPeriodicTable.index(input("Please input\n>>> ")))