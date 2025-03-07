from lib.instruction import AbstractInstruction

class CmpInstruction(AbstractInstruction):
    def __init__(self, reg1, reg2):
        self.reg1 = reg1
        self.reg2 = reg2

    def execute(self, assembler):
        val1 = assembler.get_register(self.reg1)
        val2 = assembler.get_register(self.reg2)
        assembler.flags["ZF"] = (val1 == val2)  # Zero Flag (等しいなら1)
        assembler.flags["SF"] = (val1 < val2)   # Sign Flag (val1が小さいなら1)

        if assembler.debug:
            if (val1 == val2):
                print("-> {val1} == {val2} -> ZF = 1")
            else:
                print("-> {val1} != {val2} -> ZF = 0")
            if (val1 < val2):
                print("-> {val1} < {val2} -> SF = 1")
            else:
                print("-> {val1} >= {val2} -> SF = 0")

    def __str__(self):
        return f"CMP {self.reg1}, {self.reg2}"

    @classmethod
    def from_parts(cls, parts):
        return cls(parts[1], parts[2])
