<div align="center">
  <img src="assets/logo.svg" width="200" height="200" alt="Beam Logo">
  
  # Beam
  
  **跨设备剪贴板.**
  
  [![PyPI version](https://badge.fury.io/py/beam-clipboard.svg)](https://pypi.org/project/beam-clipboard/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  
  [English](README.md)
  
  通过云端 API 实现快速跨设备文本共享的命令行工具。
  
  **只需两个命令: `bm c` (复制) 和 `bm p` (粘贴)**
</div>

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
- 🔐 **加密** - 上传前加密内容
- 🗜️ **压缩** - 减少传输大小 (代码可压缩约 60%)
- 🔓 **开源** - MIT License

## 使用方法

### 复制和粘贴

```bash
# 复制文本
bm c "hello world"

# 从 stdin 复制
echo "hello" | bm c
pbpaste | bm c  # 从剪贴板复制

# 明文模式 (用于移动设备浏览器查看)
bm c --plain "hello world"

# 粘贴文本
bm p
```

### 修改 Key 和密码

```bash
# 交互式修改 (key + 密码)
bm e

# 直接设置新 key
bm e mynewkey

# 设置加密密码
bm e -p mypassword
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

### 📱 电脑与移动设备互传

**电脑到手机 (浏览器查看)**

```bash
# 在电脑上
bm c --plain "hello world"

# 在手机浏览器访问
# https://textdb.online/你的key
```

**手机到电脑 (浏览器输入)**

```bash
# 在手机浏览器访问
# https://textdb.online/你的key
# 直接输入文本

# 在电脑上
bm p
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
  "key": "your_personal_key",
  "password": "your_encryption_password"
}
```

- `key`: 你在 TextDB API 使用的个人 key
- `password`: 加密密码 (默认: `123456`)

## 安全性

所有内容在上传前都会先**压缩** (zlib) 再**加密** (XOR + SHA256):

```
你的文本 → 压缩 → 加密 → Base64 → 上传
```

服务器只能看到类似 `BM2:xxxxx...` 的加密数据, 无法读取你的内容。

使用 `--plain` 选项可以跳过压缩和加密, 适用于需要在移动设备浏览器中查看的非敏感内容。

> ⚠️ 这是为便利性设计的轻量级加密, 不适用于高度敏感数据。

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
