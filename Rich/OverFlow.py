from typing import List
from rich.console import Console, OverflowMethod

console = Console(width=14)
supercali = "supercalifragilistixpialdocious"
over_flow_methods: List[OverflowMethod] = ["fold","crop","ellipsis"]
for overflow in over_flow_methods:
	console.rule(overflow)
	console.print(supercali,overflow=overflow,style="bold blue")
	console.print()

