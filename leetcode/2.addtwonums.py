# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def convert_to_number(l1):
    sum = l1.val
    power = 0
    while l1.next:
        power = power + 1
        l1 = l1.next
        sum = sum + l1.val * (10 ** power)
    return sum

class Solution:
    def addTwoNumbers(self, l1, l2):
        first_num = convert_to_number(l1)
        second_num = convert_to_number(l2)
        reversed_str = str(first_num + second_num)[::-1]
        l = ListNode(int(reversed_str[0]))
        start_list_node = l
        for i in range(len(reversed_str)):
            if i != len(reversed_str)-1:
                j = ListNode(int(reversed_str[i+1]))
                l.next = j
                l = j
            else:
                l.next = None
        return start_list_node


ge = ListNode(3)
# shi = ListNode(2)
# bai = ListNode(5)
# ge.next = shi
# shi.next = bai

ge2 = ListNode(1)
shi2 = ListNode(0)
bai2 = ListNode(5)
qian2 = ListNode(9)
ge2.next = shi2
shi2.next = bai2
bai2.next = qian2


print(convert_to_number(ge))
print(convert_to_number(ge2))
s = Solution()
node = s.addTwoNumbers(ge,ge2)
print(convert_to_number(node))


class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str_l1, str_l2 = '', ''
        while l1:
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2:
            str_l2 += str(l2.val)
            l2 = l2.next
        int_l1 = int(str_l1[::-1])
        int_l2 = int(str_l2[::-1])
        return list(map(int, str(int_l1 + int_l2)[::-1]))


s2 = Solution2()
print(s2.addTwoNumbers(ge,ge2))
