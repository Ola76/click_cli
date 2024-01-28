import git
import sys
import os

def initialize_or_clone_repository():
    try:
        if not os.path.exists('.git'):
            init_or_clone = input('No Git repository found. Do you want to initialize a new repository (I) or clone an existing one (C)? ').lower()
            
            if init_or_clone == 'i':
                repo_url = input('Enter the Git repository URL (or leave blank to initialize locally): ')
                if repo_url:
                    git.Repo.clone_from(repo_url, '.')
                    print(f'Repository cloned from {repo_url}.')
                else:
                    git.Repo.init('.')
                    print('Initialized a new Git repository locally.')
            elif init_or_clone == 'c':
                repo_url = input('Enter the Git repository URL to clone: ')
                git.Repo.clone_from(repo_url, '.')
                print(f'Repository cloned from {repo_url}.')
            else:
                print('Invalid choice. Exiting.')
                sys.exit(1)
                
    except git.exc.GitCommandError as e:
        print(f'Error: {e}')
        print('Failed to initialize or clone the repository.')

def git_ignore_management():
    try:
        repo = git.Repo('.')
        
        # Check if .gitignore file exists
        gitignore_path = os.path.join(repo.working_tree_dir, '.gitignore')
        
        if not os.path.exists(gitignore_path):
            create_gitignore = input('No .gitignore file found. Do you want to create one? (y/n): ').lower()
            
            if create_gitignore == 'y':
                with open(gitignore_path, 'w') as gitignore_file:
                    gitignore_file.write("# Example .gitignore file\n")
                print('.gitignore file created.')
            else:
                print('Continuing without creating .gitignore.')

        # Provide options for Git Ignore Management
        print('Options for Git Ignore Management:')
        print('1. Add entries to .gitignore')
        print('2. Remove entries from .gitignore')
        print('3. List entries in .gitignore')
        gitignore_choice = input('Choose an option (1/2/3): ')

        if gitignore_choice == '1':
            entries_to_add = input('Enter entries to add to .gitignore (separate multiple entries with spaces): ')
            with open(gitignore_path, 'a') as gitignore_file:
                gitignore_file.write(entries_to_add + '\n')
            print('Entries added to .gitignore.')
        elif gitignore_choice == '2':
            entries_to_remove = input('Enter entries to remove from .gitignore (separate multiple entries with spaces): ')
            with open(gitignore_path, 'r') as gitignore_file:
                lines = gitignore_file.readlines()
            with open(gitignore_path, 'w') as gitignore_file:
                for line in lines:
                    if line.strip() not in entries_to_remove.split():
                        gitignore_file.write(line)
            print('Entries removed from .gitignore.')
        elif gitignore_choice == '3':
            with open(gitignore_path, 'r') as gitignore_file:
                print('.gitignore entries:')
                print(gitignore_file.read())
        else:
            print('Invalid choice. Exiting.')
            sys.exit(1)

    except git.exc.GitCommandError as e:
        print(f'Error: {e}')
        print('Failed to perform Git operations during .gitignore management.')

def branch_management():
    try:
        repo = git.Repo('.')
        branches = [branch.name for branch in repo.branches]

        print('Available branches:')
        for branch in branches:
            print(f' - {branch}')

        branch_choice = input('Do you want to create a new branch (N), switch to an existing branch (S), or continue with the current branch (C)? ').lower()

        if branch_choice == 'n':
            new_branch_name = input('Enter the name for the new branch: ')
            default_branch = input('Use the default branch as the starting point? (y/n): ').lower()
            
            if default_branch == 'y':
                repo.git.checkout('master')  # Change 'master' to your default branch name
                repo.git.branch(new_branch_name)
                repo.git.checkout(new_branch_name)
            else:
                base_branch = input('Enter the name of the branch to base the new branch on: ')
                repo.git.checkout(base_branch)
                repo.git.branch(new_branch_name)
                repo.git.checkout(new_branch_name)

            print(f'New branch "{new_branch_name}" created and checked out.')
        elif branch_choice == 's':
            switch_branch = input('Enter the name of the branch to switch to: ')
            repo.git.checkout(switch_branch)
            print(f'Switched to branch "{switch_branch}".')
        elif branch_choice != 'c':
            print('Invalid choice. Exiting.')
            sys.exit(1)

    except git.exc.GitCommandError as e:
        print(f'Error: {e}')
        print('Failed to perform Git operations during branch management.')

def git_commit():
    try:
        repo = git.Repo('.')

        # Prompt for commit message
        message = input('Enter commit message: ')

        # Prompt for files to commit
        files = input('Enter file(s) to commit (separate multiple files with spaces): ').split()

        if files:
            repo.index.add(files)
        else:
            repo.index.add('*')

        if repo.is_dirty():
            repo.index.commit(message)
            print('Changes committed successfully!')

            # Ask for confirmation before pushing
            push_choice = input('Do you want to push changes to the remote repository? (y/n): ').lower()
            if push_choice == 'y':
                origin = repo.remote('origin')
                origin.push()
                print('Changes pushed successfully!')
            else:
                print('Changes are staged but not pushed to the remote repository.')

        else:
            print('No changes to commit.')

    except git.exc.InvalidGitRepositoryError:
        print('This directory is not a Git repository. Exiting.')
        sys.exit(1)
    except git.exc.GitCommandError as e:
        print(f'Error: {e}')
        print('Failed to perform Git operations during commit.')

if __name__ == '__main__':
    initialize_or_clone_repository()
    git_ignore_management()
    git_commit()
    sys.stdout.close()
    sys.stderr.close()
