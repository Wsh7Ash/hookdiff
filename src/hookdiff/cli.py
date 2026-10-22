#!/usr/bin/env python3
import click, json
from rich.console import Console
from .diff import diff, breaking
console = Console()
@click.group()
@click.version_option()
def main(): pass
@main.command()
@click.argument('old_file')
@click.argument('new_file')
def compare(old_file, new_file):
    old = json.load(open(old_file))
    new = json.load(open(new_file))
    changes = diff(old, new)
    brk = breaking(changes)
    for c in changes:
        color = {'added': 'green', 'removed': 'red', 'changed': 'yellow'}[c['change']]
        console.print(f'[{color}]{c["change"]:8}[/] {c["path"]}')
    console.print(f'[bold]{len(changes)} changes, {len(brk)} potentially breaking[/bold]')
if __name__ == '__main__': main()
