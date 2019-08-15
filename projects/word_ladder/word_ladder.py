f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# KEYWORDS:
# Dictionary - Words are nodes
# Shortest - BFS
# Transformation sequence - Path


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def get_neighbors(word):  # get neighbors of any word
    neighbors = []
    # turning the word into an array or list of characters
    string_word = list(word)
    # loop through string_word and change each letter to letter
    # and check if it's a word in the provided file
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:  # if the word we started with
                neighbors.append(w)
    return neighbors

# Run search


def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        vertex = path[-1]
        if vertex not in visited:
            visited.add(vertex)
            if vertex == end_word:
                return path
            # create a path copy and enqueue with neighboring valid words
            for neighbor in get_neighbors(vertex):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print(find_word_ladder("hello", "world"))

# Make a graph
# Traverse it - Run BFS
# Parse the result in a way that matches the problem and return it
