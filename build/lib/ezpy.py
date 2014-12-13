from cliff.command import Command
from configuration_parser import ConfigurationParser
from extension_parser import ExtensionParser
from code_generator import CodeGenerator
from setup_script_generator import SetupScriptGenerator

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
        setup_script_generator = SetupScriptGenerator()
        setup_script_generator.generate(config)


class Extend(Command):

    def get_parser(self, prog_name):
        parser = super(Extend, self).get_parser(prog_name)
        parser.add_argument('config_file', nargs='?', default='.')
        return parser

    def take_action(self, parsed_args):       
        config_parser = ExtensionParser()
        config = config_parser.parse(parsed_args.config_file)
        print config
        # code_generator = CodeGenerator(config)
        # code_generator.generate()
        # setup_script_generator = SetupScriptGenerator()
        # setup_script_generator.generate(config)

