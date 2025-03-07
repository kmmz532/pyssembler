from lib.instruction import AbstractInstruction

class RetInstruction(AbstractInstruction):
    def execute(self, assembler):
        return_address = assembler.memory[assembler.get_register("RSP")]
        assembler.set_register("RSP", assembler.get_register("RSP") + 1)
        
        return return_address

    def __str__(self):
        return "RET"

    @classmethod
    def from_parts(cls, parts):
        return cls()
