from rich.console import Console
from rich.progress import *
import time

console = Console()
print()
console.print(f"Hello World!", style= f"{'cyan'} bold")
print()


console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")

with Progress() as progress:
    task1 = progress.add_task("[red]Timing...", total=100)

    while not progress.finished:
        progress.update(task1, advance=60/100)
        time.sleep(0.05)