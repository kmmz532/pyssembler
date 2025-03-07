from lib.instruction import AbstractInstruction

class PushInstruction(AbstractInstruction):
    def __init__(self, register):
        self.register = register

    def execute(self, assembler):
        value = assembler.registers.get(self.register)
        assembler.push(value)

        if assembler.debug:
            print(f"-> {value} to stack")

    def __str__(self):
        return f"PUSH {self.register}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1])
