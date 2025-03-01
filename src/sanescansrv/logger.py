"""Simple logging to both console and log files."""

# Programmed by CoolCat467

from __future__ import annotations

__title__ = "Logging"
__author__ = "CoolCat467"


import time
from os import makedirs, path

PROGRAM_TITLE: str = __title__


def set_title(title: str) -> None:
    """Set program title."""
    global PROGRAM_TITLE
    PROGRAM_TITLE = title


def log(message: str, level: int = 1, log_dir: str | None = None) -> None:
    """Log a message to console and log file."""
    levels = ["DEBUG", "INFO", "ERROR"]

    if log_dir is None:
        # log_dir = path.join(path.dirname(__file__), "logs")
        log_dir = path.abspath(
            path.expanduser(path.join("~", ".sanescansrv", "logs")),
        )
    if not path.exists(log_dir):
        makedirs(log_dir, exist_ok=True)
    filename = time.strftime("log_%Y_%m_%d.log")
    log_file = path.join(log_dir, filename)

    log_level = levels[min(max(0, level), len(levels) - 1)]
    log_time = time.asctime()
    log_message_text = message.encode("unicode_escape").decode("utf-8")

    log_msg = (
        f"[{PROGRAM_TITLE}] [{log_time}] [{log_level}] {log_message_text}"
    )

    if not path.exists(log_file):
        with open(log_file, mode="w", encoding="utf-8") as file:
            file.close()
    with open(log_file, mode="a", encoding="utf-8") as file:
        file.write(f"{log_msg}\n")
        file.close()
    print(log_msg)


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
