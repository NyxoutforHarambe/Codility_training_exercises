def is_matched(expression):
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    print(mapping)
    queue = []

    for letter in expression:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

print(is_matched('(){}[][][]([]{})'))