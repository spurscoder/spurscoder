---
layout: post
title: "Algorithm"
author: "Spurs"
date: 2018-06-11 13:30:00
tags:
---

> Algorithm

<!-- more -->

###04-13

#### 1. 寻找二叉树的公共父节点。

-  递归解法

```c++
  class Solution {
  public:
      TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
          if(root==NULL || root==p||root==q) return root;
          TreeNode *left = lowestCommonAncestor(root->left, p, q);
          TreeNode *right = lowestCommonAncestor(root->right, p, q);
          if(left && right) return root;
          return left?left:right;
      }
  };
```

- 非递归解法

  ```python
  class Solution(object):
      def lowestCommonAncestor(self, root, p, q):
          """
          :type root: TreeNode
          :type p: TreeNode
          :type q: TreeNode
          :rtype: TreeNode
          """
          stack = [root]
          pair = {root:None}
          while p not in pair or q not in pair:
              node = stack.pop()
              if node.left:
                  stack.append(node.left)
                  pair[node.left] = node
              if node.right:
                  stack.append(node.right)
                  pair[node.right] = node
          #找到到达p的路径
          path = set()
          while p :
              path.add(p)
              p = pair[p]
          while q not in path:
              q = pair[q]
          return q 
  ```

####2.二叉树的中序遍历

- 递归方法

  ```c++
  void inorder(TreeNode *root, vector<int> &path)
  {
      if(root != NULL)
      {
          inorder(root->left, path);
          path.push_back(root->val);
          inorder(root->right, path);
      }
  }
  ```

- 非递归版本

  ```c++
  //非递归中序遍历
  void inorderTraversal(TreeNode *root, vector<int> &path)
  {
      stack<TreeNode *> s;
      TreeNode *p = root;
      while(p != NULL || !s.empty())
      {
          while(p != NULL)
          {
              s.push(p);
              p = p->left;
          }
          if(!s.empty())
          {
              p = s.top();
              path.push_back(p->val);
              s.pop();
              p = p->right;
          }
      }
  }
  ```

#### 3.求两个已排序数组的交集

```c++
public LinkedList<Integer> intersection(int[] A, int[] B) {  
    if (A == null || B == null || A.length == 0 || B.length == 0) return null;  
    LinkedList<Integer> list = new LinkedList<Integer>();  
    int pointerA = 0;  
    int pointerB = 0;  
    while (pointerA < A.length && pointerB < B.length) {  
        if (A[pointerA] < B[pointerB]) pointerA++;  
        else if (A[pointerA] > B[pointerB]) pointerB++;  
        else {  
            list.add(A[pointerA]);  
            pointerA++;  
            pointerB++;  
        }  
    }  
    return list;  
} 
```

- 对于多个数组的情况同样可以用上面的方法或者：首先找到最短的数组，接着对这个数组中的值用二分查找在其他数组中寻找。

#### 4.二叉搜索树转换为双向链表

```c++
void ConvertNode(BinaryTreeNode *pNode, BinaryTreeNode **pLastNodeInList) {
    if(pNode == nullptr)
        return;
    
    BinaryTreeNode *pCurrent = pNode;
    if (pCurrent->m_pLeft != nullptr)
        ConvertNode(pCurrent->m_pLeft, pLastNodeInList);
    
    pCurrent->m_pLeft = *pLastNodeInList;
    if (*pLastNodeInList != nullptr)
        (*pLastNodeInList)->m_pRight = pCurrent;
    *pLastNodeInList = pCurrent;
    
    if (pCurrent->m_pRight != nullptr)
        ConvertNode(pCurrent->m_pRight, pLastNodeInList);
}

BinaryTreeNode* Convert(BinaryTreeNode* pRootOfTree) {
    BinaryTreeNode *pLastNodeInList = nullptr;
    ConvertNode(pRootOfTree, &pLastNodeInList);
    
    //pLastNodeInList point to the last one node of the list
    BinaryTreeNode *pHeadOfList = pLastNodeInList;
    while(pHeadOfList != nullptr && pHeadOfList->m_pLeft != nullptr)
        pHeadOfList = pHeadOfList->m_pLeft;
    
    return pHeadOfList;
}
```

