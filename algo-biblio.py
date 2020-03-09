#/usr/bin/python3

from clases import *
import functools
from parsers import parse, escribir_resultado
import sys
import time

BOOKS = {
    'a': 'a_example.txt',
    'b': 'b_read_on.txt',
    'c': 'c_incunabula.txt',
    'd': 'd_tough_choices.txt',
    'e': 'e_so_many_books.txt',
    'f': 'f_libraries_of_the_world.txt',
}


numero_libros = []
tiempos_registro = {}

in_file = 'input_data/' + BOOKS[sys.argv[1]]
out_file = 'output_data/' + BOOKS[sys.argv[1]]
print(in_file)
books, libraries, days = parse(in_file)


import pickle
with open('libros.pkl', 'wb') as f:
    pickle.dump(books, f)

with open('libraries.pkl', 'wb') as f:
    pickle.dump(libraries, f)

print('volcado')
def mejor_biblio(libraries, scanned):
    puntuaciones = []
    best_library = libraries[0]
    rest = []
    best_score = 0
    print('scanned:', len(scanned))
    for library in libraries[1:]:
        score = library.getScore(scanned)
        if score > best_score:
            best_score = score
            rest.append(best_library)
            best_library = library
        else:
            rest.append(library)

    return best_library, rest

    # puntuaciones = list(map(calcular_puntuacion, libraries)).sort()

    # return puntuaciones[-1]





def orden_libs_fn(l1, l2):
    if l1.treg < l2.treg:
        return -1
    elif l1.treg > l2.treg:
        return 1
    else:
        if l1.rate > l2.rate:
            return -1
        elif l1.rate < l2.rate:
            return 1
        else:
            if len(l1.books) > len(l2.books):
                return -1
            elif len(l1.books) < len(l2.books):
                return 1
            else:
                return 1

# hay que registrar primero las bibliotecas que tardan menos en 'registrarse'

salida = []
curr_days = 0
libros_ya_escaneados = set()
while len(libraries) > 0 and curr_days <= days:
    print('=====================')
    init = time.time()
    best_lib, libraries = mejor_biblio(libraries, libros_ya_escaneados)

    print(len(libraries), '---')
    print('Mejor biblio:', best_lib)
    print('Tiempo de procesado:', time.time() - init)
    libros = best_lib.scan_books()
    libros_ya_escaneados.update(libros)
    salida.append((best_lib, libros))
    curr_days += 1

print(f'Finish. day {curr_days}')
escribir_resultado(salida, out_file)

