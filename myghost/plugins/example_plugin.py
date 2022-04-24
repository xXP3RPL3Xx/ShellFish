from myghost.lib.plugin import Plugin


class ExamplePlugin(Plugin):
    def __init__(self):
        pass

    def initialize(self) -> None:
        print("Initializing ...")

    def run(self):
        print("run plugin ...")
