class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        self.capacity = capacity
        self.buffer = list()
        self.front = self.rear = 0

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
        if self.is_full == True:
            RingBufferFull
        elif self.rear == self.capacity:
            self.rear = 0
        else:
            self.buffer.append(x)
            self.rear += 1

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if self.is_empty == True:
            RingBufferEmpty
        
        elif self.front == self.capacity:
            self.front = 0
        else:
            x = self.buffer[self.front]
            self.front += 1
            return x 
    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        return self.buffer[self.front]
    
    def printBuffer(self):
        print(self.buffer)
        
class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
