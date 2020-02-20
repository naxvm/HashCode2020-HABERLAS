#!/usr/bin/python3

class Book:
    def __init__(self, id, score):
    self.id = id
    self.score = score

class Library:
    def __init__(self, id, books, treg, rate):
    self.id = id
    self.books = []
    self.treg = treg
    self.rate = rate