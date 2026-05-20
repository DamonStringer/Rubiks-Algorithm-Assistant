🧊 Rubik's Algorithm Assistant
A command‑line Python tool for managing, searching, and persistently storing OLL/PLL algorithms using a structured JSON backend.

🎯 Purpose: A Living Engineering Log
This repository is more than a utility — it’s a living learning log. I’m using this project as a “Shadow Curriculum” to document my growth in Python, software architecture, and systems thinking.

Instead of pretending the first version is perfect, I’m intentionally building in public. Each iteration captures:

the bugs I break

the technical debt I clean

the concepts I learn

the architecture I refine

This project is both a tool and a record of my engineering progression.

🚀 Current Build — Version 0.1: Beta Architecture
This version replaces an earlier hot‑fixed prototype. V0.1 is a ground‑up rebuild focused on clarity, structure, and maintainability.

Key Features
Dynamic Data Routing  
The add function automatically routes user input into the correct nested dictionary (OLL or PLL) based on intent.

Persistent JSON Storage  
Logic and data are fully separated. Algorithms are saved locally and persist across sessions.

Solve Workflow Simulation  
A dual‑prompt flow: enter an OLL case → track move count → transition directly into a PLL prompt to mimic real solve practice.

Self‑Healing Error Handling  
try/except logic reconstructs missing or corrupted JSON structures automatically.

🧠 What I’m Learning (The Curriculum)
As of V0.1, I’ve applied and practiced:

Debugging Logic Errors  
Understanding indentation, loop flow, and order‑of‑operations inside while loops.

Variable Scope & Alignment  
Eliminating NameError issues by ensuring consistent variable naming across logic branches.

Data Structure Design  
Transitioning from flat lists to nested dictionaries and learning how to access and manipulate them cleanly.

🗺️ Roadmap to V1.0
Phase 2 — Reverse Scrambler
Generate setup moves automatically using string manipulation and algorithm inversion.

Phase 3 — OOP Refactor
Abstract the entire system into classes for cleaner architecture and scalability.

Phase 4 — Version 1.0 Release
A polished, stable, fully‑featured CLI with robust error handling and clean documentation.

## 📜 Version History & Changelog

### 🚀 [v0.3 - The OOP Foundation](https://github.com/DamonStringer/Rubiks-Algorithm-Assistant/blob/main/versions/v0.3/CA_V0.3_readme.txt)
*Architectural shift from procedural scripting to scalable, object-oriented design.*

* **OOP Refactor:** Encapsulated library management, move-counting, and file I/O into the new `AlgorithmLibrary` class.
* **Separation of Concerns:** Isolated data storage states from operational logic to reduce global state bugs.
* **Method Encapsulation:** Integrated the reverse scrambler into a reusable class method (`generate_scramble()`).
* **Curriculum Focus:** Learned state management, class architecture, and modular engine design.

---

### 🧩 [v0.2 - Reverse Scrambler Engine](https://github.com/DamonStringer/Rubiks-Algorithm-Assistant/blob/main/versions/v0.2/v0.2README.MD)
*Introduced the project's first computational subsystem to generate setup moves.*

* **Reverse Scrambler:** Added logic to clean algorithm strings, split move sequences, and invert faces/primes (preserving double moves) for targeted practice.
* **New Command:** Implemented the `scramble` gate into the main workflow loop.
* **Curriculum Focus:** Mastered advanced string manipulation (`.replace()`, `.split()`), list inversion, and translating physical cube logic into programmatic conditionals.

---

### 📦 [v0.1 - Beta Architecture](https://github.com/DamonStringer/Rubiks-Algorithm-Assistant/blob/main/README.md)
*The ground-up rebuild focusing on structural clarity and persistent storage.*

* **Dynamic Data Routing:** Automatically sorts input into nested OLL/PLL JSON dictionaries.
* **Solve Workflow:** Created a dual-prompt flow mimicking real-world OLL-to-PLL transitions.
* **Self-Healing Logic:** Implemented `try/except` blocks to auto-reconstruct corrupted or missing local data structures.
* **Curriculum Focus:** Debugged loop control flows, handled variable scope errors, and designed nested dictionary structures.
