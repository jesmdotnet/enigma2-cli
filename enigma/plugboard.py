class Plugboard:
    def __init__(self, pairs=None):
        self.mapping = {}
        if pairs:
            for pair in pairs:
                a,b = pair.split('-')
                self.mapping[a.upper()] = b.upper()
                self.mapping[b.upper()] = a.upper()
    def swap(self,c):
        return self.mapping.get(c.upper(), c.upper())
