"""CLI for context-slicing-buffer."""
import sys
import argparse
from .buffer import ContextSlicingBuffer


def main():
    parser = argparse.ArgumentParser(description="Context Slicing Buffer")
    parser.add_argument("--demo", action="store_true", help="Run buffer demo")
    args = parser.parse_args()

    buf = ContextSlicingBuffer("System: You are an expert engineer.", max_turns=3)
    buf.add_turn("user", "Hello")
    buf.add_turn("assistant", "Hi there")
    buf.add_turn("user", "Write code")
    buf.add_turn("assistant", "Code written")
    buf.add_turn("user", "Now run it")
    print(buf.build_prompt_sequence())
    sys.exit(0)


if __name__ == "__main__":
    main()
