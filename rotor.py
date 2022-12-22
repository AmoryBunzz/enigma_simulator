class Reflector(object):
    def __init__(self, wiring=None, name=None, model=None, date=None):
        if wiring != None:
            self.wiring = wiring
        else:
            self.wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = name
        self.model = model
        self.date = date

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def encipher(self, key):
        shift = (ord(self.state) - ord('A'))
        index = (ord(key) - ord('A')) % 26  # true index
        index = (index + shift) % 26  # actual connector hit

        letter = self.wiring[index]  # rotor letter generated
        out = chr(ord('A')+(ord(letter) - ord('A') + 26 - shift) %
                  26)  # actual output
        # return letter
        return out

    def __eq__(self, rotor):
        return self.name == rotor.name

    def __str__(self):
        return """
        Name: %s
        Model: %s
        Date: %s
        Wiring: %s""" % (self.name, self.model, self.date, self.wiring)


class Rotor(object):
    def __init__(self, wiring=None, notchs=None, name=None, model=None, date=None, state="A", ring="A"):
        if wiring != None:
            self.wiring = wiring
        else:
            self.wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rwiring = ["0"] * 26
        for i in range(0, len(self.wiring)):
            self.rwiring[ord(self.wiring[i]) - ord('A')] = chr(ord('A') + i)
        if notchs != None:
            self.notchs = notchs
        else:
            self.notchs = ""
        self.name = name
        self.model = model
        self.date = date
        self.state = state
        self.ring = ring

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == 'wiring':
            self.rwiring = ["0"]*26
            for i in range(0, len(self.wiring)):
                self.rwiring[ord(self.wiring[i]) - ord('A')] = chr(ord('A')+i)

    def encipher_right(self, key):
        shift = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A')) % 26  # true index
        index = (index + shift) % 26  # actual connector hit

        letter = self.wiring[index]  # rotor letter generated
        out = chr(ord('A')+(ord(letter) - ord('A') + 26 - shift) %
                  26)  # actual output
        # return letter
        return out

    def encipher_left(self, key):
        shift = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A')) % 26
        index = (index + shift) % 26
        letter = self.rwiring[index]
        out = chr(ord('A')+(ord(letter) - ord('A') + 26 - shift) % 26)
        # return letter
        return out

    def notch(self, offset=1):
        self.state = chr((ord(self.state) + offset - ord('A')) % 26 + ord('A'))
        notchnext = self.state in self.notchs

    def is_in_turnover_pos(self):
        return chr((ord(self.state) + 1 - ord('A')) % 26 + ord('A')) in self.notchs

    def __eq__(self, rotor):
        return self.name == rotor.name

    def __str__(self):
        return """
        Name: %s
        Model: %s
        Date: %s
        Wiring: %s
        State: %s""" % (self.name, self.model, self.date, self.wiring, self.state)


# Enigma
ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notchs="R",
                name="I", model="Enigma 1", date="1930")
ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE",
                 notchs="F", name="II", model="Enigma 1", date="1930")
ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO",
                  notchs="W", name="III", model="Enigma 1", date="1930")
ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", notchs="K",
                 name="IV", model="M3 Army", date="December 1938")
ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", notchs="A",
                name="V", model="M3 Army", date="December 1938")
ROTOR_VI = Rotor(wiring="JPGVOUMFYQBENHZRDKASXLICTW", notchs="AN",
                 name="VI", model="M3 & M4 Naval(February 1942)", date="1939")
ROTOR_VII = Rotor(wiring="NZJHGRCXMYSWBOUFAIVLPEKQDT", notchs="AN",
                  name="VII", model="M3 & M4 Naval(February 1942)", date="1939")
ROTOR_VIII = Rotor(wiring="FKQHTLXOCBJSPDZRAMEWNIUYGV", notchs="AN",
                   name="VIII", model="M3 & M4 Naval(February 1942)", date="1939")

# Reflectors
ROTOR_Reflector = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD")
