class Deque:

    def __init__(self, capacity):
        assert 0 < capacity
        self.store = [None for _ in range(capacity)]
        self.cap = capacity
        self.len = 0
        self.front = 0  # the index after the last element
        self.back = 0  # the index before the first element

    def push_front(self, val):
        if self.cap == self.len:
            self.reallocate()

        if self.front == self.cap:
            self.front = 0

        self.store[self.front] = val
        self.front += 1
        self.len += 1

    def push_back(self, val):
        if self.cap == self.len:
            self.reallocate()

        if self.back == 0:
            self.back = self.cap

        self.back -= 1
        self.store[self.back] = val
        self.len += 1

    def pop_front(self):
        if self.len == 0:
            raise IndexError("pop from empty deque")

        if self.front == 0:
            self.front = self.cap

        self.front -= 1
        val = self.store[self.front]
        self.store[self.front] = None
        self.len -= 1
        return val

    def pop_back(self):
        if self.len == 0:
            raise IndexError("pop from empty deque")

        if self.back == self.cap:
            self.back = 0

        val = self.store[self.back]
        self.store[self.back] = None
        self.back += 1
        self.len -= 1
        return val

    def get(self, i):
        if self.len <= i:
            raise IndexError("deque index out of bounds")

        back = 0 if self.back == self.cap else self.back
        return self.store[(back + i) % self.cap]

    def reallocate(self):
        # Copy our data into a temporary deque with twice the capacity.
        #
        # Note: we must double the capacity to maintain an amortized constant
        # time in the other methods. Growing by a constant factor will lead to
        # a linear amortized runtime.
        tmp_deque = Deque(self.cap * 2)
        while 0 < self.len:
            val = self.pop_back()
            tmp_deque.push_front(val)

        # Take ownership of the internal state of the temporay deque.
        self.store = tmp_deque.store
        self.cap = tmp_deque.cap
        self.len = tmp_deque.len
        self.front = tmp_deque.front
        self.back = tmp_deque.back



def test_deque():
    deque = Deque(5)
    assert deque.store == [None, None, None, None, None]
    assert deque.len == 0

    deque.push_front(1)
    deque.push_front(2)
    deque.push_front(3)
    assert deque.store == [1, 2, 3, None, None]
    assert deque.get(0) == 1
    assert deque.get(1) == 2
    assert deque.get(2) == 3
    assert deque.len == 3

    assert deque.pop_front() == 3
    assert deque.pop_back() == 1
    assert deque.store == [None, 2, None, None, None]
    assert deque.get(0) == 2
    assert deque.len == 1

    deque.push_back(4)
    deque.push_back(5)
    assert deque.store == [4, 2, None, None, 5], deque.store
    assert deque.get(0) == 5
    assert deque.get(1) == 4
    assert deque.get(2) == 2
    assert deque.len == 3

    assert deque.pop_back() == 5
    assert deque.pop_back() == 4
    assert deque.store == [None, 2, None, None, None]
    assert deque.get(0) == 2
    assert deque.len == 1

    deque.push_front(6)
    deque.push_front(7)
    deque.push_front(8)
    deque.push_front(9)
    assert deque.store == [9, 2, 6, 7, 8]
    assert deque.get(0) == 2
    assert deque.get(1) == 6
    assert deque.get(2) == 7
    assert deque.get(3) == 8
    assert deque.get(4) == 9
    assert deque.len == 5

    assert deque.pop_front() == 9
    assert deque.pop_back() == 2
    assert deque.store == [None, None, 6, 7, 8]
    assert deque.get(0) == 6
    assert deque.get(1) == 7
    assert deque.get(2) == 8
    assert deque.len == 3

    assert deque.pop_front() == 8
    assert deque.pop_back() == 6
    assert deque.pop_front() == 7
    assert deque.store == [None, None, None, None, None]
    assert deque.len == 0
    assert deque.front == 3
    assert deque.back == 3

    deque.push_back(0)
    deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)
    assert deque.store == [2, 1, 0, None, 3]
    assert deque.len == 4

    deque.push_front(4)
    deque.push_front(5)
    assert deque.store == [3, 2, 1, 0, 4, 5, None, None, None, None]
    assert deque.len == 6
    assert deque.cap == 10
