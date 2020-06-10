"""Each ListNode holds a reference to its prv node
as well as its nxt node in the List."""
class ListNode:
    def __init__(self, value, prv=None, nxt=None):
        self.value = value
        self.prv = prv
        self.nxt = nxt

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a nxt node it is point to."""
    def insert_after(self, value):
        current_nxt = self.nxt
        self.nxt = ListNode(value, self, current_nxt)
        if current_nxt:
            current_nxt.prv = self.nxt

        return self.nxt

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a prv node it is point to."""
    def insert_before(self, value):
        current_prv = self.prv
        self.prv = ListNode(value, current_prv, self)
        if current_prv:
            current_prv.nxt = self.prv

        return self.prv

    """Rearranges this ListNode's prv and nxt pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prv:
            self.prv.nxt = self.nxt
        if self.nxt:
            self.nxt.prv = self.prv


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's prv pointer accordingly."""
        if self.head:
            new_head = self.head.insert_before(value)
            self.head = new_head
            self.length += 1
        else:
            # if tail exists and has no previous link
            if self.tail and not self.tail.prv:
                self.head = ListNode(value)
                self.tail.prv = self.head
                self.head.nxt = self.tail
                self.length += 1
            else:
                self.head = ListNode(value)
                self.tail = self.head
                self.length += 1


    """Removes the List's current head node, making the
    current head's nxt node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            if self.head.nxt and self.head.nxt is not self.tail:
                new_head = self.head.nxt
                new_head.prv = None
                removed_value = self.head.value
                self.head = new_head
                self.length -= 1

                return removed_value

            elif self.head.nxt and self.head.nxt is self.tail:
                removed_value = self.head.value
                self.head = self.tail
                self.length -= 1

                return removed_value

            else:
                removed_value = self.head.value
                self.head = None
                self.tail = None
                self.length -= 1
                
                return removed_value
        else:
            print("Non-existent Head")

            return None



    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's nxt pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail:
            new_tail = self.tail.insert_after(value)
            self.tail = new_tail
            self.length += 1
        else:
            if not self.tail:
                self.tail = ListNode(value)
                self.head = self.tail
                self.length += 1
            else:
                self.tail = ListNode(value)
                self.length += 1



    """Removes the List's current tail node, making the 
    current tail's prv node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail:
            removed_value = self.tail.value
            if self.tail.prv is self.head:
                self.tail = None
                self.length -= 1

                return removed_value
            elif self.tail.prv is None and self.head:
                self.tail = None
                self.head = None
                self.length -= 1

                return removed_value
            else:
                new_tail = self.tail.prv
                self.tail = new_tail
                self.length -= 1

                return removed_value
        else:
            print("Non-existent Tail")

            return None


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node.delete()
        node.prv = None
        node.nxt = self.head
        self.head.prv = node
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.head and self.tail.prv is self.head:
            self.head, self.tail = self.tail, self.head 
            self.tail.nxt = None
            self.head.nxt = self.tail
            self.tail.prv = self.head
            self.head.prv = None 
        else:
            node.delete()
            node.nxt = None
            node.prv = self.tail
            self.tail.nxt = node
            self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value
        current = self.head.nxt

        while current:
            if current.value > max_value:
                max_value = current.value

            current = current.nxt
        return max_value
