from token import *
from translatorExceptions import *
from parser import shlexToList
import tokenizer
import scanner
from node import *

stack = []

def createTree(fileContent):

    global stack
    stack = shlexToList(tokenizer.parseWords(fileContent))

    tok = stack.pop()

    # sanity check, this should always be true at this point
    if tok != "(":
        raise CreateParseTreeException(stack)

    root = createTreeHelper()

    # stack should now be empty
    if len(stack) != 1 and stack[0] != "$":
        raise CreateParseTreeException("Stack not empty")

    return root

def createTreeHelper():
    nextToken = stack.pop()
    newNode = None

    if nextToken == "(":
        newNode =  createTreeHelper()
    elif scanner.isConstant(nextToken):
        newNode = Node(nextToken)
    elif scanner.isOperator(nextToken):
        newNode = Node(nextToken)
        leftOperand = stack.pop()
        if leftOperand == "(":
            newNode.leftChild = createTreeHelper()
        elif scanner.isConstant(leftOperand):
            newNode.leftChild = Node(leftOperand)
        else:
            raise CreateParseTreeException(stack)

        if scanner.getArgCount(nextToken) == 2:
            rightOperand = stack.pop()
            if rightOperand == "(":
                newNode.rightChild = createTreeHelper()
            elif scanner.isConstant(rightOperand):
                newNode.rightChild = Node(rightOperand)
            else:
                raise CreateParseTreeException(stack)

    else:
        raise CreateParseTreeException(stack)

    lastToken = stack.pop()
    if lastToken != ")":
        raise CreateParseTreeException(stack)

    return newNode

def printTree(node):
    if node is not None:
        printTree(node.leftChild)
        printTree(node.rightChild)
        print node.data


