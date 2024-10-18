from chibi_command import Command
from chibi_atlas import Chibi_atlas_list


class Ssh( Command ):
    command = 'ssh'
    captive = False

    def __init__( self, user, host, *args, **kw ):
        self._user = user
        self._host = host
        super().__init__( self._build_connection(), *args, **kw )

    def append( self, *commands ):
        self.commands.append( *commands )

    def _concatenate_commands( self, sudo=False, fail_fast=True ):
        if sudo:
            preview_commands = map(
                lambda x: f'sudo {x.preview()}',
                self.commands )
        else:
            preview_commands = map( lambda x: x.preview(), self.commands )
        if fail_fast:
            result = " && ".join( preview_commands )
        else:
            result = "; ".join( preview_commands )
        if result:
            result = f"'{result}'"
        return result

    def _build_connection( self ):
        return f"{self._user}@{self._host}"

    def build_tuple( self, *args, sudo=False, **kw ):
        commands = self._concatenate_commands( sudo=sudo )
        if commands:
            return super().build_tuple( *args, commands, **kw )
        return super().build_tuple( *args, **kw )

    @property
    def commands( self ):
        try:
            return self._commands
        except AttributeError:
            self._commands = Chibi_atlas_list()
            return self._commands
