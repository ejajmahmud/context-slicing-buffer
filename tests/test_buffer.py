"""Tests for context-slicing-buffer."""
import unittest
from context_slicing_buffer.buffer import ContextSlicingBuffer


class TestContextSlicingBuffer(unittest.TestCase):
    def setUp(self):
        self.buf = ContextSlicingBuffer("System instructions", max_turns=2)

    def test_pinned_preservation_and_eviction(self):
        self.buf.add_turn("user", "Turn 1")
        self.buf.add_turn("assistant", "Turn 2")
        self.buf.add_turn("user", "Turn 3")
        prompt = self.buf.build_prompt_sequence()
        # Pinned system prompt must always be at index 0
        self.assertEqual(prompt[0]["role"], "system")
        self.assertEqual(prompt[0]["content"], "System instructions")
        # Only 2 turns + 1 eviction notice + 1 pinned system prompt = 4 items
        self.assertEqual(len(prompt), 4)


if __name__ == "__main__":
    unittest.main()
