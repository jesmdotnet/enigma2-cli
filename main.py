import argparse
from enigma import EnigmaMachine

def parse_args():
    parser = argparse.ArgumentParser(description="Minimal Enigma CLI")
    parser.add_argument("message", help="Message to encrypt/decrypt")
    parser.add_argument("--rotors", nargs=3, choices=["1","2","3"], default=["1","2","3"])
    parser.add_argument("--start_positions", nargs=3, default=["A","A","A"])
    parser.add_argument("--plugboard", nargs="*", default=[])
    return parser.parse_args()

def main():
    args = parse_args()
    machine = EnigmaMachine(args.rotors, args.start_positions, args.plugboard)
    print(machine.encrypt(args.message))

if __name__ == "__main__":
    main()
