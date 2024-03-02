from rich import print
from rich.panel import Panel
from rich.text import Text 
from rich.console import Console

console = Console()
text = Text("Hello World!")
text.stylize("bold magenta",0,6)
console.print(text)
#you can use append too
text2 = Text()
text2.append("Hello",style="bold magenta")
text2.append(" World!")
console.print(text2)
text3 = Text.from_ansi("\033[1mHello World!\033[0m")
console.print(text3.spans)
#and you can also use assemble for the same 
text4 = Text.assemble(("Hello","bold magenta")," World!")
console.print(text4)
panel = Panel(Text("Hello",justify="center"))
print(panel)
