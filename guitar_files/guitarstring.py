#!/usr/bin/env python3
from random import random
from ringbuffer import RingBuffer
class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 24000 Hz
        '''
        N = 24000/frequency
        self.newBuffer = RingBuffer(int(N))
        self.numTicks = 0
        for i in range(N):
            self.newBuffer.enqueue(0)
          
    def make_from_array(self, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # TO-DO: implement this

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        for i in range(self.newBuffer.size()):
            self.newBuffer[i] = random.uniform(-1/2,1/2)
            
    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        self.numTicks += 1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        return self.newBuffer.peek()
    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.numTicks