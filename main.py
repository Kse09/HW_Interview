class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст!")
        return self.items[-1]

    def size(self):
        return len(self.items)



def is_balanced_brackets(brackets_string):
    brackets_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    opening_brackets = set(brackets_dict.keys())
    closing_brackets = set(brackets_dict.values())

    stack = Stack()

    for char in brackets_string:
        if char in opening_brackets:
            stack.push(char)

        elif char in closing_brackets:
            if stack.is_empty():
                return False

            last_opening = stack.pop()

            if brackets_dict[last_opening] != char:
                return False

    return stack.is_empty()


def main():
    brackets_string = input("Введите строку со скобками: ")

    if is_balanced_brackets(brackets_string):
        print("Сбалансированно")
    else:
        print("Несбалансированно")


if __name__ == "__main__":
    main()
