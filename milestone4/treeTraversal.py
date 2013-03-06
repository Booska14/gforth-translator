from binarytree import *
from token import *
from scanner import *
from translatorExceptions import ParseTreeException

def printTreeTraversal(root):
    printTreeTraversalHelper(currentNode)
    print " "


def printTreeTraversalHelper(currentNode):
    if currentNode is None:
        return None

    leftType = printTreeTraversalHelper(currentNode.leftChild)
    rightType = printTreeTraversalHelper(currentNode.rightChild)

    if scanner.isConstant(currentNode.data.Word):
        if leftType == "Real":
            print currentNode.data.Word + "e "
        elif leftType == "String":
            print "s\" " + currentNode.data.Word[1:]
        else:
            print currentNode.data.Word
        return currentNode.data.Type

    elif scanner.isOperator(currentNode.data.Word):
        numberOperands = scanner.getArgCount(currentNode.data.Word)
        if numberOperands == 1:
            if leftType == "Real" and rightType is None:
                print "f" + currentNode.data.Word + " "
                return leftType
            elif leftType is not None and rightType is None:
                print currentNode.data.Word + " "
                return leftType
            else:
                raise ParseTreeException(currentNode)
        elif numberOperands == 2:
            if leftType == rightType:
                if leftType == "Real":
                    print "f" + itblToGforth(currentNode.data.Word) + " "
                elif leftType == "String":
                    print "s" + itblToGforth(currentNode.data.Word) + " "
                else:
                    print itblToGforth(currentNode.data.Word) + " "
                return leftType
            else:
                raise ParseTreeException(currentNode)

    elif currentNode.data.Word == "println":
        if rightType is None:
            if leftType == "Real":
                print "f. CR"
            elif leftType == "String":
                print "type CR"
            else:
                print ". CR"
            return None
        else:
            raise ParseTreeException(currentNode)
    else:
        return None

def itblToGforth(operand):
    if(operand == "^"):
        return "**"
    if(operand == "%"):
        return "mod"
    if(operand == "logn"):
        return "ln"
    if(operand == "not"):
        return "negate"
    if(operand == "iff"):
        return "xor"
    return operand
