#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# linkedlist 的一些简单操作


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = self.getNumberFromList(l1)
        num2 = self.getNumberFromList(l2)
        num3 = num1 + num2
        return self.setNumberListNode(num3)

    def getNumberFromList(self, l):
        num = 0
        times = 0
        while l is not None:
            num = num + l.value * 10**times
            l = l.next
            times += 1
        return num

    def setNumberListNode(self, num):
        b = num % 10
        start = ListNode(b)
        node = start
        num = num // 10
        while num > 0:
            b = num % 10
            temp = ListNode(b)
            node.next = temp
            node = node.next
            num = num // 10
        return start
