#coding:utf-8
#用前序遍历和中序遍历结果构建二叉树，遍历结果中不包含重复值
def construct_tree(preorder=None,inorder=None):
    '''
    构建二叉树
    '''
    if not preorder or not inorder:
        return None

    index=inorder.index(preorder[0])
    left=inorder[0:index]
    right=inorder[index+1:]
    root=TreeNode(preorder[0])
    root.left=construct_tree(preorder[1:1+len(left),left])
    root.right=construct_tree(preorder[-len(right):],right)
    return root

#看不懂
