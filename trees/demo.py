from TreeNode import TreeNode

root = TreeNode("Nilupul", "CEO")
chinmay = TreeNode("Chinmay", "CTO")
root.add_child(chinmay)
gels = TreeNode("Gels", "HR Head")
root.add_child(gels)
dhaval = TreeNode("Dhaval", "Cloud Manager")
abhijit = TreeNode("Abhijit", "App Manager")
gels.add_child(dhaval)
gels.add_child(abhijit)

root.print_tree("name", 0)
root.print_tree("designation", 1)
root.print_tree("both", 2)
print(root.calc_nodes())
