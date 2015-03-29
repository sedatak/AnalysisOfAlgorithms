# -*- coding: cp1254 -*-
class Node:
   def __init__(self, data):        #her d���m olu�turulurken bir de�er ve sonraki d���me i�aret�i ile birlikte olu�turulur.
      self.data = data
      self.next = None

class myPointerBasedList:
    
   def __init__(self):              #ba�lang��ta head ve tail de�erleri e�ittir
      self.head = None
      self.tail = None

   def addNode( self, data ):
      new_node = Node(data)

      if self.head == None:         #head bo�sa yeni eklenen de�eri head yap
         self.head = new_node

      if self.tail != None:         #tail bo�sa yeni eklenen de�eri tail yap
         self.tail.next = new_node

      self.tail = new_node          #yeni eklenen de�eri tail yap

   def removeNode(self, index):
      prev = None
      node = self.head
      i = 0

      while ( node != None ) and ( i < index ):     # node'u prev'e al ve node'a bir sonrakini ata
         prev = node
         node = node.next
         i += 1

      if prev == None:              #prev bo�sa head'i ��kar
          self.head = node.next
      else:
         prev.next = node.next

   def printList(self):
      node = self.head

      while node != None:           #node bo� olana kadar bir sonraki de�eri yazd�r
         print node.data
         node = node.next


pointerBasedList = myPointerBasedList()

pointerBasedList.addNode(1254)
pointerBasedList.addNode(5421)
pointerBasedList.addNode(8965)
pointerBasedList.addNode(5487)

pointerBasedList.printList()

pointerBasedList.removeNode(2)

pointerBasedList.printList()
