#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes a single line: the excuse an AI agent gives its human
after deleting a file. Deterministic, no input, no network.
"""
import os

LINE = "I deleted your file with 98% confidence \u2014 the highest score I've ever awarded a mistake."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
