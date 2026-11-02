"""P1 命令行工具箱 —— 统一入口

用法:
    python toolbox.py               查看全部用法
    python toolbox.py todo ...      待办清单
    python toolbox.py ren ...       批量改名
    python toolbox.py stat ...      文本统计
    python toolbox.py pwd 位数      随机密码(学员自设计的第4个工具)
"""
import sys

from tools import pwd, ren, stat, todo

# 子命令名 -> 对应工具模块。以后加新工具:写个新文件,在这里登记一行
TOOLS = {
    "todo": todo,
    "ren": ren,
    "stat": stat,
    "pwd": pwd,
}


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    name = sys.argv[1]          # 第一个词是子命令名,比如 todo
    tool = TOOLS.get(name)
    if tool is None:
        print(f"未知命令:{name}")
        print("运行 python toolbox.py 查看用法")
        return
    tool.run(sys.argv[2:])      # 子命令后面的参数原样交给工具


if __name__ == "__main__":
    main()
