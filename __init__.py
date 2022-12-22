import rotor
import enigma

__author__ = "Nguyen Dang Tuan Kiet, Mai Xuan Nhat"
__version__ = "0.0.1"
__date__ = "$Date: 2022/12/22 $"

print("\n------------ Enigma Simulator ------------\n")
print(__author__)
print(__version__)
print(__date__)
print("\n------------------------------------------\n")

available_rotors = {
    "ROTOR_I": rotor.ROTOR_I,
    "ROTOR_II": rotor.ROTOR_II,
    "ROTOR_III": rotor.ROTOR_III,
    "ROTOR_IV": rotor.ROTOR_IV,
    "ROTOR_V": rotor.ROTOR_V,
    "ROTOR_VI": rotor.ROTOR_VI,
    "ROTOR_VII": rotor.ROTOR_VII,
    "ROTOR_VIII": rotor.ROTOR_VIII,
}

print("\n-------------- Enigma Setup --------------\n")

print("""List of available Rotors:
ROTOR_I
ROTOR_II
ROTOR_III
ROTOR_IV
ROTOR_V
ROTOR_VI
ROTOR_VII
ROTOR_VIII\n
""")

enigma_rotors = []
order = ['1st', '2nd', '3rd']
index = 0
while index <= 2:
    rotor_name = ''
    while rotor_name not in available_rotors.keys():
        rotor_name = input("Please choose " + order[index] + " rotor: ")

    enigma_rotors.append(available_rotors[rotor_name])
    index += 1

plugs_config = input(
    "\nType in plugboard wiring configuration (Ex: AV BS CG DL FU HZ IN KM OW RX): ")

init_key = input("\nType in initial key for rotor's position (Ex: ABC): ")

enigma_simulator = enigma.Enigma(rotor.ROTOR_Reflector, enigma_rotors[0],
                                 enigma_rotors[1], enigma_rotors[2],
                                 key=init_key, plugs=plugs_config)

print("\nConfigurations and Structures of Enigma machine:")
print(enigma_simulator)
print("\n")

plaintext = input("Type in plaintext to encrypt / decrypt: ")

print("\nResult: ", enigma_simulator.encipher(plaintext))
print("\n")
