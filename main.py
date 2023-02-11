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
    
    return "Sucsess"



def main():
    text = input()
    if text[0] == "I":
        if len(text) > 10**5 : 
            return
    mismatch = find_mismatch(text)
    print(mismatch)
    
if __name__ == "__main__":
    main()
