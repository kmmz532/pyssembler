from lib.instruction import AbstractInstruction

class SubInstruction(AbstractInstruction):
    def __init__(self, register1, register2):
        self.register1 = register1
        self.register2 = register2

    def execute(self, assembler):
        a = assembler.get_register(self.register1)
        b = assembler.get_register(self.register2)
        result = a - b
        assembler.set_register(self.register1, result)
        
        if assembler.debug:
            print(f"-> {self.register1} = {self.register1} - {self.register2} = {a} - {b} = {result}")

    def __str__(self):
        return f"SUB {self.register1}, {self.register2}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1], parts[2])
