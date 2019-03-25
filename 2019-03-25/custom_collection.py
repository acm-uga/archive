import random

class CustomCollection:
    '''A combination of a list and a hashmap.

    This collections implements all methods in constant time.
    '''

    def __init__(self):
        '''Construct an empty collection.
        '''
        self.items = []  # A list holding the elements.
        self.positions = {}  # A map from element to its position in the list.

    def insert(self, elm):
        '''Insert an element into the collection.
        '''
        # Append to the end of the list.
        pos = len(self.items)
        self.items.append(elm)
        self.positions[elm] = pos

    def find(self, elm):
        '''Return ``True`` if the element is in the collection.
        '''
        # Lookup the element in the hashmap.
        return elm in self.positions

    def pick_random(self):
        '''Return a random element from the collection.
        '''
        # Roll a random number, then pick the element at that position.
        i = random.randrange(len(self.items))
        return self.items[i]

    def delete(self, elm):
        '''Remove an element from the collection.
        '''
        # Perform a "swap-delete": swap the given element with the one
        # at the end of the list, then pop it from the list.
        last = self.items[-1]

        if last == elm:
            del self.items[-1]
            del self.positions[elm]
            return

        i = self.positions[elm]
        j = self.positions[last]
        self.items[i], self.items[j] = self.items[j], self.items[i]
        self.positions[last] = i
        return self.items.pop()
