#!/usr/bin/env python3
import random
from ringbuffer import RingBuffer
import math
class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 24000 Hz
        '''
        self.capacity = math.ceil(24000/frequency)
        self.buffer = RingBuffer(self.capacity)
        self.numTicks = 0
        for i in range(self.capacity):
            self.buffer.enqueue(0)
    
    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        for i in range(self.capacity):
            self.buffer.buffer[i] = random.uniform(-1/2,1/2)
            
    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        
        x = self.buffer.peek()
        self.buffer.dequeue()
        y = self.buffer.peek()
        self.buffer.enqueue(0.996*(x+y)/2)
        self.numTicks+=1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        return self.buffer.peek()
        
    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.numTicks