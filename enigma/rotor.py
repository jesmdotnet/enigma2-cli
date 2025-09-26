class Rotor:
    def __init__(self, wiring, notch, position='A'):
        self.wiring = wiring
        self.inverse_wiring = ''.join(sorted(wiring, key=lambda c: wiring.index(c)))
        self.notch = notch
        self.position = position.upper()

    def step(self):
        self.position = chr((ord(self.position)-65+1)%26+65)

    def at_notch(self):
        return self.position == self.notch

    def encode_forward(self, c):
        index = (ord(c)-65+ord(self.position)-65)%26
        return self.wiring[index]

    def encode_backward(self, c):
        index = (self.inverse_wiring.index(c)-(ord(self.position)-65))%26
        return chr(index+65)
