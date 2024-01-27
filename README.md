# Git Click CLI Automation Tool

A command-line interface (CLI) automation tool built using Click to simplify common Git operations. This tool allows for effortless Git repository initialization, committing changes, pulling updates, and pushing changes to a remote repository.

## Features

- **Git Initialization:** Easily initialize a new Git repository.
- **Commit Changes:** Streamline the process of committing changes with a clear command.
- **Pull Updates:** Effortlessly pull the latest changes from the remote repository.
- **Push Changes:** Seamlessly push your local changes to the remote repository.

## Prerequisites

Before using this tool, ensure that you have the following installed on your machine:

- [Python](https://www.python.org/downloads/) (>=3.6)
- [Git](https://git-scm.com/downloads/)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ola76/click_cli.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd click_cli
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Git Initialization

Initialize a new Git repository in the current directory:

```bash
python cli.py init
```

### Commit Changes

Commit your changes with a descriptive message:

```bash
python cli.py commit -m "Your commit message here"
```

### Pull Updates

Pull the latest changes from the remote repository:

```bash
python cli.py pull
```

### Push Changes

Push your local changes to the remote repository:

```bash
python cli.py push
```

## Troubleshooting

If you encounter any issues or have questions, please check our [troubleshooting guide](TROUBLESHOOTING.md).

## Contributing

If you'd like to contribute to the development of this tool, please follow our [contribution guidelines](CONTRIBUTING.md).

```

Feel free to make any additional modifications based on your preferences or project-specific details. If you have specific elements you'd like to include or customize, just let me know!
