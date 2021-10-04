class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.no_of_nodes = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    def append(self, value):
        self.no_of_nodes +=1
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def delete(self, value):
        node = self.head
        prev = None
        if self.head.value == value:
            next = self.head.next
            self.head = self.head.next
            self.no_of_nodes -=1
            node = next
        while node:
            next = node.next
            if node.value == value:
                prev.next = node.next
                self.no_of_nodes -=1
            else:
                prev = node
            node = next
        return
    def size(self):
        return self.no_of_nodes

#  Since problem is not clear about How to handle duplicates
#  following solution of Union and intersection is with Duplicates
def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None and llist_2 == None:
        return None
    if llist_1 ==  None:
        return llist_2
    if llist_2 ==  None:
        return llist_1
    keys_set = set()
    result_list = LinkedList()
    curr = llist_1.head
    while curr:
        keys_set.add(curr.value)
        result_list.append(curr.value)
        curr = curr.next
    
    curr_2 = llist_2.head
    while curr_2:
        if not curr_2.value in keys_set:
            result_list.append(curr_2.value)
        curr_2 = curr_2.next
    return result_list.__str__()
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        return None
    keys_set = set()
    result_list = LinkedList()
    curr = llist_1.head
    while curr:
        keys_set.add(curr.value)
        curr = curr.next
    curr_2 = llist_2.head
    while curr_2:
        if curr_2.value in keys_set:
            result_list.append(curr_2.value)
        curr_2 = curr_2.next
    return result_list.__str__()
    pass

#  Since problem is not clear about How to handle duplicates
#  following solution of Union and intersection is without Duplicates
def union_without_duplicates(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None and llist_2 == None:
        return None
    if llist_1 ==  None:
        return llist_2
    if llist_2 ==  None:
        return llist_1
    keys_set = set()
    result_list = LinkedList()
    curr = llist_1.head
    while curr:
        keys_set.add(curr.value)
        curr = curr.next
    curr_2 = llist_2.head
    while curr_2:
        keys_set.add(curr_2.value)
        curr_2 = curr_2.next
    for key_code in keys_set:
        result_list.append(key_code)
    return result_list.__str__()
    pass

def intersection_without_duplicates(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        return None
    keys_map = dict()
    result_list = LinkedList()
    curr = llist_1.head
    while curr:
        keys_map[curr.value] = 1
        curr = curr.next
    curr_2 = llist_2.head
    while curr_2:
        if curr_2.value in keys_map:
            keys_map[curr_2.value] = 0 
        curr_2 = curr_2.next
    for key in keys_map:
        if keys_map[key] == 0:
            result_list.append(key)
    return result_list.__str__()
    pass

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# Edge cases
ll_emmpty_1 = LinkedList()
ll_emmpty_2 = LinkedList()

print (union(linked_list_1,None))
print (union(linked_list_1,ll_emmpty_2))
print (union(None,linked_list_2))
print (union(ll_emmpty_1,linked_list_2))
print (intersection(None,None))
print (union(ll_emmpty_1,ll_emmpty_2))
print (intersection(linked_list_1,None))
print (intersection(linked_list_1,ll_emmpty_2))
print (intersection(ll_emmpty_2,linked_list_2))


print (union_without_duplicates(linked_list_1,linked_list_2))
print (intersection_without_duplicates(linked_list_1,linked_list_2))


print (union_without_duplicates(ll_emmpty_1,ll_emmpty_2))
print (union_without_duplicates(linked_list_1,ll_emmpty_2))
print (union_without_duplicates(ll_emmpty_1,linked_list_2))
print (union_without_duplicates(None,None))
print (union_without_duplicates(linked_list_1,None))
print (union_without_duplicates(None,linked_list_2))
print (intersection_without_duplicates(None,None))
print (intersection_without_duplicates(linked_list_1,None))
print (intersection_without_duplicates(None,linked_list_2))


# this is for Mutating input linked list without using extra space for result
#  This is to mutate list 1 and append to list 2 No extra space for result

def union_without_extraspace(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None and llist_2 == None:
        return None
    if llist_1 ==  None:
        return llist_2
    if llist_2 ==  None:
        return llist_1
    keys_set = set()
 
    curr = llist_1.head
    prev = None
    while curr:
        keys_set.add(curr.value)
        prev = curr
        curr = curr.next
    
    curr2 = llist_2.head
    while curr2:
        curr2_next = curr2.next
        if curr2.value in keys_set:
            llist_2.delete(curr2.value)
        curr2 = curr2_next
    if llist_2.head !=None and prev:
        # After removing common nodes on llist2. Set llist1 last element next to l2 head
        prev.next = llist_2.head
    return llist_1.__str__()
    pass

#  This is to mutate list 2 and remove non common elements and return list2 for intersections
def intersection_without_extraspace(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        return None
    keys_set = set()
 
    curr = llist_1.head
    while curr:
        keys_set.add(curr.value)
        curr = curr.next
    curr2 = llist_2.head
    while curr2:
        curr2_next = curr2.next
        if not curr2.value in keys_set:
            llist_2.delete(curr2.value)
        curr2 = curr2_next

    return llist_2.__str__()
    pass

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
for i in element_1:
    linked_list_3.append(i)
    linked_list_5.append(i)

for i in element_2:
    linked_list_4.append(i)
    linked_list_6.append(i)

print (union_without_extraspace(linked_list_3,linked_list_4))
print (intersection_without_extraspace(linked_list_5,linked_list_6))

print (union_without_extraspace(None,None))
print (union_without_extraspace(linked_list_1,None))
print (union_without_extraspace(None,linked_list_2))
print (intersection_without_extraspace(None,None))
print (intersection_without_extraspace(linked_list_1,None))
print (intersection_without_extraspace(None,linked_list_2))

print (union_without_extraspace(ll_emmpty_1,ll_emmpty_2))
print (union_without_extraspace(linked_list_1,ll_emmpty_2))
print (union_without_extraspace(ll_emmpty_1,linked_list_2))
print (intersection_without_extraspace(ll_emmpty_1,ll_emmpty_2))
print (intersection_without_extraspace(linked_list_1,ll_emmpty_2))
print (intersection_without_extraspace(ll_emmpty_1,linked_list_2))