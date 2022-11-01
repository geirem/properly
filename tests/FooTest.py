from properly.lib.Foo import Foo


def test_foo() -> None:
    foo: Foo = Foo()
    foo.action("bar")
    assert "bar" in str(foo)
