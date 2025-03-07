class Register:
    DEFAULT_REGISTERS = {
        "RAX", "RBX", "RCX", "RDX", "RSI", "RDI", "RBP", "RSP", "RIP",
        "R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15"
    }

    def __init__(self, custom_registers=None):
        """指定されたレジスタのみを使用可能にする"""
        if custom_registers is None:
            custom_registers = self.DEFAULT_REGISTERS
        self.registers = {reg.upper(): 0 for reg in custom_registers}

    def get(self, register_name):
        """レジスタの値を取得"""
        reg = register_name.upper()
        if reg not in self.registers:
            raise ValueError(f"Invalid register: {register_name}")
        return self.registers[reg]

    def set(self, register_name, value):
        """レジスタに値を設定"""
        reg = register_name.upper()
        if reg not in self.registers:
            raise ValueError(f"Invalid register: {register_name}")
        self.registers[reg] = value

    def dump(self):
        """全レジスタの状態を表示"""
        return self.registers
