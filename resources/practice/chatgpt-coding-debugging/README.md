# 排查代码报错｜练习包

[完整教程](../../../docs/chatgpt-coding-debugging.md) · [全部练习](../../README.md)

材料均为原创虚构练习。先阅读教程，再按顺序使用输入与提示词；代码只在自己确认的本地练习目录运行。

## 先怎样使用

01-reference.py是故意保留的出错例子；03-reference.py是修复后函数。02说明预期，04要求检查；调用修复函数时依次试[]、[0]、[80,100]、[5]。

| 文件 | 用途 |
|---|---|
| [01-reference.py](01-reference.py) | 从正文完整提取的输入、提示词或参考代码 |
| [02-prompt-or-input.txt](02-prompt-or-input.txt) | 从正文完整提取的输入、提示词或参考代码 |
| [03-reference.py](03-reference.py) | 从正文完整提取的输入、提示词或参考代码 |
| [04-prompt-or-input.txt](04-prompt-or-input.txt) | 从正文完整提取的输入、提示词或参考代码 |
| [expected-result.md](expected-result.md) | 参考答案与检查重点 |

## 完成后检查

原始空列表触发ZeroDivisionError；修复后[]返回None、[0]返回0、[80,100]返回90、[5]返回5。

GitHub文件页可以使用Raw或下载入口；也可在资源总页下载合集。
