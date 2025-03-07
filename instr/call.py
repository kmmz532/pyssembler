from lib.instruction import AbstractInstruction

class CallInstruction(AbstractInstruction):
    def __init__(self, label):
        self.label = label

    def execute(self, assembler):
        assembler.set_register("RSP", assembler.get_register("RSP") - 1)
        assembler.memory[assembler.get_register("RSP")] = assembler.pc + 1  # 戻りアドレス保存
        return assembler.labels.get(self.label)

    def __str__(self):
        return f"CALL {self.label}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1])
