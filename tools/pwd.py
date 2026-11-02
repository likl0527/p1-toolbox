"""pwd —— 随机密码生成器(学员自设计的第 4 个工具)

需求原文:"我要密码工具:我输入位数(比如 12),它输出一个 12 位的随机强密码"

用法:
    python toolbox.py pwd 16      生成一个 16 位的随机强密码
    python toolbox.py pwd         不给位数就默认 16 位
"""
import random
import string

# 字符池:大写、小写、数字、符号,四类都备齐
POOL = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*-_=+"


def run(args):
    # 第一步:要几位?没说就默认 16
    if not args:
        n = 16
    else:
        s = args[0]
        if not s.isdigit():
            print(f"位数得是数字,你给的是:{s}")
            return
        n = int(s)
        if n < 8:
            print("太短了,至少 8 位才安全,换个大点的数再来")
            return
        if n > 64:
            print("太长了,最多 64 位")
            return

    # 第二步:从字符池里随机摸 n 次,摸一个记一个
    chars = []
    for _ in range(n):
        chars.append(random.choice(POOL))

    # 第三步:拼成一串,吐出来
    password = "".join(chars)
    print(f"你的 {n} 位随机密码:{password}")
