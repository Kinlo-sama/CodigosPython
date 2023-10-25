from rich.console import Console 
from rich.__main__ import make_test_card

console_ = Console()
with console_.pager():
	console_.print(make_test_card())

