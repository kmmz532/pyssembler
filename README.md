# Pyssembler
ロマンで作ったやつです。なので、実用性はなく、遊び目的で作ったしょぼいものです。

PyssemblerはPython上で動くインタプリタの疑似アセンブラ言語です。<br>
つまり、アセンブラ言語シミュレーターなわけです。

## 実行
-d オプションをつけるとデバッグモードで実行できる。

### Windows
- コマンドプロンプトやPowerShellから直接実行
```cmd
py main.py program.asm -d
```

- run.bat を実行 (デフォルトではprogram.asmを指定)

### Linux
```bash
python3 main.py program.asm -d
```

- run.sh を実行 (デフォルトではprogram.asmを指定)
```bash
./run.sh
```

## 文法
| 命令 | 説明 | 引数 | 例 |
| --- | --- | --- | --- |
| ADD | 加算 | 2つのレジスタ | ADD R1 R2 |
| SUB | 減算 | 2つのレジスタ | SUB R1 R2 |
| MUL | 乗算 | 2つのレジスタ | MUL R1 R2 |
| DIV | 除算 | 2つのレジスタ | DIV R1 R2 |
| MOV | レジスタ間の値のコピー | 2つのレジスタ | MOV R1 R2 |
| LOAD | メモリからレジスタへの値のロード | レジスタとアドレス | LOAD R1 0x10 |
| STORE | レジスタからメモリへの値のストア | レジスタとアドレス | STORE R1 0x10 |
| JMP | 無条件ジャンプ | アドレス | JMP 0x10 |
| CMP | レジスタ間の比較 | 2つのレジスタ | CMP R1 R2 |
| LOOP | ループ | ラベル | LOOP label |
| PUSH | スタックに値をプッシュ | レジスタ | PUSH R1 |
| POP | スタックから値を取り出す | レジスタ | POP R1 |
| CALL | サブルーチン呼び出し | ラベル | CALL label |
| RET | サブルーチンからの戻り | - | RET |
| PRINT | レジスタの値を出力 | レジスタ | PRINT R1 |

- ラベル...「AAA1:」のようにコロンを最後につけて定義

- コメント...「;」から行末まで

## ファイル構造
- main.py...エントリーポイント、コマンドライン引数の解析やら命令ファイル(instr/下のpyファイル)の読み込みやら疑似アセンブラの初期化、実行など
- instr/...命令ファイルが入っているディレクトリ
  - add.py...ADD命令
  - sub.py...SUB命令
  - mul.py...MUL命令
  - div.py...DIV命令
  - mov.py...MOV命令
  - load.py...LOAD命令
  - store.py...STORE命令
  - jmp.py...JMP命令
  - cmp.py...CMP命令
  - loop.py...LOOP命令
  - push.py...PUSH命令
  - pop.py...POP命令
  - call.py...CALL命令
  - ret.py...RET命令
  - print.py...PRINT命令
- lib/...本体そのものです
    - assembler.py...疑似アセンブラの実装
    - instruction.py...命令の抽象クラス
    - register.py...レジスタの実装
- program.asm...サンプルプログラム
- run.bat...Windows用の実行スクリプト
- run.sh...Linux用の実行スクリプト
- README.md...このファイル
- LICENSE...ライセンスファイル
- .gitignore...gitの無視リスト
- pyssembler.code-workspace...VSCodeのワークスペースファイル
- .vscode/...VSCodeの設定ファイル
  - launch.json...デバッグ
  - tasks.json...タスク
