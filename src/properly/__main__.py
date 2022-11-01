from properly.lib.Foo import Foo
from properly import setup

setup()

foo = Foo()
foo.action("Hei")
print(foo)
