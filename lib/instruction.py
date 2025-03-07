# 命令 (詳しくはinstr/の各命令ファイルを参照すること)
class AbstractInstruction:
    def execute(self, assembler):
        """実行処理"""
        raise NotImplementedError("SubClass is not implemented this method.")

    @classmethod
    def from_parts(cls, parts):
        """引数から命令オブジェクトを作成"""
        raise NotImplementedError("SubClass is not implemented this method.")
