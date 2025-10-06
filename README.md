# enigma2-cli
A minimal Enigma Machine CLI implementation in Python.
Encrypt and decrypt messages using a configurable set of rotors, starting positions, and plugboard wiring. Designed to serve as a clean baseline for feature expansion and to practice GitHub Flow.

##Overview
enigma2-cli is a Python-based CLI for the classic Enigma encryption machine.
Supports 3 rotors (configurable order & start positions)
Basic plugboard wiring
Simple reflector
Designed as a foundation for adding advanced features like rotor combinations, multiple reflectors, and full plugboard support

##Installation

Clone the repo and set up a virtual environment:
git clone git@github.com:jesmdotnet/enigma2-cli.git
cd enigma2-cli
python3 -m venv venv
source venv/bin/activate

To run the CLI directly:
python3 main.py "YOUR MESSAGE"

##Usage
python3 main.py "HELLO WORLD" --rotors 1 2 3 --start_positions A A A --plugboard A-B C-D
###Arguments:
message → The text to encrypt/decrypt
--rotors → Three rotors to use (default: 1 2 3)
--start_positions → Starting letters for the rotors (default: A A A)
--plugboard → Optional pairs, e.g., A-B C-D

##Features

Minimal working Enigma encryption/decryption
Supports plugboard wiring
Configurable rotor order and start positions
Ready for feature expansion

##Contributing

###We use GitHub Flow:
main → stable, production-ready
develop → active development branch
Feature branches → branch off develop for each new feature
PRs → merge feature branches into develop after testing
Merge develop into main for releases

###Commit Messages:
Use meaningful, concise messages:
Add feature: plugboard wiring validation
Fix: rotor stepping bug

##Roadmap

###Future planned features:
Rotor Combinations → Choose 3 out of 5 rotors
Full Plugboard Wiring → Arbitrary letter pair swaps
Multiple Reflectors → Allow different reflector wirings
Start Position Validation → Ensure input letters A-Z
CLI Improvements → Explicit encrypt/decrypt mode, help messages
Packaging & Installable CLI → pip install -e . and global command
Unit Testing → Automated tests for machine logic
Advanced Features → Rotor stepping enhancements, historical wiring modes