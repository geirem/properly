class Foo:

    def __init__(self) -> None:
        self._what = "world"
        self._action: str|None = None

    def action(self, action: str) -> None:
        self._action = action

    def __repr__(self) -> str:
        return f"{self._action if self._action else 'Hello'}, {self._what}"
