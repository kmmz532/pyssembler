from lib.instruction import AbstractInstruction

class PopInstruction(AbstractInstruction):
    def __init__(self, register):
        self.register = register

    def execute(self, assembler):
        value = assembler.pop()
        assembler.registers.set(self.register, value)

        if assembler.debug:
            print(f"-> {self.register} = {value} from stack")

    def __str__(self):
        return f"POP {self.register}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1])
