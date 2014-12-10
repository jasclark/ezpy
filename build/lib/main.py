import sys
from cliff.app import App
from cliff.commandmanager import CommandManager


class EzpyApp(App):

    def __init__(self):
        super(EzpyApp, self).__init__(
            description='ezpy app',
            version='0.1',
            command_manager=CommandManager('ezpy'),
            )

def main(argv=sys.argv[1:]):
    ezpyApp = EzpyApp()
    return ezpyApp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))