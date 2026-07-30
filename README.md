# todo-cli

一个简单的命令行待办工具（学习用）。

## 功能
- 添加任务：`python3 main.py add "买牛奶"`
- 列出任务：`python3 main.py list`
- 标记完成：`python3 main.py done 1`
- 删除任务：`python3 main.py remove 1`

## 运行
1. 在项目目录（已激活虚拟环境）：`python3 main.py add "示例任务"`
2. 之后可通过 `list/done/remove` 操作。

## 说明
任务保存在本地的 `tasks.json`（已加入 .gitignore，不会提交）