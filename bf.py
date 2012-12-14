# Simple Python Bloom Filter
from array import array
import hashlib


def h1(element, length):
  m = hashlib.md5()
	m.update(str(element))
	return hash(m.hexdigest())%length

def h2(element, length):
	return hash(element)%length

def h3(element, length):
	m = hashlib.sha1()
	m.update(str(element))
	return hash(m.hexdigest())%length


k = list()
k.append(h1)
k.append(h2)
k.append(h3)

class BloomFilter:
	thearray = array('H')


	def Insert(self, item):
		for hashfunction in k:
			self.thearray[hashfunction(item,self.m)] = 1
		

	def Delete(self, item):
		pass

	def DeleteAll(self):
		for i in range(len(self.thearray)):
			self.thearray[i] = 0


	def Lookup(self, item):
		for hashfunction in k:
			if(self.thearray[hashfunction(item,self.m)] == 0):
				return False
		return True

	def Init(self, k, m):
		self.k = k
		self.m = m
		for i in range(self.m):
			self.thearray.append(0)

	def Print(self):
		print 'BloomFilter:',
		for i in range(self.m):
			print self.thearray[i],
		print




def main():
	bf = BloomFilter()
	bf.Init(k,32)
	bf.Print()
	bf.Insert("hello world")
	bf.Print()
	bf.Insert("Hello world")
	bf.Print()
	print "Is hello world in the BF?:",bf.Lookup('hello world')
	print "Is Hello world in the BF?:",bf.Lookup('Hello world')
	print "Is Hello World in the BF?:",bf.Lookup("Hello World")


if __name__ == '__main__':
	main()
