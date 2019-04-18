

node_0 = SimpleTreeNode(0, None)
node_1 = SimpleTreeNode(1, None)
node_2 = SimpleTreeNode(2, None)
node_3 = SimpleTreeNode(3, None)
node_4 = SimpleTreeNode(4, None)
node_5 = SimpleTreeNode(5, None)
node_6 = SimpleTreeNode(6, None)
node_7 = SimpleTreeNode(7, None)
node_8 = SimpleTreeNode(8, None)


tree = SimpleTree(node_0)

tree.AddChild(node_0, node_1)
tree.AddChild(node_1, node_2)
# tree.AddChild(node_1, node_3)
tree.AddChild(node_2, node_4)
# tree.AddChild(node_2, node_5)
# tree.AddChild(node_2, node_6)
# tree.AddChild(node_3, node_7)

print(tree.GetAllNodes())

for i in tree.GetAllNodes():
    print(i.NodeValue)

tree.MoveNode(node_2, node_0)
tree.MoveNode(node_1, node_4)
# tree.MoveNode(node_1, node_3)
#
# # tree.DeleteNode(node_1)
# # tree.DeleteNode(node_2)
# # tree.DeleteNode(node_3)
#
# # print(tree.GetAllNodes())
# # print("node 1 parent", node_1.Parent)
print("tree count",tree.Count())
# print("root children", tree.Root.Children)
print("LeafCount", tree.LeafCount())
print("root parent", tree.Root.Parent)
# # print("root parent", node_7.Parent)
#
# # print(node_1.Parent.NodeValue)
#
# print(tree.GetAllNodes())
# print(tree.GetAllNodes())
# print(tree.GetAllNodes())
# print(tree.GetAllNodes())
# print(tree.GetAllNodes())
for i in tree.GetAllNodes():
    print(i.NodeValue)