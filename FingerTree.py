# username - complete info
# id1      - 331777987
# name1    - Itamar Lipkin
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

        if (key != None):
            self.left = AVLNode(None, None)
            self.right = AVLNode(None, None)
            self.height = 0
            self.size = 1

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.value != None

    def get_balance_factor(self):
        return self.left.height - self.right.height

    def return_updated_height(self):
        return 1 + max(self.left.height, self.right.height)

    def update_size(self):
        self.size = self.left.size + self.right.size + 1

    def successor(self):  # only used if self has 2 children
        current_node = self.right
        while current_node.left.is_real_node():
            current_node = current_node.left
        return current_node


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = AVLNode(None, None)
        self.finger = AVLNode(None, None)

    """searches for a node in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: node corresponding to key
    """

    def search(self, key):
        curr_node = self.root
        while curr_node.key != None:
            if key == curr_node.key:
                return curr_node
            elif key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None

    """inserts a new node into the dictionary with corresponding key and value

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        node_to_add = AVLNode(key, val)
        save_parent = None
        if not self.root.is_real_node():
            self.root = node_to_add
            self.root.parent = AVLNode(None, None)
            self.finger = node_to_add
            return (0, 0)
        else:
            search_cost = 0
            curr_node = self.finger
        #finding from where to start searching normally

            while curr_node.key != None and key < curr_node.key:
                search_cost+=1
                curr_node = curr_node.parent
            search_cost-=1
            if (curr_node.key == None):
                curr_node = self.root
            else:
                if(self.finger != curr_node):
                    curr_node = curr_node.right
            if (key > self.finger.key):
                self.finger = node_to_add

        # inserting to a BST as usual


        #making sure max stays right




        while curr_node.is_real_node():
            save_parent = curr_node
            if key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
            search_cost+=1

        node_to_add.parent = save_parent

        if save_parent == None:
            self.root = node_to_add
            self.root.size += 1

        elif key < save_parent.key:
            save_parent.left = node_to_add
        else:
            save_parent.right = node_to_add
        #search_cost += 1
        bf = 0
        num_of_balances = 0

        while save_parent != None and save_parent.is_real_node():  # going up in the tree until it is balanced or performed a rotation

            bf = save_parent.get_balance_factor()

            if abs(bf) < 2 and save_parent.height == save_parent.return_updated_height():
                save_parent.update_size()
                save_parent = save_parent.parent

            elif abs(bf) < 2:
                save_parent.height = save_parent.return_updated_height()
                num_of_balances += 1
                save_parent.update_size()
                save_parent = save_parent.parent

            else:
                if bf == -2:
                    if save_parent.right.is_real_node() and save_parent.right.get_balance_factor() == -1:
                        self.left_rotation(save_parent)
                        num_of_balances += 1
                    else:
                        self.right_left_rotation(save_parent)
                        num_of_balances += 2
                elif bf == 2:
                    if save_parent.left.is_real_node() and save_parent.left.get_balance_factor() == -1:
                        self.left_right_rotation(save_parent)
                        num_of_balances += 2
                    else:
                        self.right_rotation(save_parent)
                        num_of_balances += 1
                save_parent = save_parent.parent

        return (num_of_balances + search_cost , self.root.size - self.rank(node_to_add))

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        # bst delete
        if (node.right.key == None and node.left.key == None):
            save_parent = node.parent
            if (self.root == node):
                self.root = AVLNode(None, None)
            if (node.parent.key > node.key):
                node.parent.left = AVLNode(None, None)
            else:
                node.parent.right = AVLNode(None, None)
        if (node.right.key == None):
            save_parent = node.parent
            if (self.root == node):
                self.root = node.left
                node.left.parent = AVLNode(None, None)
            if (node.parent.key > node.key):
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
        if (node.left.key == None):
            save_parent = node.parent
            if (self.root == node):
                self.root = node.right
                node.right.parent = AVLNode(None, None)
            if (node.parent.key > node.key):
                node.parent.left = node.right
                node.right.parent = node.parent
            else:
                node.parent.right = node.right
                node.right.parent = node.parent
        successor = node.successor()
        save_parent = successor.parent
        # remove successor
        successor.parent.left = successor.right
        if (successor.right.is_real_node()):
            successor.right.parent = successor.parent

        # replace node with successor
        if (self.root == node):
            self.root = successor
        else:
            if (node.parent.key > node.key):
                node.parent.left = successor
            else:
                node.parent.right = successor
        successor.parent = node.parent
        successor.right = node.right
        node.right.parent = successor
        successor.left = node.left
        node.left.parent = successor

        # update information for avl and rotations
        bf = 0
        num_of_balances = 0

        while save_parent != None and save_parent.is_real_node():  # going up in the tree until it is balanced

            bf = save_parent.get_balance_factor()

            if abs(bf) < 2 and save_parent.height == save_parent.return_updated_height():
                save_parent.update_size()
                save_parent = save_parent.parent

            elif abs(bf) < 2:
                save_parent.height = save_parent.return_updated_height()
                num_of_balances += 1
                save_parent.update_size()
                save_parent = save_parent.parent

            else:
                if bf == -2:
                    if save_parent.right.get_balance_factor() == 1:
                        self.right_left_rotation(save_parent)
                        num_of_balances += 2
                    else:
                        self.left_rotation(save_parent)
                        num_of_balances += 1
                elif bf == 2:
                    if save_parent.left.get_balance_factor() == -1:
                        self.left_right_rotation(save_parent)
                        num_of_balances += 2
                    else:
                        self.right_rotation(save_parent)
                        num_of_balances += 1
                save_parent = save_parent.parent

        return num_of_balances

    """all the rotations necessary to use in insert/delete"""

    def right_rotation(self, problem_node):
        # perform pointers change
        left_node = problem_node.left
        left_node.parent = problem_node.parent
        problem_node.parent = left_node
        problem_node.left = left_node.right
        left_node.right.parent = problem_node
        left_node.right = problem_node

        if (self.root == problem_node):
            self.root = left_node

        if (left_node.parent.is_real_node()):
            if (left_node.key > left_node.parent.key):
                left_node.parent.right = left_node
            else:
                left_node.parent.left = left_node

        # update heights
        left_node.right.height = left_node.right.return_updated_height()
        left_node.left.height = left_node.left.return_updated_height()
        left_node.height = left_node.return_updated_height()

        # update sizes
        left_node.right.update_size()
        left_node.left.update_size()
        left_node.update_size()

    def left_rotation(self, problem_node):
        # perform pointers change
        right_node = problem_node.right
        right_node.parent = problem_node.parent
        problem_node.parent = right_node
        problem_node.right = right_node.left
        right_node.left.parent = problem_node
        right_node.left = problem_node

        if (self.root == problem_node):
            self.root = right_node

        if (right_node.parent.is_real_node()):
            if (right_node.key > right_node.parent.key):
                right_node.parent.right = right_node
            else:
                right_node.parent.left = right_node

        # update heights
        right_node.right.height = right_node.right.return_updated_height()
        right_node.left.height = right_node.left.return_updated_height()
        right_node.height = right_node.return_updated_height()

        # update sizes
        right_node.right.update_size()
        right_node.left.update_size()
        right_node.update_size()

    def left_right_rotation(self, problem_node):
        # perform pointers change
        left_node = problem_node.left
        left_right_node = left_node.right

        left_right_node.parent = problem_node.parent
        problem_node.parent = left_right_node
        problem_node.left = left_right_node.right
        left_right_node.right.parent = problem_node
        left_right_node.right = problem_node
        left_node.parent = left_right_node
        left_node.right = left_right_node.left
        left_right_node.left.parent = left_node
        left_right_node.left = left_node

        if (self.root == problem_node):
            self.root = left_right_node

        if (left_right_node.parent.is_real_node()):
            if (left_right_node.key > left_right_node.parent.key):
                left_right_node.parent.right = left_right_node
            else:
                left_right_node.parent.left = left_right_node

        # update heights
        left_right_node.right.height = left_right_node.right.return_updated_height()
        left_right_node.left.height = left_right_node.left.return_updated_height()
        left_right_node.height = left_right_node.return_updated_height()

        # update sizes
        left_right_node.right.update_size()
        left_right_node.left.update_size()
        left_right_node.update_size()

    def right_left_rotation(self, problem_node):
        right_node = problem_node.right
        right_left_node = right_node.left

        right_left_node.parent = problem_node.parent
        problem_node.parent = right_left_node
        problem_node.right = right_left_node.left
        right_left_node.left.parent = problem_node
        right_left_node.left = problem_node
        right_node.parent = right_left_node
        right_node.left = right_left_node.right
        right_left_node.right.parent = right_node
        right_left_node.right = right_node

        if (self.root == problem_node):
            self.root = right_left_node

        if (right_left_node.parent.is_real_node()):
            if (right_left_node.key > right_left_node.parent.key):
                right_left_node.parent.right = right_left_node
            else:
                right_left_node.parent.left = right_left_node

        # update heights
        right_left_node.right.height = right_left_node.right.return_updated_height()
        right_left_node.left.height = right_left_node.left.return_updated_height()
        right_left_node.height = right_left_node.return_updated_height()

        # update sizes
        right_left_node.right.update_size()
        right_left_node.left.update_size()
        right_left_node.update_size()

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        return None
        root = self.root
        if root.key == None:
            return []
        list_ret = [(root.key, root.value)]
        left_list = []
        right_list = []
        left_list = self.to_arr_rec(root.left)
        right_list = self.to_arr_rec(root.right)
        return left_list + list_ret + right_list

    def to_arr_rec(self, node):
        if node.value == None:
            return []
        list_ret = [(node.key, node.value)]
        left_list = []
        right_list = []
        left_list = self.to_arr_rec(node.left)
        right_list = self.to_arr_rec(node.right)
        return left_list + list_ret + right_list

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return self.root.size

    """compute the rank of node in the dictionary

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary to compute the rank for
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node):
        left_size = node.left.size + 1
        cuur_node = node

        while (cuur_node.is_real_node()):
            if cuur_node == cuur_node.parent.right:
                left_size += cuur_node.parent.left.size + 1
            cuur_node = cuur_node.parent

        return left_size

    """finds the i'th smallest item (according to keys) in the dictionary

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: AVLNode
    @returns: the node of rank i in self
    """

    def rec_select(self, node, i):
        left_size = node.left.size + 1

        if (left_size == i):
            return node
        if (left_size > i):
            return self.rec_select(node.left, i)

        return self.rec_select(node.right, i - left_size)

    def select(self, i):
        return self.rec_select(self.root, i)

    """finds the node with the largest value in a specified range of keys

    @type a: int
    @param a: the lower end of the range
    @type b: int
    @param b: the upper end of the range
    @pre: a<b
    @rtype: AVLNode
    @returns: the node with maximal (lexicographically) value having a<=key<=b, or None if no such keys exist
    """

    def max_range(self, a, b):
        root = self.root
        if (root == None):
            return None

        if (root.key < a):
            return self.rec_max_range(root.right, a, b)
        if (root.key > b):
            return self.rec_max_range(root.left, a, b)
        if (root.key == a):
            return self.max_lex(root, self.rec_max_range(root.right, a, b))
        if (root.key == b):
            return self.max_lex(root, self.rec_max_range(root.left, a, b))

        return self.max_lex(root,
                            self.max_lex(self.rec_max_range(root.right, a, b), self.rec_max_range(root.left, a, b)))

    def rec_max_range(self, node, a, b):
        if (node.value == None):
            return node

        if (node.key < a):
            return self.rec_max_range(node.right, a, b)
        if (node.key > b):
            return self.rec_max_range(node.left, a, b)
        if (node.key == a):
            return self.max_lex(node, self.rec_max_range(node.right, a, b))
        if (node.key == b):
            return self.max_lex(node, self.rec_max_range(node.left, a, b))

        return self.max_lex(node,
                            self.max_lex(self.rec_max_range(node.right, a, b), self.rec_max_range(node.left, a, b)))

    def max_lex(self, node1, node2):
        if (node1.value == None):
            return node2
        if (node2.value == None):
            return node1

        char_list1 = [char for char in node1.value]
        char_list2 = [char for char in node2.value]

        for i in range(0, min(len(char_list1), len(char_list2))):
            if (char_list1[i] > char_list2[i]):
                return node1
            if (char_list1[i] < char_list2[i]):
                return node2

        if (len(char_list1) > len(char_list2)):
            return node1
        return node2

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root

