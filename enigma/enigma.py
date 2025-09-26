from .rotor import Rotor
from .plugboard import Plugboard
from .rotors_data import ROTORS, REFLECTOR

class EnigmaMachine:
    def __init__(self, rotor_names, start_positions, plugboard_pairs=None):
        self.rotors = [Rotor(ROTORS[name]["wiring"], ROTORS[name]["notch"], pos)
                       for name,pos in zip(rotor_names,start_positions)]
        self.plugboard = Plugboard(plugboard_pairs)
        self.reflector = REFLECTOR
        self.initial_positions = start_positions

    def reset_rotors(self):
        for rotor,pos in zip(self.rotors,self.initial_positions):
            rotor.position = pos

    def step_rotors(self):
        if self.rotors[1].at_notch(): self.rotors[0].step(); self.rotors[1].step()
        elif self.rotors[2].at_notch(): self.rotors[1].step()
        self.rotors[2].step()

    def encrypt_char(self,c):
        if not c.isalpha(): return c
        self.step_rotors()
        c = self.plugboard.swap(c)
        for rotor in reversed(self.rotors): c = rotor.encode_forward(c)
        c = self.reflector[ord(c)-65]
        for rotor in self.rotors: c = rotor.encode_backward(c)
        return self.plugboard.swap(c)

    def encrypt(self,message):
        self.reset_rotors()
        return ''.join(self.encrypt_char(c.upper()) for c in message)
