#!/usr/bin/python 

class Corbillard(object):
    def __init__(self):
        self.truckload = []
    
    fini = 'poil' 


class Cadavre(object):
    pass


class Membre(object):
    def craquer(self):
        print "craque"

class Spongieux(Membre):
    qualite = 6

class Main(Spongieux):
    def craquer(self):
        print "cric croque" 

class Pieds(Spongieux):
    pass


if __name__ == '__main__':
    corb = Corbillard()

