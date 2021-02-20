#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if head is None:
        head.data = data
        head.prev = None
    elif head.next is None:
        if head.data < data:
            head.next = node
            node.prev = head
            node.next = None
        else:
            head.prev = node
            node.next = head
            head = node
            node.prev = None
    else:
        temp = head
        while temp is not None:
            if temp.data > data and temp == head:
                head = node
                head.next = temp
                temp = temp.next
                return head
            elif temp.data > data:
                node.prev = temp.prev
                temp.prev.next = node
                temp.prev = node
                node.next = temp
                return head
            elif temp.data < data and temp.next is None:
                temp.next = node
                node.prev = temp
                return head
            else:
                temp = temp.next
    return head


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
