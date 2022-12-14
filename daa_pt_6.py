# -*- coding: utf-8 -*-
"""DAA pt 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TDPQJFWEqwhWpsUpAgqWQeiWQnn7U1iP
"""

Algoritma dynamic dengan fibonacci

#fibonacci dengan while
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto ",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1+n2
        #update nilai
        n1 = n2
        n2 = nth
        count += 1

"""algoritma dynamic
deret fibonacci dengan while
"""

#Fibonacci dengan rekursi

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 20

#cek apakah nilai nterms valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))

"""latihan"""

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Masukkan berapa banyak angkanya:"))

#cek apakah nilai nterms valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))

"""penerapan algoritma greedy pada tsp(travelling salesman/salesperson problem)"""

import random
from itertools import permutations
alltours = permutations

def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i])
        for i in range(len(aTour)))
    
aCity = complex    

def distance_points(first, second):
    return abs(first - second)

def generate_cities (number_of_cities):
    seed=111;width=500;height=300
    random.seed((number_of_cities, seed))
    return frozenset(aCity(random.randint(1, width), random.randint(1,height))
        for c in range(number_of_cities))

"""slide 2"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000: plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD') 
def visualize_segment (segment, style='bo-'):
        plt.plot([x(c) for c in segment], [y(c) for c in segment], style, clip_pn=false)
        plt.axis('scaled')
        plt.axis('off')       

def x(city): "X axis"; return city.real

def y(city): "Y axis"; return city.imag

"""slide 3"""

from time import process_time
from collections import Counter
def tsp(algorithm, cities):
    t0 = process_time()
    tour = algorithm(cities)
    t1 = process_time()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}:{} cities => tour length {:.0f}(in {:.{3f} sec)".format(name(algorithm), len(tour), distance_tour(tour), t1-t0))



def name(algorithm): return algorithm.__name__.replace('_tsp','')

"""slide 4"""

def greedy_algorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour    

def first(collection): return next(iter(collection))

def nearest_neighbor(A, cities):
    return min(cities, key=lambda c: distance_points(c,A))
    tsp(greedy_algorithm, generate_cities(5))

"""penerapan algoritma greedy dengan huffman coding"""

string = 'BCAADDDCCACACAC'

# creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left= left
        self.right= right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

"""slide ke 2"""

# main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))    
    return d

"""slide ke 3"""

# calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1+c2))
    
    nodes = sorted(nodes, key =lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])    

print(' Char | Huffman code ')
print('---------------------')
for (char, frequency) in freq:
     print(' %-4r |%12s' % (char, huffmanCode[char]))