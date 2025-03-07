import re
from lib.instruction import AbstractInstruction
from instr.loop import LoopInstruction
from lib.register import Register

class Assembler:
    def __init__(self, pc = -1):
        self.instructions = {} # 命令
        self.registers = Register() # レジスタ
        self.memory = {} # メモリ
        self.labels = {} # ラベル
        self.loop_instruction = None  # LOOP命令を格納するための変数
        
        self.registers.set("R13", 0x1000) # スタックポインタ
        self.stack_base = 0x1000 # スタックベース

        self.pc = pc
        self.debug = False

    def parse(self, lines):
        """字句解析"""
        instructions = []
        for i, line in enumerate(lines):
            line = line.strip() # 前後の空白や改行を取り除く

            if not line or line.startswith(";"): # 空行 or コメント行ならスキップ
                continue

            # _startラベルを見つけたらプログラムカウンタをその行に設定
            if "_start:" in line:
                self.pc = i - 1

            parts = re.split(r'[,\s]+', line) # 例: ["ADD", "R1", "R2"] みたいな感じに命令を分割
            instructions.append(parts) # 命令リストに追加
    
        return instructions

    def add_instruction(self, name, instruction_cls):
        """命令の追加"""
        self.instructions[name] = instruction_cls

    def execute(self, instructions):
        """命令リストを実行"""
        if (self.pc < 0):
            self.pc = 0

        pc = self.pc

        # ラベルの記録
        self.register_labels(instructions)
        
        # 命令の処理
        while pc < len(instructions):
            parts = instructions[pc]
            command = parts[0].upper()
            
            if command.endswith(":"):
                pc += 1
                continue
            
            if command in self.instructions:
                instruction = self.instructions[command].from_parts(parts)
                
                # LOOP命令は同じインスタンスを繰り返し使用
                if isinstance(instruction, LoopInstruction):
                    if self.loop_instruction is None:
                        self.loop_instruction = instruction  # 初回のみ新しく作成
                    res = self.loop_instruction.execute(self)
                    if self.debug:
                        print(f"exec: {self.loop_instruction}")
                    
                    if res is not None:
                        pc = res  # LOOP命令でラベルに飛ぶ
                    else:
                        self.loop_instruction = None  # ループ終了時にはリセット
                        pc += 1
                else:
                    if self.debug:
                        print(f"exec: {instruction}")
                    res = instruction.execute(self)
                    if res is not None:
                        pc = res  # 他の命令もラベルに飛ぶ
                    else:
                        pc += 1
            else:
                print(f"Unknown instruction: {command}")
                pc += 1

    def register_labels(self, instructions):
        """ラベルの記録"""
        for i, parts in enumerate(instructions):
            if parts[0].endswith(":"):  # ラベル定義
                label = parts[0][:-1]
                self.labels[label] = i

    def get_register(self, register_name):
        """レジスタの値を取得"""
        return self.registers.get(register_name)

    def set_register(self, register_name, value):
        """レジスタに値をセット"""
        self.registers.set(register_name, value)

    def load_from_memory(self, address):
        """指定されたメモリアドレスから値をロード"""
        return self.memory.get(address, 0)

    def store_to_memory(self, address, value):
        """指定されたメモリアドレスに値をストア"""
        self.memory[address] = value

    def push(self, value):
        """スタックに値をプッシュ"""
        sp = self.registers.get("R13")  # スタックポインタ
        sp -= 1
        self.memory[sp] = value
        self.registers.set("R13", sp)

    def pop(self):
        """スタックから値をポップ"""
        sp = self.registers.get("R13")  # スタックポインタ
        value = self.memory.get(sp, 0)
        sp += 1
        self.registers.set("R13", sp)
        return value