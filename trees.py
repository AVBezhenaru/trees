class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root;  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        pass  # ваш код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete == self.Root:
            return

        NodeToDelete.Parent.Children.remove(NodeToDelete)


    def GetAllNodes(self, allNodes = None):

        if allNodes is None:
            allNodes = []

        node = self.Root

        if node.Parent == None and len(allNodes) ==  0:
            allNodes.append(node)

        for child in node.Children:
            allNodes.append(child)
            self.Root = child
            self.GetAllNodes(allNodes)

        self.Root = allNodes[0]
        result = allNodes
        allNodes = None
        return result

    def FindNodesByValue(self, val):
        FindNodesList = []

        for i in self.GetAllNodes():
            if i.NodeValue == val:
                FindNodesList.append(i)

        return FindNodesList

    def MoveNode(self, OriginalNode, NewParent):
        NewParent.Children.append(OriginalNode)
        self.DeleteNode(OriginalNode)

    def Count(self):
        count = len(self.GetAllNodes())

        return count

    def LeafCount(self):
        count = 0

        for child in self.GetAllNodes():
            if not child.Children:
                count += 1

        return count