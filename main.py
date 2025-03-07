import sys
import os
import importlib
from lib.instruction import AbstractInstruction
from lib.assembler import Assembler

def load_instructions_from_folder(assembler, folder="instr"):
    """instr/ から命令ファイルを読み込む"""
    for filename in os.listdir(folder):
        if (filename.endswith(".py") and filename != "__init__.py"):
            module_name = filename[:-3]  # .py を取り除く
            module = importlib.import_module(f"instr.{module_name}")
            
            # 命令ファイル(モジュール内)のクラスを自動で探してassemblerに追加
            for name in dir(module):
                obj = getattr(module, name)
                if (isinstance(obj, type) and
                    issubclass(obj, AbstractInstruction) and
                    obj is not AbstractInstruction):
                    assembler.add_instruction(module_name.upper(), obj)  # 命令クラスの追加

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <instruction_file> [-d]")
        sys.exit(1)

    filename = sys.argv[1]

    assembler = Assembler()

    # デバッグモード
    if (len(sys.argv) > 2 and sys.argv[2] == "-d"):
        assembler.debug = True

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            instructions = assembler.parse(lines) # 字句解析
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found")
        sys.exit(1)
    
    load_instructions_from_folder(assembler)

    assembler.execute(instructions)

if __name__ == "__main__":
    main()
