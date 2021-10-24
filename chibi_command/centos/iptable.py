from chibi_hybrid.chibi_hybrid import Chibi_hybrid
from chibi_command import Command


__all__ = [ 'Iptables' ]


class Iptables( Command ):
    command = "iptables"
    kw_format = "--{key} {value}"


    @Chibi_hybrid
    def table( cls, table ):
        return cls( table=table )

    @table.instancemethod
    def table( self, table ):
        self.add_args( table=table )
        return self

    @Chibi_hybrid
    def append( cls, chain ):
        return cls( append=chain )

    @append.instancemethod
    def append( self, chain ):
        self.add_args( append=chain )
        return self

    @Chibi_hybrid
    def delete( cls ):
        return cls( delete="" )

    @delete.instancemethod
    def delete( self ):
        self.add_args( delete="" )
        return self

    @Chibi_hybrid
    def line_numbers( cls ):
        return cls( '--line-numbers' )

    @delete.instancemethod
    def line_numbers( self ):
        self.add_args( '--line-numbers' )
        return self

    @Chibi_hybrid
    def protocol( cls, protocol ):
        return cls( protocol=protocol )

    @protocol.instancemethod
    def protocol( self, protocol ):
        self.add_args( protocol=protocol )
        return self

    @Chibi_hybrid
    def in_interface( cls, interface ):
        return cls( **{ 'in-interface': interface } )

    @in_interface.instancemethod
    def in_interface( self, interface ):
        kw = { 'in-interface': interface }
        self.add_args( **kw )
        return self

    @Chibi_hybrid
    def destination_port( cls, port ):
        return cls( **{ 'destination-port': port } )

    @destination_port.instancemethod
    def destination_port( self, port ):
        kw = { 'destination-port': port }
        self.add_args( **kw )
        return self

    @Chibi_hybrid
    def jump( cls, target ):
        return cls( jump=target )

    @destination_port.instancemethod
    def jump( self, target ):
        self.add_args( jump=target )
        return self

    @Chibi_hybrid
    def to_destination( cls, ip, port=None ):
        if port is not None:
            ip = f"{ip}:{port}"
        return cls( **{ 'to-destination': port } )

    @to_destination.instancemethod
    def to_destination( self, ip, port=None):
        if port is not None:
            ip = f"{ip}:{port}"

        kw = { 'to-destination': ip }
        self.add_args( **kw )
        return self
