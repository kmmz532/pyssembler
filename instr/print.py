from lib.instruction import AbstractInstruction

class PrintInstruction(AbstractInstruction):
    def __init__(self, value):
        self.value = value

    def execute(self, assembler):
        if self.value.startswith('"') and self.value.endswith('"'):
            print(self.value[1:-1])  # 文字列を出力
        else:
            print(assembler.get_register(self.value))  # レジスタの値を出力

    def __str__(self):
        return f"PRINT {self.value}"

    @classmethod
    def from_parts(cls, parts):
        return cls(" ".join(parts[1:]))  # 文字列の場合は複数の単語も考慮
