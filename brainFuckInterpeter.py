pos = 0
posTape = [0]
negTape = []
loopStack = []

code = input()
i = 0
while i < len(code):
    instruction = code[i]
    if instruction == "<":
        pos -= 1
        if len(negTape) <= -pos:
            negTape.append(0)
    elif instruction == ">":
        pos += 1
        if len(posTape) <= pos:
            posTape.append(0)
    elif instruction == "+":
        if pos < 0:
            negTape[-pos] += 1
        else:
            posTape[pos] += 1
    elif instruction == "-":
        if pos < 0:
            negTape[-pos] -= 1
        else:
            posTape[pos] -= 1
    elif instruction == ".":
        if pos < 0:
            print(chr(negTape[-pos]), end='')
            ##print(negTape[-pos])
        else:
            print(chr(posTape[pos]), end='')
            ##print(posTape[pos])
    elif instruction == ",":
        if pos < 0:
            negTape[-pos] = ord(input())
        else:
            posTape[pos] = ord(input())
    elif instruction == "[":
        loopStack.append(i - 1)
    elif instruction == "]":
        if pos < 0:
           val = negTape[-pos] 
        else:
           val = posTape[pos]
        if val != 0:
            i = loopStack.pop()
    ##print(negTape,posTape," ",pos)
    i += 1
    
    