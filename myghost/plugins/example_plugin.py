from myghost.lib.plugin import Plugin


class ExamplePlugin(Plugin):
    def __init__(self, name, version, description, usage, needs_root):
        super().__init__(name, version, description, usage, needs_root)

    def initialize(self) -> None:
        print("Initializing ...")

    def run(self):
        print("run plugin ...")
