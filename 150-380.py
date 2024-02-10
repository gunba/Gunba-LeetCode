import random

class RandomizedSet(object):
    def __init__(self):
        self.s = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.s:
            self.s.append(val)
            return True
        else:
            return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        try:
            self.s.remove(val)
            return True
        except ValueError:
            return False
       

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.s)