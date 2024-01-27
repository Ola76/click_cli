import click
import subprocess

@click.command()
@click.option('--message', '-m', prompt=True, help='Commit message')
@click.option('--file', '-f', multiple=True, help='Specify files to stage and commit')
def git_commit(message, file):
    """A script to commit changes using Git."""
    
    try:
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
    except subprocess.CalledProcessError as e:
        click.echo(f'Error: {e}')
        click.echo('Failed to commit changes.')

if __name__ == '__main__':
    git_commit()


# python git_commit_script.py --message "Initial commit" --file file1.txt file2.txt