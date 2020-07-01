# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque, OrderedDict

class Leaf:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def show(self):
        print(f'key: {self.key}, val: {self.value}')  

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    
def haffman_tree(s: str) -> Node:
    data = []
    freq = Counter(s)

    for k, v in freq.most_common():
        data.append(Leaf(k, v))

    while len(data) > 2:
        r, l = data.pop(), data.pop()
        temp = Node(l.value + r.value, l, r)
        if temp.value < data[-1].value:
            data.append(temp)
        elif temp.value > data[0].value:
            data.insert(0, temp)
        else:
            for i in range(len(data)):
                if temp.value > data[i].value:
                    data.insert(i+1, temp)
                    break
                elif i == len(data) - 1:
                    data.append(temp)

    data = Node(data[0].value + data[1].value, data[0], data[1])

    return data

def encode_dict(data: Node, encodings=dict(), code="") -> dict:
    if isinstance(data, Leaf):
        encodings[data.key] = code
    elif isinstance(data, Node):
        encode_dict(data.left, code=code+'0')
        encode_dict(data.right, code=code+'1')

    return encodings
        
def encode(s: str, encodings: dict()) -> str:
    res = []
    for char in s:
        res.append(encodings[char])
    return ''.join(res)

def decode(e_s: str, encodings: dict()) -> str:
    encodings = {value: key for key, value in encodings.items()}
    res = []

    i = 0
    while i < len(e_s):
        j = i + 1
        while e_s[i:j] not in encodings.keys():
            j += 1
        res.append(encodings[e_s[i:j]])
        i = j
    
    return ''.join(res)
    
def haffman_encoding(s:str):

    print(f'Строка для кодирования: {s}')

    tree = haffman_tree(s)

    encodings = encode_dict(tree, code="")

    print(f'Cловарь кодирования: {encodings}')

    encoded_s = encode(s, encodings)

    print(f'Закодированная строка: {encoded_s}')

    decoded_s = decode(encoded_s, encodings)

    print(f'Расшифрованная строка: {decoded_s}')



s = input("Введите строку которую нужно закодировать: ")

haffman_encoding(s)
