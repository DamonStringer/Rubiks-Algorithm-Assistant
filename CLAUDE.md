# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python CLI tool for managing OLL/PLL Rubik's Cube algorithms with a JSON backend. This is also a deliberate "Shadow Curriculum" — a learning log where each version intentionally captures bugs, refactors, and architectural decisions. Preserve that spirit: don't silently hide mistakes or over-engineer.

## Running the App

```bash
python ca_v0.41
```

No dependencies beyond the Python standard library (`json` module only). No build step, no package manager, no virtual environment needed.

**Available commands at runtime:** `list`, `add`, `scramble`, `exit`, or an OLL case name directly.

## Architecture

Two classes in `ca_v0.41`:

- **`AlgorithmLibrary`** — data model and persistence. Loads `algs.json` on init; falls back to `default_algs.json` if missing. Saves back to `algs.json` on `exit` or after `add`.
- **`CubeAssistant`** — the UI loop. Owns an `AlgorithmLibrary` instance and routes user input via `run()`.

**Data files:**
- `default_algs.json` — committed seed template with 8 OLL + 6 PLL cases. Never contains user data.
- `algs.json` — live user database; gitignored to prevent personal data leaks and Git conflicts.

## Known Control Flow Issue (V0.41)

There is an unreachable code bug in `ca_v0.41`. After the `if/elif/else` block (lines 49–84), the OLL lookup (lines 87–99) runs unconditionally on every loop iteration — including after `list`, `add`, `scramble`, and invalid commands. The `else` on line 83 catches all non-command inputs, so the intended OLL case lookup flow (lines 87–99) is never reached from a genuine OLL case name entry. This is a known architectural issue documented as part of the project's learning log.

## Roadmap Context

- **Phase 3 (next):** GUI transition using Tkinter or Kivy
- **Phase 4:** Package as `.exe` and `.apk` for desktop and Android

When adding features, keep the engine (AlgorithmLibrary) decoupled from the interface layer (CubeAssistant) so the GUI phase can swap in a new UI without rewriting logic.

## Versions Archive

`versions/` holds snapshots of each major version (v0.1–v0.41). These are historical records, not active code. Don't modify them.
