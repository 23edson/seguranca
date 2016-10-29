from bitarray import *

def addprefixos(xs, p):
    return dict((k, bitarray(p) + v) for (k,v) in xs.items())


def huffmann(lista):
	while(len(lista) > 1):
		lista.sort()
		a = lista.pop()
		b = lista.pop()
		#print(str(a) + " " + str(b))
		c = a.join(b)
		lista.append(c)
	d = lista.pop().coding()
	return d	

class N:
    def __init__(self, x, f):
        self.x = x
        self.f = f
        self.l = None
        self.r = None

    def join(self, o):
        n = N(None, self.f + o.f)
        n.l = self
        n.r = o
        return n

    def coding(self):
        
        l = {}
        r = {}
        if self.x:
            return {self.x: bitarray()}
        if self.l: 
            l = self.l.coding()
        if self.r:
            r = self.r.coding()
        ret = {}
        ret.update(addprefixos(l, '0'))
        ret.update(addprefixos(r, '1'))
        #if(self.x == 0):
        #    print(str(self.x) + " " + str(self.f) + str(len(ret)))
       
        return ret

    def __lt__(self, o):
        return self.f > o.f

    def __repr__(self):
        return "N(%s,%f)" % (self.x, self.f)