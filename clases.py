#!/usr/bin/python3
import numpy as np

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
        self.new_books = books

    def __repr__(self):
        return str(self.id)


    def getScore(self, scanned_books):
        self.new_books = list(filter(lambda x: x not in scanned_books, self.new_books))

        s1 = np.sum([b.score for b in self.new_books])
        s2 = self.rate
        s3 = self.treg

        return s1 * s2 / s3


    def scan_books(self):
        sorted_books = sorted(self.new_books, reverse=True, key=lambda b: b.score)

        # unique_books = []
        # for b in sorted_books:
        #     if not b in scanned_books:
        #         unique_books.append(b)
        return sorted_books
        # # print('nbooks', nbooks)
        # # first n books
        # # reverse para no joder la indexacion tras sacar libros
        # # primero los ultimos
        # sbooks = []

        # for idx in range(nbooks, 1, -1):
        #     # print('idx:', idx)
        #     # print('antes', self.books)
        #     sbooks.append(self.books.pop(idx-1))
        #     # print('despues', self.books)
        

        # return sbooks
