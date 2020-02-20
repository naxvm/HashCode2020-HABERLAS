from clases import *

process = lambda l: list(map(int, l.split()))

def parse(file):
    with open(file, 'r') as f:
        lines_raw = f.readlines()
    lines = list(map(process, lines_raw))

    total_days = lines[0][2]

    books = []
    for idx, score in enumerate(lines[1]):
        # info['books'][idx] = score
        book = Book(idx, score)
        books.append(book)
    
    libraries = []
    line_ix = 2
    library_idx = 0
    while line_ix < len(lines):
        if len(lines[line_ix]) == 0:
            break
        _, treg, rate = lines[line_ix]

        line_ix += 1

        books_idx = lines[line_ix]
        books_ = [books[ix] for ix in books_idx]
        library = Library(library_idx, books_, treg, rate)
        libraries.append(library)
        # info['libraries'][library_idx] = {
        #     'treg': treg,
        #     'rate': rate,
        #     'books': books}
        line_ix += 1
        library_idx += 1


    return books, libraries, total_days



def escribir_resultado(salida, filename='output.txt'):
    output = open(filename, 'w')
    salida_f = list(filter(lambda x: len(x[1]) > 0, salida))
    output.write(f'{len(salida_f)}\n')
    for library, books in salida_f:
        output.write(f'{library.id} {len(books)}\n')
        for book in books:
            output.write(str(book.id) + ' ')
        output.write('\n')

    output.close()


if __name__ == '__main__':
    d = parse('input_data/b_read_on.txt')