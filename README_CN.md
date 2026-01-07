[![PyPI version](https://badge.fury.io/py/beam-clipboard.svg)](https://pypi.org/project/beam-clipboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Beam - 跨设备剪贴板

[English](README.md)

通过云端 API 实现快速跨设备文本共享的命令行工具。

**只需两个命令: `bm c` (复制) 和 `bm p` (粘贴)**

## 快速开始

```bash
# 安装
pip install beam-clipboard

# 首次使用: 设置个人 key
bm c "hello world"
# 提示: No key configured. Please enter your personal key:
# 输入你的 key (建议 20+ 字符)

# 日常使用
bm c "复制这个"    # 复制到云端
bm p              # 从云端粘贴
```

## 特性

- ✨ **极简** - 只需 `bm c` 和 `bm p` 两个命令
- 🚀 **零配置** - 首次使用自动设置
- 🔄 **跨设备** - Mac, Linux, Windows, iPhone 浏览器
- 📦 **纯 Python** - 无额外依赖
- 🔓 **开源** - MIT License

## 使用方法

### 复制和粘贴

```bash
# 复制文本
bm c "hello world"

# 从 stdin 复制
echo "hello" | bm c
pbpaste | bm c  # 从剪贴板复制

# 粘贴文本
bm p
```

### 修改 Key

```bash
# 交互式修改
bm e

# 直接设置新 key
bm e mynewkey
```

### 其他使用方式

```bash
python -m beam c "hello world"
python -m beam p
```

## 使用场景

### 💻 电脑间同步

```bash
# 电脑 A
bm c "some data"

# 电脑 B
bm p
```

### 📱 Mac 复制到 iPhone

```bash
# 在 Mac 上
pbpaste | bm c

# 在 iPhone 浏览器访问
# https://textdb.online/你的key
```

## API 说明

基于 TextDB.online 服务:

- **创建/更新**: `https://api.textdb.online/update/?key={key}&value={text}`
- **读取**: `https://textdb.online/{key}`
- **删除**: `https://api.textdb.online/update/?key={key}&value=`

Key 要求:
- 长度: 6-60 字符
- 不能包含斜杠 (/)
- 建议 20+ 字符以保证安全性

## 配置文件

配置保存在: `~/.config/beam/config.json`

```json
{
  "key": "your_personal_key"
}
```

## 依赖

- Python 3.6+

## 贡献

欢迎贡献! 你可以:
- 🐛 报告 bug
- 💡 提出新功能建议
- 🔧 提交 pull request

## 许可证

MIT License

## 作者

[vw2x](https://github.com/vw2x)

---

**如果觉得有用, 请给个 Star ⭐**
