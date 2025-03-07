from lib.instruction import AbstractInstruction

class LoadInstruction(AbstractInstruction):
    def __init__(self, register, address):
        self.register = register
        self.address = address

    def execute(self, assembler):
        """メモリからレジスタにデータを読み込む"""
        value = assembler.load_from_memory(self.address)
        assembler.set_register(self.register, value)

        if assembler.debug:
            print(f"-> {self.register} = {value} from Address '{self.address}'")

    def __str__(self):
        return f"LOAD {self.register}, {self.address}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1], int(parts[2]))
