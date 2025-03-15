# Advanced Python Calculator

This project is a midterm submission for a Software Engineering Graduate Course, demonstrating professional software development practices through a Python-based calculator application. It features a command-line REPL, a plugin system, Pandas-based history management, advanced logging, and the application of design patterns for scalability and maintainability.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage Examples](#usage-examples)
- [Design Patterns](#design-patterns)
- [Environment Variables](#environment-variables)
- [Logging Strategy](#logging-strategy)
- [Exception Handling](#exception-handling)
- [Testing](#testing)
- [Video Demonstration](#video-demonstration)
- [Architectural Decisions](#architectural-decisions)
- [License](#license)

## Project Overview
This calculator application integrates clean, maintainable code with advanced features like dynamic plugin loading, Pandas for data management, and a robust logging system. It adheres to PEP 8 standards, achieves 90%+ test coverage, and uses GitHub Actions for continuous integration. The project showcases a clear development history through logical commits in the Git repository.

Repository: (https://github.com/Raz2997/midterm_2025_calc)

## Features
- **Command-Line Interface (REPL)**: Interactive execution of arithmetic operations and history management.
- **Plugin System**: Dynamically load new commands (e.g., statistical operations) without modifying core code.
- **Calculation History**: Managed with Pandas, supporting save, load, and clear operations.
- **Logging**: Configurable via environment variables, with severity levels (INFO, WARNING, ERROR).
- **Design Patterns**: Command, Facade, Singleton, Factory Method, and Strategy patterns for scalability.


### REPL Commands
- **Basic Operations**:
  ```
  Enter command: add
  Enter two numbers: 4 5
  Result: 9.0
  ```
- **History Management**:
  ```
  Enter command: history
     operand1  operand2 operation  result
  0       4.0       5.0         +     9.0
  Enter command: save
  History saved to history.csv
  Enter command: clear
  History cleared
  ```
- **Plugin Command (e.g., Stats)**:
  ```
  Enter command: stats
  Enter two numbers for average: 10 20
  Average: 15.0
  ```

## Design Patterns
The project leverages design patterns to enhance scalability and maintainability:

1. **Command Pattern**: Encapsulates operations as objects, enabling flexible execution and extension in the REPL.
2. **Facade Pattern**: Simplifies Pandas interactions for history management, providing a clean interface.
3. **Singleton Pattern**: Ensures a single `HistoryFacade` instance, maintaining consistent history state.
4. **Factory Method Pattern**: Centralizes command creation, allowing dynamic instantiation.
5. **Strategy Pattern**: Defines interchangeable operation strategies, improving extensibility.

## Environment Variables
Environment variables configure the application dynamically:
- `LOG_LEVEL`: Sets logging verbosity (e.g., `INFO`, `DEBUG`).
- `LOG_FILE`: Specifies log output file (e.g., `calculator.log`).
- `ENVIRONMENT`: Tags logs with the runtime environment (e.g., `development`).

Example `.env`:
```
LOG_LEVEL=DEBUG
LOG_FILE=calculator.log
ENVIRONMENT=development
```

## Logging Strategy
Logging is implemented for monitoring and debugging:
- **Severity Levels**: INFO for operations, WARNING for minor issues, ERROR for failures.
- **Dynamic Configuration**: Controlled via `.env` variables for level and output destination.
- **Format**: Includes timestamp, environment, severity, and message.

## Exception Handling
- **LBYL**: Checks if a history file exists before loading to prevent unnecessary exceptions.
- **EAFP**: Uses try/except for invalid input handling in commands.

## Testing
- **Framework**: Pytest with 90%+ coverage.
- **Coverage Areas**: Calculator operations, history management, command execution, plugin loading.
- **CI/CD**: GitHub Actions runs tests on every push/pull request.
- Run locally: `pytest --cov=./ --cov-report=html`.


## Architectural Decisions
- **Modularity**: Separated concerns into directories for maintainability.
- **Plugin System**: Dynamic loading ensures extensibility.
- **Pandas**: Efficient CSV handling and history querying.
- **Logging**: Provides runtime insights, configurable for development vs. production needs.
- **Commit History**: Logical branches merged into `main` show development progression.

