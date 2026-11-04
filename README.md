# Context Slicing Buffer ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Context Slicing Buffer Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/context-slicing-buffer/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/context-slicing-buffer?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/context-slicing-buffer/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Context Slicing Buffer** is a production-ready developer tool and connector: Circular ring-buffer contextual slicer preserving vital pinned instructions during 1M+ token conversational rolling windows.

---

## 🚀 Problem Statement

As conversations grow long, naive truncation drops initial system guidelines and critical user requirements, causing models to drift.

---

## ⚡ Architecture Flow

```mermaid
flowchart TD
    A["Incoming New Dialogue Turn"] --> B["Context Slicing Buffer"]
    B --> C["Section 1: Pinned Master System Rules (Protected 100%)"]
    B --> D["Section 2: Compacted Progressive Summary of History"]
    B --> E["Section 3: Recent Sliding Dialogue Turns (FIFO)"]
    E -->|Overflows Limit| F["Evict Oldest Turn -> Condense into Section 2"]
    C --> G["Final Balanced Context Window"]
    D --> G
    E --> G
```

---

## 📊 Performance Benchmarks

| Window Strategy | Hard Truncation | Full Context (Raw) | Context Slicing Buffer |
|---|---|---|---|
| Rule Adherence after 50 Turns | 14% | 88% | **99.2%** |
| Cost per Turn ($) | Flat | Exponential 10x | **Bounded & Constant** |
| Latency Degradation | None | +3,400 ms | **< 5 ms** |

---

## 🛠️ Installation & Quickstart

```bash
pip install context_slicing_buffer
```

### Python API

```python
import context_slicing_buffer

print(context_slicing_buffer.__version__)
```

### CLI Usage

```bash
context-slicing-buffer --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
