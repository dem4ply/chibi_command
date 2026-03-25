from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.common import Exit
from chibi_atlas import Chibi_atlas_list


class Ssh( Command ):
    command = 'ssh'
    captive = False

    def __init__( self, user, host, identity_file=None, *args, **kw ):
        self._user = user
        self._host = host
        self._sudo_command = None
        super().__init__( self._build_connection(), *args, **kw )
        self.identity_file = identity_file

    @property
    def sudo_command( self ):
        return self._sudo_command

    @sudo_command.setter
    def sudo_command( self, value ):
        if value == "sudo" or value == "su":
            self._sudo_command = value
        elif value is None:
            self._sudo_command = None
        else:
            raise NotImplementedError(
                f"alternativa a sudo '{value}' no implementada" )

    @property
    def user( self ):
        return self._user

    @property
    def host( self ):
        return self._host

    @property
    def identity_file( self ):
        return self._identity_file

    @identity_file.setter
    def identity_file( self, value ):
        if value is None:
            self._identity_file = None
            return
        path = Chibi_path( value )
        if not path.exists:
            raise FileNotFoundError( path )
        self._identity_file = path
        self.kw[ '-i' ] = self._identity_file

    def append( self, *commands ):
        self.commands.append( *commands )

    def _concatenate_commands( self, sudo=False, fail_fast=True ):
        if sudo or self.sudo_command:
            tmp_sudo = self.sudo_command
            if tmp_sudo is None:
                tmp_sudo = 'sudo'
            preview_commands = map(
                lambda x: f'{tmp_sudo} {x.preview()}',
                self.commands )
        else:
            preview_commands = map( lambda x: x.preview(), self.commands )
        if fail_fast:
            splitter = '&&'
        else:
            splitter = ';'
        result = []
        for command in preview_commands:
            result.append( command )
            result.append( splitter )
        # quita el ultimo splitter porque soy pendejo
        # y no se como hacerlo de otra forma
        if result:
            result.pop()
        return result

    def _build_connection( self ):
        return f"{self._user}@{self._host}"

    def build_tuple( self, *args, sudo=False, **kw ):
        commands = self._concatenate_commands( sudo=sudo )
        if commands:
            return super().build_tuple( *args, *commands, **kw )
        return super().build_tuple( *args, **kw )

    @property
    def commands( self ):
        try:
            return self._commands
        except AttributeError:
            self._commands = Chibi_atlas_list()
            return self._commands

    def set_to_test( self ):
        self.insert_args( '-q' )
        self.commands.append( Exit() )
        self.raise_on_fail = False
        return self
