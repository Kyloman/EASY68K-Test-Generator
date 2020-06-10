import array as arr
import random as rand

#HERE IS ALL MODIFIABLE VARIABLES

#QUANTITY
#How many different sets of instructions you want. 1 is minimum
tests = 1

#INSTRUCTION
opcode = "MOVE"

#SET ALL POSSIBLE SIZES
bytesize = True
wordsize = True
longsize = True

#SET NUMBER OF OPERANDS HERE 
#ZERO,ONE,TWO
operands = "TWO"

#SET ALL POSSIBLE ADDRESSING MODES FOR OPERAND 1
Dn1 = True
An1 = True 
PAnP1 = True
PAnPPlus1 = True
MinusPAnP1 = True
Imm = True
xxxW1 = True
xxxL1 = True

#SET ALL POSSIBLE ADDRESSING MODES FOR OPERAND 1
Dn2 = True 
An2 = True
PAnP2 = True
PAnPPlus2 = True
MinusPAnP2 = True
Imm2 = False
xxxW2 = True
xxxL2 = True

chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "0"]
ea1 = [Dn1, An1, PAnP1,PAnPPlus1,MinusPAnP1, Imm, xxxW1, xxxL1]
ea2 = [Dn2, An2, PAnP2,PAnPPlus2,MinusPAnP2, Imm2, xxxW2, xxxL2]

def print_size(size):
    if(size == "B"):
        file1.write(".B")
    if(size == "W"):
        file1.write(".W")
    if(size == "L"):
        file1.write(".L")
    
def print_opcode():
    line = "     " + opcode + ""
    file1.write(line)

def getRandByte():
    tempstring = ""
    tempstring += str(chars[rand.randint(0,15)])
    tempstring += str(chars[rand.randint(0,15)])
    return tempstring

def getRandWord():
    tempstring = ""
    tempstring += getRandByte()
    tempstring += getRandByte()
    return tempstring

def getRandLong():
    tempstring = ""
    tempstring += getRandWord()
    tempstring += getRandWord()
    return tempstring    
    

def getOperand(ind):
    #Dn
    if(ind == 1):
        file1.write("D" + str(rand.randint(0,7)))
    #An
    elif(ind == 2):
        file1.write("A" + str(rand.randint(0,6)))
    #(An)
    elif(ind == 3):
        file1.write("(A" + str(rand.randint(0,6)) + ")")
    #(An)+
    elif(ind == 4):
        file1.write("(A" + str(rand.randint(0,6)) + ")+")
    #-(An)
    elif(ind == 5):
        file1.write("-(A" + str(rand.randint(0,6)) + ")")
    ##Imm
    elif(ind == 6):
        file1.write("#$" + str(getRandByte()))
    #(xxx).W
    elif(ind == 7):
        file1.write("$" + str(getRandWord()))
    #(xxx).L
    elif(ind == 8):
        file1.write("$" + str(getRandLong()))
    else:
        file1.write(";ERROR")    
#CODE STARTS HERE
currop1 = 0
currop2 = 0 
        
filename = str(r'C:\Users\kylom_000\Documents\School Work\Python Projects\ASSEMBLERTESTS\TEST_' + opcode + ".txt")
file1 = open(filename,"w+")
file1.write(opcode + "_FULLTEST\n")        

#ZERO OPERANDS
if(operands == "ZERO"):
    for x in range (0,6):
        print_opcode()
        file1.write('\n')

#ONE OPERAND
if(operands == "ONE"):
    for x in range (0,tests):
        currop1 = 0
        while(currop1 != 8):
            currop1 += 1
            if(ea1[currop1 - 1] == True):
                print_opcode()
                file1.write(" ")
                getOperand(currop1)
                file1.write("\n")
        if(bytesize == True):
            currop1 = 0
            while(currop1 != 8):
                currop1 += 1
                if(ea1[currop1 - 1] == True):
                    print_opcode()
                    file1.write(".B ")
                    getOperand(currop1)
                    file1.write("\n")
        if(wordsize == True):
            currop1 = 0
            while(currop1 != 8):
                currop1 += 1
                if(ea1[currop1 - 1] == True):
                    print_opcode()
                    file1.write(".W ")
                    getOperand(currop1)
                    file1.write("\n")
        if(longsize == True):
            currop1 = 0
            while(currop1 != 8):
                currop1 += 1
                if(ea1[currop1 - 1] == True):
                    print_opcode()
                    file1.write(".L ")
                    getOperand(currop1)
                    file1.write("\n")
                    
#TWO OPERANDS
if(operands == "TWO"):
    for x in range (0,tests):
        currop1 = 0
        while(currop1 != 8):
            currop1 += 1
            currop2 = 0
            if(ea1[currop1 - 1] == True):
                while(currop2 != 8):
                    currop2 += 1
                    if(ea2[currop2 - 1] == True):
                        print_opcode()
                        file1.write(" ")
                        getOperand(currop1)
                        file1.write(",")
                        getOperand(currop2)
                        file1.write("\n")
        if(bytesize == True):
            currop1 = 0
            while(currop1 != 8):
                currop1 += 1
                currop2 = 0
                if(ea1[currop1 - 1] == True and currop1 != 2):
                    while(currop2 != 8):
                        currop2 += 1
                        if(ea2[currop2 - 1] == True and currop2 != 2):
                            print_opcode()
                            file1.write(".B ")
                            getOperand(currop1)
                            file1.write(",")
                            getOperand(currop2)
                            file1.write("\n")
        if(wordsize == True):
            currop1 = 0
            while(currop1 != 8):
                currop1 += 1
                currop2 = 0
                if(ea1[currop1 - 1] == True):
                    while(currop2 != 8):
                        currop2 += 1
                        if(ea2[currop2 - 1] == True):
                            print_opcode()
                            file1.write(".W ")
                            getOperand(currop1)
                            file1.write(",")
                            getOperand(currop2)
                            file1.write("\n")
        if(longsize == True):
            currop1 = 0
            while(currop1 != 8):
                currop1 += 1
                currop2 = 0
                if(ea1[currop1 - 1] == True):
                    while(currop2 != 8):
                        currop2 += 1
                        if(ea2[currop2 - 1] == True):
                            print_opcode()
                            file1.write(".L ")
                            getOperand(currop1)
                            file1.write(",")
                            getOperand(currop2)
                            file1.write("\n")
      
file1.close()

 


