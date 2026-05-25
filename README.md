# 🧊 Rubik's Algorithm Assistant

A command‑line Python tool for managing, searching, and persistently storing OLL/PLL algorithms using a structured JSON backend.

## 🎯 Purpose: A Living Engineering Log
This repository is more than a utility — it’s a living learning log. I’m using this project as a “Shadow Curriculum” to document my growth in Python, software architecture, and systems thinking.
Instead of pretending the first version is perfect, I’m intentionally building in public. Each iteration captures:
- the bugs I break
- the technical debt I clean
- the concepts I learn
- the architecture I refine

This project is both a tool and a record of my engineering progression.

## 🚀 Current Build — Version 0.41: Seed Data & Mobile Deployment
This version finalizes the OOP UI loop, secures the repository architecture, and proves the engine's portability by successfully deploying to an Android environment.

**Key Features**
- **Seed Data Architecture:** Implemented a fallback template (`default_algs.json`) to securely generate local databases for new users without causing Git merge conflicts.
- **2-Look PLL Expansion:** The default JSON database now includes the complete 2-Look PLL toolset (Ua, Ub, Z, Y perms) for full last-layer permutation.
- **Mobile Portability:** Validated the engine's execution on Android via Pydroid 3, overcoming OS scoped-storage and sandboxing limitations.
- **Hardened Controller Loop:** Patched loop control flaws (misaligned catch-alls and infinite `continue` traps) in the UI router.

## 🧠 What I’m Learning (The Curriculum)
As of V0.41, I’ve applied and practiced:
- **Repository Architecture:** Implementing `.gitignore` firewalls and separating template data from live user data to prevent public data leaks.
- **Object-Oriented Design:** Method delegation, state management (`self.data`), and object composition (Model-View-Controller).
- **Deployment Environments:** Escaping Android's "Scoped Storage" to allow Python engines to read and write files on mobile devices.
- **Control Flow:** Mastering nested conditionals and short-circuiting loops.

## 🗺️ Roadmap to V1.0
- **Phase 1 — Procedural Logic:** Built the core reverse-scrambler and JSON dictionary logic. *(Completed)*
- **Phase 2 — OOP Refactor:** Abstract the system into objects and secure the repository data state. *(Completed)*
- **Phase 3 — Graphical User Interface (GUI):** Transition from a text-based terminal loop to a visual canvas with clickable inputs (Tkinter/Kivy).
- **Phase 4 — Standalone Packaging:** Compile the final GUI application into deployable `.exe` and `.apk` files for desktop and mobile users.

---

## 📜 Version History & Changelog

### 📱 v0.41 - Seed Data & Mobile Deployment
*Secured the repository architecture and successfully deployed the engine to a mobile environment.*
- **State Separation:** Built a `try/except` initialization sequence using `default_algs.json` to prevent personal user databases from leaking into public version control.
- **Database Expansion:** Completed the "2-Look PLL" algorithm dictionary by adding the Ua, Ub, Z, and Y permutations.
- **Controller Hardening:** Patched UI router logic, successfully nesting search conditionals and removing infinite loop traps.
- **Curriculum Focus:** Mastered repository architecture (`.gitignore`), Git conflict prevention, and Android OS Scoped Storage constraints.

### 🚀 v0.3 - The OOP Foundation
*Architectural shift from procedural scripting to scalable, object-oriented design.*
- **OOP Refactor:** Encapsulated library management, move-counting, and file I/O into the new `AlgorithmLibrary` class.
- **Separation of Concerns:** Isolated data storage states from operational logic to reduce global state bugs.
- **Method Encapsulation:** Integrated the reverse scrambler into a reusable class method (`generate_scramble()`).
- **Curriculum Focus:** Learned state management, class architecture, and modular engine design.

### 🧩 v0.2 - Reverse Scrambler Engine
*Introduced the project's first computational subsystem to generate setup moves.*
- **Reverse Scrambler:** Added logic to clean algorithm strings, split move sequences, and invert faces/primes (preserving double moves) for targeted practice.
- **New Command:** Implemented the `scramble` gate into the main workflow loop.
- **Curriculum Focus:** Mastered advanced string manipulation (`.replace()`, `.split()`), list inversion, and translating physical cube logic into programmatic conditionals.

### 📦 v0.1 - Beta Architecture
*The ground-up rebuild focusing on structural clarity and persistent storage.*
- **Dynamic Data Routing:** Automatically sorts input into nested OLL/PLL JSON dictionaries.
- **Solve Workflow:** Created a dual-prompt flow mimicking real-world OLL-to-PLL transitions.
- **Self-Healing Logic:** Implemented `try/except` blocks to auto-reconstruct corrupted or missing local data structures.
- **Curriculum Focus:** Debugged loop control flows, handled variable scope errors, and designed nested dictionary structures.
