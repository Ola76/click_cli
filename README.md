# Git Commit Script with GitPython

This Python script automates the process of committing changes using Git. It utilizes the GitPython library to interact with Git repositories. The script prompts the user for a commit message, allows the selection of files to commit, and optionally pushes the changes to the remote repository.

## Prerequisites

- Python installed on your machine
- GitPython library installed (`pip install gitpython`)

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Run the Script:**
   ```bash
   python git_commit_script.py
   ```
   Follow the prompts to enter the commit message, select files, and confirm the push to the remote repository.

## Features
- .gitignore management (add, delete, view).
- Branch management (create, switch, current).
- Commit changes with a custom commit message.
- Select specific files to commit or commit all changes.
- Optional push to the remote repository after committing.

## Troubleshooting

- If you encounter any issues, make sure you have GitPython installed (`pip install gitpython`).
- Check if your current directory is a valid Git repository.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.


## Acknowledgments

- Thank you to the GitPython developers for providing a Pythonic interface to Git.
