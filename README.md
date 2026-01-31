# Production-Quality CLI Task Manager

A robust, modular, and extensible Command Line Interface (CLI) Task Manager built in Python, adhering to SOLID principles and Clean Architecture.

## 🚀 Features
- **SOLID Design**: Modular architecture following the Single Responsibility and Dependency Inversion principles.
- **Persistent Storage**: Tasks are automatically saved to and loaded from a `tasks.json` file.
- **Clean Architecture**: Separation of concerns between domain models, storage implementations, business logic, and user interface.
- **Robust Error Handling**: Handles invalid user input and potential file-system issues gracefully.

## 📁 Project Structure
```text
.
├── main.py
├── task_manager/
│   ├── models.py
│   ├── interfaces.py
│   ├── storage.py
│   ├── service.py
│   └── ui.py
└── README.md
```

## 🏃 How to Run
```bash
python main.py
```
