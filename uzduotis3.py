# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}

def get_dict_values(zodynas):
    '''
    Funkcija pasiima tik reikšmes (values) iš žodyno ir grąžina jų sąrašą
    Pirmiausiai pasidarome tuščią sarašą kur kelsime reikšmes iš žodyno
    Tada pasirašom ciklą kuriuo grąžiname supildytą reikšmių sąrašą
    Iškviečiame 'docstring' tipo komentarą
    Iškviečiame funkciją ir perduodame norimą žodyną kaip argumentą, kad pamatyti rezultatą dar ir atspausdiname
    '''
    sarasas = []
    for reiksme in zodynas:
        sarasas.append(zodynas[reiksme])
    return sarasas

  # jei reiktų atvaizduoti, o ne grąžinti (data prie f-jos iškvietimo nereiktų 'print')
  # for reiksme in zodynas:
    # print(zodynas[reiksme])

print(get_dict_values.__doc__)  #atspausdina docstring komentarą
print(get_dict_values(audi))
