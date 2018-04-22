#F. Derek Roman - GitHub Profile CodeNamor
#SWDV-610-3W Data Structures Unit 6

#define imports needed for this module
from Stack import *
from BinaryTree import BinaryTree

#define the buildParseTree function
def buildParseTree(treeExpression):
    list = treeExpression.split()
    pStack = Stack
    bTree = BinaryTree
    pStack.push(list)
    currentTree = bTree
    #follwoing the rules for buiding a parse tree
    for i in list:
        #if '( ' is the first token, by Rule 1 of parse trees add a new left node
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        #add functionality to handle boolean values
        elif i == True or False:
            #pop the value
            currentTree= pStack.pop()
        else:
            #if there is a problem raise a Value Error
            raise ValueError
    #return the tree
    return bTree

def main():
    #if spaces are added to the equation
    mathEq = "(  (  10  +  5  )  *  3  ) "
    #remove the extra spaces
    mathEqStrip = mathEq.strip(" ")
    #send the stripped equation to the build Parse Tree function
    pt = buildParseTree(mathEqStrip)
    pt.postorder()
    
main()
