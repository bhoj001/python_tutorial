"""
method and variable overriding in other class
"""

class Mammal:
    species = 'mammal'

    def run(self):
        return "Fast"
    
    def sound(self):
        return "Some sound"
    

class ReptileBreed(Mammal):
    species = 'reptile'

    def run(self):
        return "slow"


s = ReptileBreed()
print(s.species)
print(s.run())
print(s.sound())