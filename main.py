import os
import click
import subprocess

@click.command()
@click.option('--message', '-m', prompt=True, help='Commit message')
@click.option('--file', '-f', multiple=True, help='Specify files to stage and commit')
def git_commit(message, file):
    """A script to commit changes using Git."""
    
    try:
        # Check if the current directory is a Git repository
        if not os.path.exists('.git'):
            click.echo('This directory is not a Git repository. Initialize Git manually.')
            return

        if file:
            subprocess.run(['git', 'add'] + list(file), check=True)
        else:
            subprocess.run(['git', 'add', '.'], check=True)

        # Check if there are changes to commit before running 'git commit'
        status_check = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, check=True)
        if status_check.stdout.strip():
            subprocess.run(['git', 'commit', '-m', message], check=True)
            click.echo('Changes committed successfully!')
        else:
            click.echo('No changes to commit.')

        # Push changes to the remote repository
        subprocess.run(['git', 'push'], check=True)
        click.echo('Changes pushed successfully!')

    except subprocess.CalledProcessError as e:
        click.echo(f'Error: {e}')
        click.echo('Failed to commit and push changes.')

if __name__ == '__main__':
    git_commit()


# python main.py --message "Initial commit" --file main.py requirements.txt