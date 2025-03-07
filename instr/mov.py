from lib.instruction import AbstractInstruction

class MovInstruction(AbstractInstruction):
    def __init__(self, dest, src):
        self.dest = dest
        self.src = src

    def execute(self, assembler):
        """MOV命令の実行：レジスタ間 or 即値の代入"""
        
        value = None
        if self.src.isdigit():  # 数値なら即値として代入
            value = int(self.src)
        else:  # そうでなければレジスタからコピー
            value = assembler.get_register(self.src)
        assembler.set_register(self.dest, value)
        
        if assembler.debug:
            if self.src.isdigit():
                print(f"-> {self.dest} = {self.src}")
            else:
                print(f"-> {self.dest} = {self.src} = {value}")

    def __str__(self):
        return f"MOV {self.dest}, {self.src}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1], parts[2])
