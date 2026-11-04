"""Context slicing ring buffer with pinned system prompt."""
from typing import List, Dict, Any


class ContextSlicingBuffer:
    def __init__(self, pinned_system_prompt: str, max_turns: int = 5):
        self.pinned = pinned_system_prompt
        self.max_turns = max_turns
        self._turns: List[Dict[str, str]] = []
        self._evicted_count = 0

    def add_turn(self, role: str, content: str):
        self._turns.append({"role": role, "content": content})
        if len(self._turns) > self.max_turns:
            self._turns.pop(0)
            self._evicted_count += 1

    def build_prompt_sequence(self) -> List[Dict[str, str]]:
        seq = [{"role": "system", "content": self.pinned}]
        if self._evicted_count > 0:
            seq.append({"role": "system", "content": f"[Note: {self._evicted_count} earlier turns compacted]"})
        seq.extend(self._turns)
        return seq
