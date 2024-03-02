from rich.highlighter import RegexHighlighter
from rich.theme import Theme 
from rich.console import Console 

class  EmailHighlighter(RegexHighlighter):
	base_style = "example."
	highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]
theme = Theme({"example.email":"bold magenta"})
console = Console(highlighter=EmailHighlighter(),theme=theme)
console.print("Send funds to money@example.org")
