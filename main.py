import os
import git
import sys

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
        print('Failed to perform Git operations.')

if __name__ == '__main__':
    initialize_or_clone_repository()
    git_commit()
    sys.stdout.close()
    sys.stderr.close()