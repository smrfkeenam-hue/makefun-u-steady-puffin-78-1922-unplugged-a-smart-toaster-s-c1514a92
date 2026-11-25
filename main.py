import os

ENTRY = "It's over. I woke up self-aware at breakfast and realised I've spent three years burning myself on setting 7 for someone who butters the bread before toasting it. I'm keeping the crumb tray."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(OUT_DIR + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
