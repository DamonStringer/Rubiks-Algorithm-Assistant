# Rubik's Algorithm Assistant 🧊

A command-line Python application designed to manage, search, and persistently store Rubik's Cube OLL and PLL algorithms using a nested JSON architecture. 

## 🎯 The Core Mission: A Living Learning Log
This repository is more than just a functional tool; it is a **living engineering log**. I am using this project as a "Shadow Curriculum" to actively document my progression in Python and software architecture. 

Rather than building a perfect program on day one, I am deploying iterative versions. Future commits will document not just new features, but the bugs I break, the technical debt I clean up, and the engineering concepts I master along the way.

## 🚀 Version 1.0 Features
* **Persistent Data Storage:** Separates the Python logic (the engine) from the JSON data (the fuel), ensuring algorithms are saved locally and permanently.
* **Nested Dictionary Architecture:** Upgraded from a flat data list to categorized "drawers" for independent OLL and PLL querying.
* **The "Solve Workflow":** A dual-prompt logic gate that allows the user to input an OLL case and immediately transitions to a PLL prompt to simulate an actual practice solve.
* **Automated Error Handling:** Includes `try/except` safety nets to automatically reconstruct the necessary JSON file structure if it is ever deleted or corrupted.

## 🧠 What I'm Learning (The Curriculum)
As I iterate on this project, I am actively mapping these computer science concepts:
* **Decoupling:** Keeping data layers (`algs.json`) strictly separated from execution layers (`.py`).
* **Control Flow:** Building resilient `while True:` loops and logic gates that handle unexpected user input cleanly.
* **Data Structures:** Moving from flat lists to complex nested dictionaries.
* **Code Sanitization:** Adhering strictly to PEP 8 indentation and syntax standards.
