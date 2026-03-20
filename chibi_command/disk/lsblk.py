from chibi_command import Command
import json

from chibi.atlas import Chibi_atlas

from chibi_command import Command, Command_result, Command_json_result


class Block( Chibi_atlas ):
    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw )
        childs = self.pop( 'children', None )
        if childs:
            self.childs = childs


class Blocks( Chibi_atlas ):
    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw )
        self.childs = [ Block( c ) for c in self.pop( 'children' ) ]


class Lsblk_result( Command_json_result ):
    def parse_result( self ):
        super().parse_result()
        result = self.result
        result = { b.name: Blocks( b ) for b in result.blockdevices }
        self.result = result

    def __getitem__( self, key ):
        return self.result[ key ]


class Lsblk( Command ):
    command = 'lsblk'
    captive = True
    args = ( '-f', '--json' )
    result_class = Lsblk_result