#### 5.从尾到头打印链表

```c++
void PrintListReversingly_Iteratively(ListNode *pHead)
{
    stack<ListNode* > nodes;
    
    ListNode* pNode = pHead;
    while(pNode != nullptr) {
        nodes.push(pNode);
        pNode = pNode->m_pNext;
    }

    while(!nodes.empty())
    {
        pNode = nodes.top();
        cout << pNode->m_nValue << endl;
        nodes.pop();
    }
}
```



#### 6.重建二叉树

```c++
BinaryTreeNode *ConstructCore(int *startPreorder, int *endPreorder, int *startInorder, int *endInorder) {
    // 前序遍历的第一个数值是根结底
    int rootValue = startPreorder[0];
    BinaryTreeNode* root = new BinaryTreeNode(rootValue);
    
    if (startPreorder == endPreorder)
    {
        if (startInorder == endInorder && *startPreorder == *startInorder)
            return root;
        else
            throw runtime_error("Invalid input.");
    }
    
    // 在中序遍历序列中找到根节点的值
    int *rootInorder = startInorder;
    while (rootInorder <= endInorder && *rootInorder != rootValue)
        ++rootInorder;
    
    if (rootInorder == endInorder && *rootInorder != rootValue)
        throw runtime_error("Invalid input.");
    
    int leftLength = int(rootInorder - startInorder);
    int *leftPreorderEnd = startPreorder + leftLength;
    if (leftLength > 0) {
        // 构建左子树
        root->m_pLeft = ConstructCore(startPreorder + 1, leftPreorderEnd, startInorder, rootInorder - 1);
    }
    if (leftLength < endPreorder - startPreorder)
    {
        root->m_pRight = ConstructCore(leftPreorderEnd + 1, endPreorder, rootInorder + 1, endInorder);
    }
    
    return root;
}

BinaryTreeNode *Construct(int *preorder, int *inorder, int length){
    if (preorder == nullptr || inorder == nullptr || length <= 0)
        return nullptr;
    
    return ConstructCore(preorder, preorder + length - 1, inorder, inorder + length - 1);
}
```

#### 7.下一个节点

```c++
BinaryTreeNode *GetNext(BinaryTreeNode *pNode) {
    if (pNode == nullptr)
        return  nullptr;
    
    BinaryTreeNode *pNext = nullptr;
    if (pNode->m_pRight != nullptr) {
        BinaryTreeNode *pRight = pNode->m_pRight;
        while (pRight != nullptr)
            pRight = pRight->m_pLeft;
        pNext = pRight;
    }
    else if (pNode->m_pParent != nullptr) {
        BinaryTreeNode *pCurrent = pNode;
        BinaryTreeNode *pParent = pNode->m_pParent;
        while(pParent != nullptr && pCurrent == pParent->m_pRight)
        {
            pCurrent = pParent;
            pParent = pParent->m_pParent;
        }
        pNext = pParent;
    }
    return pNext;
}
```



#### 8.二维数组的查找

```c++
bool Find(int *matrix, int rows, int columns, int number){
    bool found = false;
    
    if (matrix != nullptr && rows > 0 && columns > 0)
    {
        int row = 0;
        int column = columns - 1;
        while (row < rows && column >= 0)
        {
            if (matrix[row*columns + column] == columns)
            {
                found = true;
                break;
            }
            else if (matrix[row*columns + column] > number)
                -- column;
            else
                ++ row;
        }
    }
    return found;
}
```



#### 9.替换字符串中的空节点

```c++
void ReplaceBlank(char string[], int length)
{
    if (string == nullptr || length <= 0)
        return;
    
    int originalLength = 0;
    int numberOfBlank = 0;
    int i = 0;
    while (string[i] != '\0')
    {
        ++originalLength;
        if (string[i] == ' ')
            ++numberOfBlank;
        ++i;
    }
    
    int newLength = originalLength + numberOfBlank * 2;
    if (newLength > length)
        return;
    
    int indexOfOriginal = originalLength;
    int indexOfNew = newLength;
    while (indexOfOriginal >= 0 && indexOfNew > indexOfOriginal)
    {
        if (string[indexOfOriginal] == ' ')
        {
            string[indexOfNew --] = '0';
            string[indexOfNew --] = '2';
            string[indexOfNew --] = '%';
        }
        else
            string[indexOfNew --] = string[indexOfOriginal];
        
        -- indexOfOriginal;
    }
}
```



