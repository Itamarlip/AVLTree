from AVLTree import AVLTree, AVLNode
import  random
"""
T = AVLTree()

for i in range(1,13):
    T.insert(i,str(i))
T.delete(T.search(9))
print(T.delete(T.search(11)))
"""




def create_tree(values, random_order=False):
    if random_order:
        random.shuffle(values)
    tree = AVLTree()
    for val in values:
        print(val)
        tree.insert(val, str(val))
    return tree


"""lst = [i for i in range(1,1000)]
copy = []
for i in range(1000):
    copy.append((i, str(i)))
random.shuffle(lst)
print("here 12")

T = create_tree(lst)

print("here 1")

print(lst == T.avl_to_array())"""




def display(self):
    lines, *_ = display_aux(self)
    for line in lines:
        print(line)


def display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if not self.right.is_real_node() and not self.left.is_real_node():
        line = '%s' % self.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if not self.right.is_real_node():
        lines, n, p, x = display_aux(self.left)
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if not self.left.is_real_node():
        lines, n, p, x = display_aux(self.right)
        s = '%s' % self.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display_aux(self.left)
    right, m, q, y = display_aux(self.right)
    s = '%s' % self.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


tree = AVLTree()
values = lst = [383,39,1187,751,557]
for val in values:
    tree.insert(val, str(val))
    print(tree.rank(tree.search(val)))

print("W")
display(tree.get_root())
print(tree.max_range(111110,10010101).key)
