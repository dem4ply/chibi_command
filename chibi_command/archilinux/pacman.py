from chibi_atlas import Chibi_atlas
from chibi_command import Command, Command_result
from chibi_hybrid import Chibi_hybrid


def join_parted_lines( lines ):
    prev = next( lines )
    for line in lines:
        if line.startswith( ' ' ):
            prev = f"{prev}\n{line}"
        else:
            yield prev
            prev = line
    yield prev


class Query_result( Command_result ):
    def parse_result( self ):
        if not bool( self ):
            return
        lines = self.result.split( '\n' )
        lines = filter( bool, lines )
        lines = join_parted_lines( lines )
        tuples = ( line.split( ':', 1 ) for line in lines )
        tuples = ( ( k.strip().lower(), v.strip() ) for k, v in tuples )
        result = Chibi_atlas( dict( tuples ) )
        self.result = result


class Pacman( Command ):
    command = 'pacman'
    captive = False

    @classmethod
    def sync( cls ):
        return cls( '-Sy' )

    @classmethod
    def upgrade( cls ):
        return cls( '-Syu' )

    @classmethod
    def install( cls, *packages ):
        return cls( '-S', *packages )

    @classmethod
    def query( cls ):
        return cls( '-Q' )

    @Chibi_hybrid
    def info( cls, package ):
        return cls.query().info( package )

    @info.instancemethod
    def info( self, package ):
        self.add_args( '-i', package )
        self.env.LC_ALL = 'C'
        self.result_class = Query_result
        self.captive = True
        self.raise_on_fail = False
        return self
