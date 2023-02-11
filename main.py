# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return ((left + right) in ["()", "[]", "{}"])

def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            
            opening_brackets_stack.append(Bracket(char , i))


        if char in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching (opening_brackets_stack.pop().char, char):
                return i + 1     
    if  opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    
    return "Success"



def main():
    text = input()
    if text[0] == "I":
        text = input()
    if "F" in text:
        pass
    mismatch = find_mismatch(text)
    
    if not mismatch:
        print("Success")
    else:
        print(mismatch) 


if __name__ == "__main__":
    main()
