import re
from chibi_atlas import Chibi_atlas
from chibi_hybrid.chibi_hybrid import Chibi_hybrid
from chibi_command import Command, Command_result
from chibi_command import Command, Command_result, Command_result

class SS_result( Command_result ):
    def parse_result( self ):
        if not bool( self ):
            return
        lines = list( self.parse_as_lines( self.result ) )
        headers = self.prepare_headers( lines.pop( 0 ) )
        result = []
        for line in lines:
            try:
                result.append( self.parse_headers( headers, line  ) )
            except Exception as e:
                import pdb
                pdb.set_trace()
                pdb.post_mortem( e.__traceback__ )
                raise
        self.result = result

    def prepare_headers( self, headers ):
        result = []
        headers = re.split( r'\s{2,}', headers.strip() )

        for header in headers:
            header = header.strip().lower()
            header = header.replace( ':', '__' )
            if header == 'recv-q send-q':
                result.append( 'recv-q' )
                result.append( 'send-q' )
            elif header == 'peer address__portprocess':
                result.append( 'peer_address__port' )
                result.append( 'process' )
            else:
                result.append( header.replace( ' ', '_' ) )
        if 'recv-q_send-q_local_address__port' in result:
            new_result = []
            for h in result:
                if h == 'recv-q_send-q_local_address__port':
                    new_result.append( 'recv-q' )
                    new_result.append( 'send-q' )
                    new_result.append( 'local_address__port' )
                else:
                    new_result.append( h )
            return self.prepare_headers( "  ".join( new_result ) )
        return result

    def parse_headers( self, headers, line ):
        result = Chibi_atlas()
        values = line.split( ' ', 5 )
        values = re.split(
            r'\s{1,}', line.strip(), maxsplit=len( headers ) + 1 )
        for h, v in zip( headers, values ):
            if h == 'recv-q':
                h = 'queue'
                current = result.setdefault( 'queue', Chibi_atlas() )
                current.receive = v
            elif h == 'send-q':
                h = 'queue'
                current = result.setdefault( 'queue', Chibi_atlas() )
                current.send = v
            elif h == 'peer_address__port':
                ip, port = v.rsplit( ':', 1 )
                current = result.setdefault( 'peer_address', Chibi_atlas() )
                current.ip = ip
                current.port = port
            elif h == 'local_address__port':
                ip, port = v.rsplit( ':', 1 )
                current = result.setdefault(
                    'local_address', Chibi_atlas() )
                current.ip = ip
                current.port = port
            else:
                result[ h ] = v
        return result


class SS( Command ):
    command = 'ss'
    captive = True
    result_class = SS_result

    @Chibi_hybrid
    def listening( cls ):
        return cls( '-l' )

    @listening.instancemethod
    def listening( self ):
        self.add_args( '-l' )
        return self

    @Chibi_hybrid
    def tcp( cls ):
        return cls( '-t' )

    @tcp.instancemethod
    def tcp( self ):
        self.add_args( '-t' )
        return self

    @Chibi_hybrid
    def numeric( cls ):
        return cls( '-n' )

    @numeric.instancemethod
    def numeric( self ):
        self.add_args( '-n' )
        return self

    @Chibi_hybrid
    def processes( cls ):
        return cls( '-p' )

    @processes.instancemethod
    def processes( self ):
        self.add_args( '-p' )
        return self

    @Chibi_hybrid
    def sport__eq( cls, port ):
        return cls( f'sport = {port}' )

    @sport__eq.instancemethod
    def sport__eq( self, port ):
        self.add_args( f'sport = {port}' )
        return self

    @Chibi_hybrid
    def port_is_open( cls, port ):
        command = cls.listening().tcp().processes().numeric()
        command.sport__eq( port )
        result = command.run().result
        return bool( len( result ) )
