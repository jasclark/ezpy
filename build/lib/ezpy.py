from cliff.command import Command


class Generate(Command):

    def take_action(self, parsed_args):
		print("you have invoked generate")

class Extend(Command):
	def take_action(self, parsed_args):
		print("you have invoked extend")