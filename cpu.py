import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110

class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.running = True
        self.pc = 0
        self.fl = 0b00000000

    def alu(self, ir, reg_a, reg_b):
        if ir == "CMP":
            self.fl &= 0b00000000
            if self.reg[reg_a] == self.reg[reg_b]:
                self.fl = 0b00000001
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.fl = 0b00000100
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.fl = 0b00000010
            self.pc += 3

    def ldi(self, address, value):
        self.reg[address] = value
        self.pc += 3

    