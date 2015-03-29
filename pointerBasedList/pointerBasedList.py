# -*- coding: cp1254 -*-
class Node:
   def __init__(self, data):        #her dugum olusturulurken bir deger ve sonraki dugume isaretci ile birlikte olusturulur
      self.data = data
      self.next = None

class myPointerBasedList:
    
   def __init__(self):              #baslangıcta head ve tail degerleri esittir
      self.head = None
      self.tail = None

   def addNode( self, data ):
      new_node = Node(data)

      if self.head == None:         #head bossa yeni eklenen degeri head yap
         self.head = new_node

      if self.tail != None:         #tail bossa yeni eklenen degeri tail yap
         self.tail.next = new_node

      self.tail = new_node          #yeni eklenen degeri tail yap

   def removeNode(self, index):
      prev = None
      node = self.head
      i = 0

      while ( node != None ) and ( i < index ):     # node'u prev'e al ve node'a bir sonrakini ata
         prev = node
         node = node.next
         i += 1

      if prev == None:              #prev bossa head'i cikar
          self.head = node.next
      else:
         prev.next = node.next

   def printList(self):
      node = self.head

      while node != None:           #node boş olana kadar bir sonraki degeri yazdir
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
