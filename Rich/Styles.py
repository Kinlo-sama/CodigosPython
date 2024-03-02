from console import console
from rich.style import Style
console.print("Hello",style="white")
console.print("Hello",style="color(10)")
console.print("Hello",style="#af00ff")
console.print("Hello",style="rgb(175,0,255)")
console.print("DANGER!",style="strike underline frame red on white")
console.print("foor [not bold]bar[/not bold] baz",style="bold")
console.print("Google",style="link google.com")
danger_style = Style(color="red",blink=True,bold=True)
console.print("Danger!",style=danger_style)

