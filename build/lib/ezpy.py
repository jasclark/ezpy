from cliff.command import Command
from configuration_parser import ConfigurationParser
from code_generator import CodeGenerator

class Generate(Command):

    def get_parser(self, prog_name):
        parser = super(Generate, self).get_parser(prog_name)
        parser.add_argument('config_file', nargs='?', default='.')
        return parser

    def take_action(self, parsed_args):
        
        config_parser = ConfigurationParser()
        config = config_parser.parse(parsed_args.config_file)
        code_generator = CodeGenerator(config)
        code_generator.generate()


class Extend(Command):
	def take_action(self, parsed_args):
		print("you have invoked extend")