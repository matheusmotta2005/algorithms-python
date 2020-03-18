from sorting.bubble import Bubble
from sorting.insert import Insert
from sorting.merge import Merge
from sorting.quick import Quick

def bubble(input):
    Bubble(input).sort()

def insert(input):
    Insert(input).sort()

def merge(input):
    Merge(input).sort()

def quick(input):
    Quick(input).sort()