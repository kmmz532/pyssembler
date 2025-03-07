from lib.instruction import AbstractInstruction

class StoreInstruction(AbstractInstruction):
    def __init__(self, register, address):
        self.register = register
        self.address = address

    def execute(self, assembler):
        """レジスタからメモリにデータを保存する"""
        value = assembler.get_register(self.register)
        assembler.store_to_memory(self.address, value)
        
        if assembler.debug:
            print(f"-> {self.register} '{value}' to Address '{self.address}'")

    def __str__(self):
        return f"STORE {self.register}, {self.address}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1], int(parts[2]))
