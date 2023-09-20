from stack import Stack

def is_balanced(line: str) -> bool:
    stack = Stack()
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    if line[0] in close_brackets:
        return False
    for char in line:
        if char in open_brackets:
            stack.push(open_brackets.index(char))
        elif char in close_brackets:
            if stack.size() != 0 and stack.peek() == close_brackets.index(char):
                stack.pop()
            else:
                return False
    return stack.is_empty()

if __name__ == '__main__':
    assert is_balanced('(((([{}]))))') == True
    assert is_balanced('[([])((([[[]]])))]{()}') == True
    assert is_balanced('{{[()]}}') == True
    assert is_balanced('}{}') == False
    assert is_balanced('{{[(])]}}') == False
    assert is_balanced('[[{())}]') == False