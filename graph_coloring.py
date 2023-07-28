import copy
import random
import time
import turtle
import numpy as np
from math import *
from numpy.polynomial import Polynomial as P

#make sure all edges are [m, n] with m < n to prevent repeats
class Graph:
  def __init__(self, v, e):
    self.vertices = v
    self.edges = e
  def setedges(self, e):
    self.edges = e
  def setvertices(self, v):
    self.vertices = v
  def numvertices(self):
    return len(self.vertices)
  def numedges(self):
    return len(self.edges)
  def v(self):
    return self.vertices
  def e(self):
    return self.edges
  def deletion(self, edge):
    #returns copy with edge deleted
    f = copy.copy(self)
    #deletes an edge
    e = copy.copy(self.edges)
    e.remove(edge)
    f.setedges(e)
    return f
  def contraction(self, edge):
    #returns copy with edge contracted
    f = copy.copy(self)
    #contracts the edge
    i = edge[0]
    j = edge[1]
    e = copy.copy(self.edges)
    v1 = copy.copy(self.vertices)
    e1 = []
    #new edges and vertices
    v1.remove(j)
    #they metabolize into i
    for m in e:
      if j not in m and m not in e1:
        e1.append(m)
      if j in m and i not in m:
        if j == m[0] and [min(i,m[1]), max(i, m[1])] not in e1:
          e1.append([min(i,m[1]), max(i, m[1])])
        elif j == m[1] and [min(m[0],i), max(m[0],i)] not in e1:
          e1.append([min(m[0],i), max(m[0],i)])
    f.setedges(e1)
    f.setvertices(v1)
    return f

s = time.time()
var = 0

def draw(g):
  t = turtle.Turtle()
  t.speed(0)
  size = len(g.v())
  turtle.setup(1000, 1000)
  w = turtle.Screen()
  coords = [[400*cos(2*pi*i/size), 400*sin(2*pi*i/size)] for i in range(size)]
  for j in range(size):
    t.penup()
    t.setpos(coords[j])
    t.dot()
    t.pendown()
  for k in range(0, len(g.e())):
    t.penup()
    t.setpos(coords[g.e()[k][0]-1][0], coords[g.e()[k][0]-1][1])
    t.pendown()
    t.goto(coords[g.e()[k][1]-1][0], coords[g.e()[k][1]-1][1])
    t.penup()
        
  
def chrompoly(g):
  global var
  var += 1
  if var % 100 == 0:
    print(str(var) + " operations completed.")
  #compute the chromatic polynomial of a graph, g.
  if g.numedges() == 0:
    p = P([0, 1])
    for j in range(g.numvertices()-1):
      p = [0,1]*p
    return p
  if g.numedges() == 1:
    p = P([-1, 1])
    for j in range(g.numvertices()-1):
      p = [0, 1] * p
    return p
  else:
    edge = g.e()[0]
    return (chrompoly(g.deletion(edge)) - chrompoly(g.contraction(edge)))

def chromnum(k):
  #input chrompoly
  num = 1
  while k(num) < 1:
    num += 1
  return num

def graph_generator(v, e):
  #generates a random graph with v vertices and e edges
  vertices = [i for i in range(1, v+1)]
  edges = []
  while len(edges) != e:
    i = random.randint(1, v-1)
    j = random.randint(i+1, v)
    if [i,j] not in edges:
      edges.append([i,j])
  return Graph(vertices, edges)


'''
INPUT
v = number of vertices
e = number of edges
a random graph (h) will be generated with these properties
h will be drawn in a new window, and it's chromatic polynomial & number calculated

'''
v = 8
e = 12
h = graph_generator(v, e)
print("Vertices: " + str(h.v()))
print("Edges: " + str(h.e()))
draw(h)

p = chrompoly(h)
print("The chromatic polynomial of the requested graph is: " + str(p))
print("Yielding chromatic number: " + str(chromnum(p)))
for j in range(chromnum(p), chromnum(p)+5):
    print("With " + str(j) + " colors, there are " + str(int(p(j))) + " ways to color.")
print(str(time.time()-s)[:5] + " seconds elapsed.")


#graph things on the unit circle? Then draw lines







    
  
