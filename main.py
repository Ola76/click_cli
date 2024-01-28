import git
import sys

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
        print('This directory is not a Git repository. Initialize Git manually.')

if __name__ == '__main__':
    git_commit()
    sys.stdout.close()
    sys.stderr.close()
