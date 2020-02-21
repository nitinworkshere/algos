class BSTAlgorithms:
    counter = 0

    @staticmethod
    def findKMaxRecursive(root, k):
        global counter

        if root is None:
            return None
        node = findKMaxRecursive(root.right, k)

        if counter is not k:
            counter += 1
            node = root
        if counter == k:
            return node
        else:
            return findKMaxRecursive(root.left, k)

    @staticmethod
    def findKmax(root, k):
        node = findKMaxRecursive(root, k)
        if node is not None:
            return node.data
        return -1

    @staticmethod
    def findheight(root):
        if root is None:
            return 0
        maxheight = max(BSTAlgorithms.findheight(root.left), BSTAlgorithms.findheight(root.right))
        return 1 + maxheight

    @staticmethod
    def findancestor(root, k, arr=[]):
        if root is None:
            return None
        if root.data > k:
            if root.left is not None:
                arr.append(root.data)
                print(root.data)
                BSTAlgorithms.findancestor(root.left, k, arr)
            else:
                return None
        if root.data < k:
            if root.right is not None:
                arr.append(root.data)
                print(root.data)
                BSTAlgorithms.findancestor(root.right, k, arr)
            else:
                return None
        else:
            return root

    @staticmethod
    def recfindacestor(root, k, arr=[]):
        #hint true and false are for search pruning, only path with true to be considered
        if root is None:
            return False
        if root.data == k:
            return True
        lfind = BSTAlgorithms.recfindacestor(root.left, k, arr)
        rfind = BSTAlgorithms.recfindacestor(root.right, k, arr)
        if rfind or lfind:
            arr.append(root.data)
            return True
        return False

    @staticmethod
    def recnodeatkdistance(root, k, level=1, arr=[]):
        if root is None:
            return False
        if level == k:
            arr.append(root.data)
            return True
        llevel = BSTAlgorithms.recnodeatkdistance(root.left, k, level+1, arr)
        rlevel = BSTAlgorithms.recnodeatkdistance(root.right, k, level+1, arr)

        if (rlevel or llevel) and level == k:
            arr.append(root.data)
            return True
        return False

    @staticmethod
    def simplerrecnodeatkdistance(root, level, arr=[]):
        if root is None:
            return
        if k == 0:
            arr.append(root.data)
        else:
            BSTAlgorithms.simplerrecnodeatkdistance(root.left, k-1, arr)
            BSTAlgorithms.simplerrecnodeatkdistance(root.right, k-1, arr)











