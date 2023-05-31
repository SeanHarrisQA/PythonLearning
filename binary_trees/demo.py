from BinaryTreeNode import BinaryTreeNode 

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = build_tree(countries)

print("UK is in the list? ", country_tree.search("UK"))
print("Sweden is in the list? ", country_tree.search("Sweden"))

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
print(numbers_tree.find_min())
print(country_tree.find_max())
print(numbers_tree.calculate_sum())
print(numbers_tree.post_order_traversal())
print(numbers_tree.pre_order_traversal())

numbers = [15,12,7,14,27,20,23,88]

numbers_tree = build_tree(numbers)
print("Input numbers:",numbers)
print("Min:",numbers_tree.find_min())
print("Max:",numbers_tree.find_max())
print("Sum:", numbers_tree.calculate_sum())
print("In order traversal:", numbers_tree.in_order_traversal())
print("Pre order traversal:", numbers_tree.pre_order_traversal())
print("Post order traversal:", numbers_tree.post_order_traversal())

print("22222222222222222222222222222222222222")

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
numbers_tree.delete(20)
print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
print(numbers_tree.size())

numbers_tree.delete(9)
print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]
print(numbers_tree.size())

numbers_tree.delete(17)
print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]
print(numbers_tree.size())