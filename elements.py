import csv

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
		pass
	def __str__(self):
		return str(self.element)
	__repr__ = __str__ 

initPeriodicTable=PeriodicTable()
print(initPeriodicTable.index(input("Please input name/symbol/number\n>>> ")))
