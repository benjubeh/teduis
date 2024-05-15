from rich.console import Console

console = Console()

def cprint(text, color):
    console.print(text, style=f"bold {color}")

cprint(f'\n>>> {to_symbol} | {error}', 'red')
