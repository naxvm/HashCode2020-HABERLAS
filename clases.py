#!/usr/bin/python3

class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __repr__(self):
        return str(self.id) + '-' + str(self.score)


class Library:
    def __init__(self, id, books, treg, rate):
        self.id = id
        self.books = books
        self.treg = treg
        self.rate = rate

    def __repr__(self):
        return str(self.id)


    def coge_libros(self, nbooks):
        # print('-----')
        nbooks = min(nbooks, len(self.books))
        # print('nbooks', nbooks)
        # first n books
        # reverse para no joder la indexacion tras sacar libros
        # primero los ultimos
        sbooks = []

        for idx in range(nbooks, 1, -1):
            # print('idx:', idx)
            # print('antes', self.books)
            sbooks.append(self.books.pop(idx-1))
            # print('despues', self.books)
        

        return sbooks
