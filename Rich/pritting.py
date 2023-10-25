from rich import print
from rich.panel import Panel
from rich.pretty import Pretty
from rich.pretty import pprint
pretty = Pretty(locals())
panel = Panel(pretty)
pprint(locals())
pprint(["egg","foo"],expand_all=True)
print(["egg","foo"])
pprint(locals(),max_length=2)
pprint("Where there is a will,there is a way",max_string=21)
print(panel)