#### 10.斐波那契数列

```c++
long long Fibonacci(unsigned n){
    int result[2] = {0, 1};
    if (n < 2)
        return result[n];
    
    long long fibNMinusOne = 1;
    long long fibNMinusTwo = 0;
    long long fibN = 0;
    for (unsigned int i = 2; i <= n; ++i)
    {
        fiN = fibNMinusOne + fibNMinusTwo;
        
        fibNMinusTwo = fibNMinusOne;
        fibNMinusOne = fibN;
    }
    return fibN;
}
```



#### 11.旋转数组中的最小值

```c++
int Min(int *numbers, int length){
    if (numbers == nullptr || length <= 0)
        throw runtime_error("Invalid Parameters.");
    
    int index1 = 0;
    int index2 = length - 1;
    int indexMid = index1;
    while(numbers[index1] >= numbers[index2])
    {
        if (index2 - index1 == 1)
        {
            indexMid = index2;
            break;
        }
        
        indexMid = (index1 + index2) / 2;
        
        if (numbers[index1] == numbers[index2] && numbers[indexMid] == numbers[index1])
            return MinInOrder(numbers, index1, index2);
        if (numbers[indexMid] >= numbers[index1])
            index1 = indexMid;
        else if (numbers[indexMid] <= numbers[index2])
            index2 = indexMid;
    }
    
    return numbers[indexMid];
}
```



#### 12.在O(1)时间内删除链表结点

```c++
/**
 删除当前节点的下一个节点
 
 @param pListHead 头指针
 @param pToBeDeleted 当前节点
 */
void DeleteNode(ListNode** pListHead, ListNode* pToBeDeleted)
{
    if (!pListHead || !pToBeDeleted)
        return;
    
    if (pToBeDeleted->m_pNext != nullptr)
    {
        ListNode* pNext = pToBeDeleted->m_pNext;
        pToBeDeleted->m_nValue = pNext->m_nValue;
        pToBeDeleted->m_pNext = pNext->m_pNext;
        
        delete pNext;
        pNext = nullptr;
    }
    else if (*pListHead == pToBeDeleted)
    {
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
        *pListHead = nullptr;
    }
    else
    {
        ListNode *pNode = *pListHead;
        while(pNode->m_pNext != pToBeDeleted)
            pNode = pNode->m_pNext;
        pNode->m_pNext = nullptr;
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
    }
}The 
```

###04-14

#### 13.调整数组顺序使得奇数位于偶数前面

```c++
/**
 ReorderOddEven的辅助函数

 @param pData 数组
 @param length 数组长度
 @param func 辅助函数
 */
void Reorder(int *pData, unsigned int length, bool (*func)(int))
{
    if (pData == nullptr || length <= 0)
        return;
    
    int *pBegin = pData;
    int *pEnd = pData + length - 1;
    
    while(pBegin < pEnd)
    {
        while(pBegin < pEnd && !func(*pBegin))
            ++pBegin;
        while(pBegin < pEnd && func(*pEnd))
            --pEnd;
        
        if (pBegin < pEnd)
        {
            int temp = *pBegin;
            *pBegin = *pEnd;
            *pEnd = temp;
        }
    }
}

/**
 ReorderOddEven函数的辅助函数

 @param n 数字n
 @return 是否是偶数，如果是则为true。否则false。
 */
bool isEven(int n)
{
    return (n & 1) == 0;
}

/**
 使得奇数排列在偶数之前
 
 @param pData 数组
 @param length 数组长度
 */
void ReorderOddEven(int* pData, unsigned int length)
{
    Reorder(pData, length, isEven);
}
```



#### 14.

#### 15.

#### 16.

#### 17.

#### 18

#### 19.

#### 20

#### 21.











