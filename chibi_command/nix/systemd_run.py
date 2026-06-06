import os
import itertools

from chibi_command import Command
from chibi_command.nix import Systemctl
from chibi_hybrid.chibi_hybrid import Chibi_hybrid
from chibi.madness.string import generate_string


__all__ = [ 'Systemctl' ]


class System_run( Command ):
    command = 'systemd-run'
    captive = False
    args = [ '--user', '--scope', ]
    kw = { 'unit': 'chibi_command_delegate', 'property': 'Delegate=yes' }
    kw_format = "--{key}={value}"

    def __init__( self, *args, **kw ):
        if os.getuid() == 0:
            if '--user' in self.args:
                self.args.remove( '--user' )
        else:
            if '--user' not in self.args:
                self.args.insert( '--user' )
        super().__init__( *args, **kw )

    @Chibi_hybrid
    def set_command( cls, command, *args ):
        command = cls( command, *args )
        return command

    @set_command.instancemethod
    def set_command( self, command, *args ):
        self.add_args( command, *args )
        return self

    def build_kw( self, **kw ):
        units = Systemctl.list_units().run()
        if os.getuid() != 0:
            units_user = Systemctl.list_units( user=True ).run()
            units = itertools.chain( iter( units ), iter( units_user ) )
        exists_unit = (
            x[ 'unit' ].startswith( self.kw[ 'unit' ] ) for x in units )
        if any( exists_unit ):
            unit_name = self.kw[ 'unit' ]
            extra = generate_string( 4 )
            self.kw[ 'unit' ] = f"{unit_name}_{extra}"
        return super().build_kw( **kw )
