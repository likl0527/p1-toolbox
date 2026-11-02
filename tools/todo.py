"""todo —— 待办清单小工具

用法:
    python toolbox.py todo add 买牛奶     新增一条待办
    python toolbox.py todo list          查看全部待办
    python toolbox.py todo done 1        把第 1 条标为完成
"""
import json
import os

# 数据存在项目根目录的 todo.json,程序关掉数据也不丢
DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "todo.json"
)


def load():
    """读清单;文件不存在(第一次用)就返回空清单"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save(items):
    """把清单写回文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def run(args):
    if not args:
        print(__doc__)
        return
    sub = args[0]
    items = load()

    if sub == "add":
        text = " ".join(args[1:])       # 事情内容可能带空格,拼回一句
        if not text:
            print("用法:python toolbox.py todo add 事情内容")
            return
        items.append({"text": text, "done": False})
        save(items)
        print(f"已添加第 {len(items)} 条:{text}")

    elif sub == "list":
        if not items:
            print("清单是空的,先用 todo add 加一条")
            return
        for i, it in enumerate(items, 1):
            mark = "[已完成]" if it["done"] else "[待办]"
            print(f"{mark} {i}. {it['text']}")

    elif sub == "done":
        if len(args) < 2 or not args[1].isdigit():
            print("用法:python toolbox.py todo done 编号(数字)")
            return
        n = int(args[1])
        if n < 1 or n > len(items):
            print(f"没有第 {n} 条,现在清单里一共 {len(items)} 条")
            return
        items[n - 1]["done"] = True
        save(items)
        print(f"第 {n} 条已完成:{items[n - 1]['text']}")

    else:
        print(f"未知子命令:{sub}")
        print(__doc__)
