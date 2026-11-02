# P1 命令行工具箱

一个程序装 4 个实用小工具,终端敲一条命令就能用。

## 启动

需要 Python 3.8+(在 3.12 验证通过),**不用安装任何第三方库**,下载后直接:

```
python toolbox.py               查看全部用法
```

## 结构

`toolbox.py` 是统一入口,按第一个词(子命令)分发;`tools/` 下每个小工具一个文件,统一提供 `run(args)` 函数。加新工具 = 新建一个文件 + 在 `toolbox.py` 的 `TOOLS` 字典登记一行。

## 四个小工具

| 子命令 | 作用 | 示例 |
|---|---|---|
| `todo` | 待办清单(存在 todo.json,关了不丢) | `python toolbox.py todo add 买牛奶` |
| `ren` | 批量改名(**先预览,加 --yes 才真改**) | `python toolbox.py ren 照片 --prefix 2026-` |
| `stat` | 文本统计(行/字/字符;汉字一个算一个,英文一个词算一个) | `python toolbox.py stat 文章.txt` |
| `pwd` | 随机强密码(学员自设计的第 4 个工具,最短 8 位) | `python toolbox.py pwd 16` |

所有工具对坏输入(文件不存在、乱给参数、非法数字)给出中文提示,不崩溃。

## 作者

VibeCoding 培养系统 · L0 · P1 项目 · 学员与 AI 协作完成
