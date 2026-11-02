"""stat —— 文本统计小工具

用法:
    python toolbox.py stat <文件路径>

数三样:行数、字数、字符数。
字数的规矩:汉字一个算一个,英文一个单词算一个。
"""
import os
import re


def run(args):
    # 第一步:检查参数,只要一个文件路径
    if len(args) != 1:
        print("用法:python toolbox.py stat <文件路径>")
        return
    path = args[0]

    # 第二步:文件得存在
    if not os.path.exists(path):
        print(f"文件不存在:{path}")
        return

    # 第三步:读内容。读到乱码(比如拿图片来数)就客气提示,不崩
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:
        print(f"这个文件好像不是文本文件(比如图片/压缩包),数不了:{path}")
        return

    # 第四步:数三样
    line_count = len(text.splitlines())
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))      # 汉字个数
    words = len(re.findall(r"[A-Za-z0-9]+", text))       # 英文单词个数
    char_count = len(text.replace("\n", "").replace(" ", "").replace("\t", ""))

    print(f"文件:{path}")
    print(f"  行数:{line_count} 行")
    print(f"  字数:{cjk + words} 字(汉字 {cjk} 个 + 英文词 {words} 个)")
    print(f"  字符数:{char_count}(不含空格和换行)")
