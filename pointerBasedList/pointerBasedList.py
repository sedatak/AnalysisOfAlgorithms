# -*- coding: cp1254 -*-
class Node:
   def __init__(self, data):        #her düğüm oluşturulurken bir değer ve sonraki düğüme işaretçi ile birlikte oluşturulur.
      self.data = data
      self.next = None

class myPointerBasedList:
    
   def __init__(self):              #başlangıçta head ve tail değerleri eşittir
      self.head = None
      self.tail = None

   def addNode( self, data ):
      new_node = Node(data)

      if self.head == None:         #head boşsa yeni eklenen değeri head yap
         self.head = new_node

      if self.tail != None:         #tail boşsa yeni eklenen değeri tail yap
         self.tail.next = new_node

      self.tail = new_node          #yeni eklenen değeri tail yap

   def removeNode(self, index):
      prev = None
      node = self.head
      i = 0

      while ( node != None ) and ( i < index ):     # node'u prev'e al ve node'a bir sonrakini ata
         prev = node
         node = node.next
         i += 1

      if prev == None:              #prev boşsa head'i çıkar
          self.head = node.next
      else:
         prev.next = node.next

   def printList(self):
      node = self.head

      while node != None:           #node boş olana kadar bir sonraki değeri yazdır
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
