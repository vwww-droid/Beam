#!/usr/bin/env python3

import sys
import json
import argparse
from pathlib import Path
from urllib import request, parse

from . import __version__


API_BASE = "https://api.textdb.online"
READ_BASE = "https://textdb.online"
CONFIG_DIR = Path.home() / ".config" / "beam"
CONFIG_FILE = CONFIG_DIR / "config.json"


def init_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config():
    if not CONFIG_FILE.exists():
        return {}
    
    with CONFIG_FILE.open("r") as f:
        return json.load(f)


def save_config(config):
    with CONFIG_FILE.open("w") as f:
        json.dump(config, f, indent=2)


def get_or_set_key():
    config = load_config()
    
    if "key" in config:
        return config["key"]
    
    print("No key configured. Please enter your personal key:")
    print("(Recommend 20+ characters for security)")
    key = input("Key: ").strip()
    
    if len(key) < 6 or len(key) > 60:
        print("Error: key must be 6-60 characters", file=sys.stderr)
        sys.exit(1)
    
    if "/" in key:
        print("Error: key cannot contain '/'", file=sys.stderr)
        sys.exit(1)
    
    config["key"] = key
    save_config(config)
    print(f"✓ Key saved: {key}")
    print(f"Access URL: {READ_BASE}/{key}")
    
    return key


def api_update(key, value):
    encoded_value = parse.quote(value)
    url = f"{API_BASE}/update/?key={key}&value={encoded_value}"
    
    with request.urlopen(url) as response:
        return json.loads(response.read().decode())


def api_read(key):
    url = f"{READ_BASE}/{key}"
    
    try:
        with request.urlopen(url) as response:
            if response.status == 200:
                return response.read().decode()
    except Exception:
        return None


def api_delete(key):
    url = f"{API_BASE}/update/?key={key}&value="
    
    with request.urlopen(url) as response:
        return json.loads(response.read().decode())


def cmd_copy(args):
    key = get_or_set_key()
    text = args.text
    
    # read from stdin if no text
    if not text and not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    
    if not text:
        print("Error: no text to copy", file=sys.stderr)
        sys.exit(1)
    
    response = api_update(key, text)
    
    if response.get('status') == 1:
        print(f"✓ Copied to cloud")
        print(f"Access URL: {READ_BASE}/{key}")
    else:
        print("Error: failed to copy", file=sys.stderr)
        sys.exit(1)


def cmd_paste(args):
    key = get_or_set_key()
    content = api_read(key)
    
    if content is None:
        print("Error: no content found", file=sys.stderr)
        sys.exit(1)
    
    print(content, end='')


def cmd_delete(args):
    key = get_or_set_key()
    response = api_delete(key)
    
    if response.get('status') == 1:
        print(f"✓ Deleted cloud content")
    else:
        print("Error: failed to delete", file=sys.stderr)
        sys.exit(1)


def cmd_edit(args):
    config = load_config()
    
    if args.key:
        key = args.key
    else:
        current_key = config.get("key", "")
        print(f"Current key: {current_key}" if current_key else "No key configured")
        print("\nEnter new key (or press Enter to keep current):")
        key = input("Key: ").strip()
        
        if not key:
            if current_key:
                print("Key unchanged")
                return
            else:
                print("Error: no key provided", file=sys.stderr)
                sys.exit(1)
    
    if len(key) < 6 or len(key) > 60:
        print("Error: key must be 6-60 characters", file=sys.stderr)
        sys.exit(1)
    
    if "/" in key:
        print("Error: key cannot contain '/'", file=sys.stderr)
        sys.exit(1)
    
    config["key"] = key
    save_config(config)
    print(f"✓ Key updated: {key}")
    print(f"Access URL: {READ_BASE}/{key}")


def main():
    init_config()
    
    parser = argparse.ArgumentParser(
        prog="bm",
        description="Beam - Cross-device clipboard tool"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='commands')
    
    # copy
    parser_copy = subparsers.add_parser('c', aliases=['copy'], help='Copy text to cloud')
    parser_copy.add_argument('text', nargs='?', help='Text to copy')
    parser_copy.set_defaults(func=cmd_copy)
    
    # paste
    parser_paste = subparsers.add_parser('p', aliases=['paste'], help='Paste text from cloud')
    parser_paste.set_defaults(func=cmd_paste)
    
    # delete
    parser_delete = subparsers.add_parser('d', aliases=['delete'], help='Delete cloud content')
    parser_delete.set_defaults(func=cmd_delete)
    
    # edit
    parser_edit = subparsers.add_parser('e', aliases=['edit'], help='Edit personal key')
    parser_edit.add_argument('key', nargs='?', help='New key to set')
    parser_edit.set_defaults(func=cmd_edit)
    
    # version
    parser.add_argument('-v', '--version', action='version', version=f'beam v{__version__}')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
