from unittest import TestCase
from chibi_command.common import Cp, Ping


class Test_cp( TestCase ):
    def test_cp( self ):
        cp = Cp( 'path/one', 'path/two' )
        self.assertEqual( cp.preview(), 'cp -v path/one path/two' )


class Test_ping( TestCase ):
    def test_ping_default( self ):
        result = Ping().preview()
        expected = 'ping -c 8'
        self.assertEqual( result, expected )

    def test_ping_result_count_be_8( self ):
        result = Ping().run( 'localhost' )
        self.assertEqual( result.count, 8 )

    def test_ping_received_should_be_int( self ):
        result = Ping().run( 'localhost' )
        self.assertIsInstance( result.received, int )

    def test_ping_should_have_all_pings( self ):
        result = Ping().run( 'localhost' )
        self.assertIsInstance( result.pings, list )
        self.assertTrue( result.pings )
