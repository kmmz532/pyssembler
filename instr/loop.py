from lib.instruction import AbstractInstruction

class LoopInstruction(AbstractInstruction):
    def __init__(self, label):
        self.label = label  # ジャンプ先ラベル
        self.count = -1
        self.total = -1

    def execute(self, assembler):
        count = assembler.get_register("RCX")
        self.count = count
        
        if self.total == -1:
            self.total = count
        
        if count > 1:
            count -= 1
            assembler.set_register("RCX", count)  # RCX をデクリメント
            if assembler.debug:
                print(f"-> RCX = {count}")
            return assembler.labels.get(self.label)  # ラベルの位置にジャンプ
        
        return None  # ループ終了

    def __str__(self):
        #count = self.total - self.count + 1
        #return f"LOOPED {self.label} [{count}]"
        return f"LOOP {self.label}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1])
