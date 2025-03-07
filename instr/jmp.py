from lib.instruction import AbstractInstruction

class JmpInstruction(AbstractInstruction):
    def __init__(self, label):
        self.label = label

    def execute(self, assembler):
        return assembler.labels.get(self.label)  # ラベルの位置にジャンプ

    def __str__(self):
        return f"JMP {self.label}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1])