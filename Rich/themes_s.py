from rich.console import Console
from rich.theme import Theme
theme_danger = Theme({
		"info":"dim cyan",
		"warning":"magenta",
		"danger":"bold red"
		})
console = Console(theme=theme_danger)
console.print("This is information",style="info")
console.print("[warning]the pod bay doors are locked[/warning]")
console.print("something bad happend!", style="danger")
