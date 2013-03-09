from node import *
from token import *
import scanner
from translatorExceptions import ParseTreeException

def printTreeTraversal(root):
    if root.data == "println" and root.rightChild is None:
        stringType = printTreeTraversalHelper(root.leftChild)
        print "CR "
        if stringType == "Real":
            print "f. "
        elif stringType == "String":
            print "type "
        else:
            print ". "
        print "CR "
    else:
        printTreeTraversalHelper(root)



def printTreeTraversalHelper(currentNode):
    if currentNode is None:
        return None

    leftType = printTreeTraversalHelper(currentNode.leftChild)
    rightType = printTreeTraversalHelper(currentNode.rightChild)

    if scanner.isConstant(currentNode.data):
        if scanner.isReal(currentNode.data):
            print currentNode.data + "e "
        elif scanner.isString(currentNode.data):
            print "s\" " + currentNode.data[1:]
        else:
            print currentNode.data
        return (scanner.getToken(currentNode.data)).Type

    elif scanner.isOperator(currentNode.data):
        numberOperands = scanner.getArgCount(currentNode.data)
        if numberOperands == 1 and rightType is None:
            # if operand is Real add a f in front of the operator
            if leftType == "Real" and rightType is None:
                print "f" + currentNode.data

            #if there is an integer using a real operation then convert the integer to real
            if leftType == "Integer" and scanner.isRealOperator(currentNode.data):
                print currentNode.data
                print "s>f"
            #is boolean type child and operator is boolean
            if leftType == "Boolean" and scanner.isBooleanOperator(currentNode.data):
                print itblToGforth(currentNode.data)
            #is integer type child and is integer operator
            if leftType == "Integer" and not scanner.isBooleanOperator(currentNode.data):
                print currentNode.data
            else:
                raise ParseTreeException(currentNode)
            return leftType

        elif numberOperands == 2:
            #children are same value no conversion needed
            if leftType == rightType:
                # children are real and real operator
                if leftType == "Real" and scanner.isRealOperator(currentNode.data):
                    print "f" + itblToGforth(currentNode.data) + " "
                # children are string and a +
                elif leftType == "String":
                    if currentNode.data == "+":
                        print "s" + itblToGforth(currentNode.data) + " "
                    else:
                        raise ParseTreeException(currentNode)
                # children are boolean and boolean operator
                elif leftType == "Boolean" and scanner.isBooleanOperator(currentNode.data):
                    print itblToGforth(currentNode.data)
                # children are integers and integer operator
                elif leftType == "Integer" and not scanner.isBooleanOperator(currentNode.data):
                    if currentNode.data == "^":
                        print "s>f"
                        print "s>f"
                        print "f" + itblToGforth(currentNode.data)
                        leftType = "Real"
                    else:
                        print itblToGforth(currentNode.data)
                # bad parse
                else:
                    raise ParseTreeException(currentNode)
                return leftType
            # type conversion needed to float
            elif (((leftType == "Integer" and rightType == "Real") or (leftType == "Real" and rightType == "Integer")) and not scanner.isBooleanOperator(currentNode.data)):
                print "s>f"
                if leftType == "Integer":
                    print "fswap"
                print "f" + itblToGforth(currentNode.data)
                return "Real"
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
        return "invert"
    if(operand == "iff"):
        return "invert xor"
    return operand
