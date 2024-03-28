"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
    
    >>> serial
    SerialGenerator(start = 100, next = 101)
    
    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start = 0):
        """Instantiates the start and next values of the generator"""
        self.start = self.next = start
        
    def __repr__ (self):
        return f"SerialGenerator(start = {self.start}, next = {self.next + 1})"
    
    def generate (self):
        """Adds one to the previously generated serial number"""
        self.next += 1
        return self.next - 1
    
    def reset (self):
        """Resets current serial number to the iniaial value"""
        self.next = self.start

