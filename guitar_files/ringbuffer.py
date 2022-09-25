#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        self.capacity = capacity
        self.buffer = [None] * capacity

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        return len(self.buffer)

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        return self.size == 0 
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        return self.size == self.capacity

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        self.buffer.append(x)

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        # TO-DO: implement this

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this


class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
