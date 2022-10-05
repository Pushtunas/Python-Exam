# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

class Movie():
    '''
    filmų klasė "Movie", kuri turi pavadinimo, režisieriaus ir biudžeto savybes
    '''
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

def was_expensive(self):
    '''
    metodas was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
    grąžins True, kitu atveju - False
    '''
    if self.budget > 100000000:
        return True
    else:
        return False

movie1 = Movie('Gladiator', 'Ridley Scott', 103000000)
movie2 = Movie('Shutter Island', 'Martin Scorsese', 80000000)
movie3 = Movie('The Secret Life of Walter Mitty ', 'Ben Stiller', 90000000)

print(Movie.__doc__)
print(was_expensive.__doc__)

print(was_expensive(movie1))
print(was_expensive(movie2))
print(was_expensive(movie3))

