# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
# sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
# naminių gyvūnų visiškai, arba turi ir šunį, ir katę.

# 2. funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
# ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
# bet turi bent vieną naminį gyvūną.

users = [
    {'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True},
    {'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False},
    {'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True},
    {'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False},
    {'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False},
    {'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True},
    {'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False},
    {'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True},
    {'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False},
]

def filter_all_or_nothing_people(sarasas):
    '''
    funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
    sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
    naminių gyvūnų visiškai, arba turi ir šunį, ir katę.
    '''
    filtruotas_sarasas = []
    for elementas in sarasas:
        if elementas['hasDog'] == False and elementas['hasCat'] == False or elementas['hasDog'] == True and elementas['hasCat'] == True:
            filtruotas_sarasas.append(elementas['name'])
    print('Vartotojai, kurie arba neturi naminių gyvūnų visiškai, arba turi ir šunį, ir katę:')
    return filtruotas_sarasas #return nes reikia grąžinti pagal užduotį

print(filter_all_or_nothing_people.__doc__) #atspausdina docstring komentarą
print(filter_all_or_nothing_people(users))

def filter_underaged_owners(sarasas):
    '''
    funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
    ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
    bet turi bent vieną naminį gyvūną.
    '''
    filtruotas_sarasas = []
    for elementas in sarasas:
        if elementas['hasDog'] == True and elementas['age'] <= 18 or elementas['hasCat'] == True and elementas['age'] <= 18:
            filtruotas_sarasas.append(elementas['name'])
    print('Vartotojai, kurie dar nėra pilnamečiai, bet turi bent vieną naminį gyvūną:')
    return filtruotas_sarasas #return nes reikia grąžinti pagal užduotį

print(filter_underaged_owners.__doc__) #atspausdina docstring komentarą
print(filter_underaged_owners(users))
