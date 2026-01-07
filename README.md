[![PyPI version](https://badge.fury.io/py/beam-clipboard.svg)](https://pypi.org/project/beam-clipboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Beam - Cross-device Clipboard

[中文文档](README_CN.md)

Command-line tool for cross-device text sharing via cloud API.

**Just 2 commands: `bm c` (copy) and `bm p` (paste)**

## Quick Start

```bash
# Install
pip install beam-clipboard

# First time: set your personal key
bm c "hello world"
# Prompt: No key configured. Please enter your personal key:
# Enter your key (recommend 20+ characters)

# Daily use
bm c "copy this"    # copy to cloud
bm p                # paste from cloud
```

## Features

- ✨ **Minimalist** - Just `bm c` and `bm p`
- 🚀 **Zero config** - Auto setup on first use
- 🔄 **Cross-device** - Mac, Linux, Windows, iPhone browser
- 📦 **Pure Python** - No external dependencies
- 🔓 **Open source** - MIT License

## Usage

### Copy & Paste

```bash
# Copy text
bm c "hello world"

# Copy from stdin
echo "hello" | bm c
pbpaste | bm c  # from clipboard

# Paste text
bm p
```

### Edit Key

```bash
# Interactive edit
bm e

# Set new key directly
bm e mynewkey
```

### Alternative Usage

```bash
python -m beam c "hello world"
python -m beam p
```

## Use Cases

### 💻 Sync Between Computers

```bash
# computer A
bm c "some data"

# computer B
bm p
```

### 📱 Mac to iPhone Transfer

```bash
# on Mac
pbpaste | bm c

# on iPhone browser
# visit: https://textdb.online/yourkey
```

## API Details

Based on TextDB.online service:

- **Create/Update**: `https://api.textdb.online/update/?key={key}&value={text}`
- **Read**: `https://textdb.online/{key}`
- **Delete**: `https://api.textdb.online/update/?key={key}&value=`

Key requirements:
- Length: 6-60 characters
- No slashes (/)
- Recommend 20+ chars for security

## Configuration

Config file location: `~/.config/beam/config.json`

```json
{
  "key": "your_personal_key"
}
```

## Requirements

- Python 3.6+

## Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## License

MIT License

## Author

[vw2x](https://github.com/vw2x)

---

**Star ⭐ this repo if you find it useful!**
