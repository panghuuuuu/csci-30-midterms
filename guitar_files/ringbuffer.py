class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        self.MAX_CAP = capacity
        self.buffer = [None] * capacity
        self._front = self._rear = -1

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        return len(self.buffer)

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        return self.size() == 0

    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        return self.size() > self.MAX_CAP

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        if self.is_full() == True:
            raise RingBufferFull
        elif self._rear == self.MAX_CAP:
            self._rear = 0
            self._front = 0
        else:
            self.buffer[self._rear] = x
            self._rear += 1 % self.MAX_CAP
    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if self.is_empty() == True:
            raise RingBufferEmpty
        elif self._front == self.MAX_CAP:
            self._rear = 0
            self._front = 0
        else:
            x = self.peek()
            self._front += 1 % self.MAX_CAP
            return x

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        if self.is_empty() == True:
            raise RingBufferEmpty
        elif self._front == self.MAX_CAP:
            return self.buffer[0]
        else:
            return self.buffer[self._front]
class RingBufferFull(Exception):
    pass


class RingBufferEmpty(Exception):
    pass
