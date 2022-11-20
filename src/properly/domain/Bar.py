class Bar:
    """ Does the bar part of the domain stuff. """

    def __init__(self) -> None:
        self._bar: str = "Bar"

    def do_the_bar(self) -> str:
        """ Actually does the bar. """
        return self._bar
