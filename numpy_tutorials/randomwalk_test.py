import random
import numpy as np

class SomeInteger:
    value = 0

    def __init__(self, v):
        self.value = v

int = SomeInteger(10)
print(type(int))