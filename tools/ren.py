"""ren —— 批量改名小工具

用法:
    python toolbox.py ren <文件夹> --prefix 前缀          只看预览,不动任何文件
    python toolbox.py ren <文件夹> --prefix 前缀 --yes    真正执行改名

例:
    python toolbox.py ren 照片 --prefix 2026-
    把"照片"文件夹里的文件都改名为 2026-原文件名
"""
import os


def run(args):
    # 第一步:把参数拆开——文件夹在哪、加什么前缀、有没有带 --yes
    folder = None
    prefix = ""
    do_it = False
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--prefix":
            if i + 1 < len(args):
                prefix = args[i + 1]
                i += 1
            else:
                print("--prefix 后面要跟前缀内容,例如 --prefix 2026-")
                return
        elif a == "--yes":
            do_it = True
        elif folder is None:
            folder = a
        else:
            print(f"不认识的参数:{a}")
            print(__doc__)
            return
        i += 1

    # 第二步:检查参数和文件夹
    if folder is None:
        print("用法:python toolbox.py ren <文件夹> --prefix 前缀 [--yes]")
        print("先不带 --yes 看预览,确认没问题再加 --yes 真正执行")
        return
    if not prefix:
        print("必须用 --prefix 指定前缀,例如 --prefix 2026-")
        return
    if not os.path.isdir(folder):
        print(f"文件夹不存在:{folder}")
        return

    # 第三步:列出文件夹里的文件(只要文件,不碰里面的子文件夹)
    names = [n for n in os.listdir(folder) if os.path.isfile(os.path.join(folder, n))]
    if not names:
        print(f"文件夹 {folder} 里没有文件")
        return

    # 算新名字;已经带前缀的跳过,避免改成 2026-2026-xxx
    plan = []
    skipped = 0
    for n in names:
        if n.startswith(prefix):
            skipped += 1
        else:
            plan.append((n, prefix + n))

    if skipped:
        print(f"跳过 {skipped} 个已经带前缀的文件")
    if not plan:
        print("没有需要改名的文件")
        return

    # 第四步:安全锁——没带 --yes 只出预览单,一个文件都不动
    if not do_it:
        print(f"预览:将把 {folder} 里的 {len(plan)} 个文件改名(现在只是预览,没动任何文件):")
        for old, new in plan:
            print(f"  {old}  →  {new}")
        print("确认没问题后,在命令最后加上 --yes 再跑一遍,才会真正改名")
        return

    # 第五步:带了 --yes,真改
    for old, new in plan:
        os.rename(os.path.join(folder, old), os.path.join(folder, new))
        print(f"  已改名:{old}  →  {new}")
    print(f"完成,共改名 {len(plan)} 个文件")
