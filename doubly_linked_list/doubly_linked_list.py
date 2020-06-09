"""Each ListNode holds a reference to its p_nodeious node
as well as its n_node node in the List."""
class ListNode:
    def __init__(self, value, p_node=None, n_node=None):
        self.value = value
        self.p_node = p_node
        self.n_node = n_node

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a n_node node it is point to."""
    def insert_after(self, value):
        current_n_node = self.n_node
        self.n_node = ListNode(value, self, current_n_node)
        if current_n_node:
            current_n_node.p_node = self.n_node

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a p_nodeious node it is point to."""
    def insert_before(self, value):
        current_p_node = self.p_node
        self.p_node = ListNode(value, current_p_node, self)
        if current_p_node:
            current_p_node.n_node = self.p_node

    """Rearranges this ListNode's p_nodeious and n_node pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.p_node:
            self.p_node.n_node = self.n_node
        if self.n_node:
            self.n_node.p_node = self.p_node


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
    the old head node's p_nodeious pointer accordingly."""
        # create a new node
        new_node = ListNode(value, None, None)
        # check if the DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.n_node = self.head
            self.head.p_node = new_node
            slef.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's n_node node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        pass

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's n_node pointer accordingly."""
    def add_to_tail(self, value):
        pass

    """Removes the List's current tail node, making the 
    current tail's p_nodeious node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
