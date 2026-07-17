from unittest import TestCase
from chibi_command.network.ss import SS


class Test_ss( TestCase ):
    def test_should_return_expected_sport_preview( self ):
        expected = "ss -l -t -p sport = 80"
        command = SS.listening().tcp().processes().sport__eq( 80 )
        self.assertEqual( command.preview(), expected )

    def test_should_return_expected_preview( self ):
        expected = "ss -l -t -p"
        command = SS.listening().tcp().processes()
        self.assertEqual( command.preview(), expected )

    def test_result_should_have_expected_fields( self ):
        command = SS.listening().tcp().processes().numeric()
        result = command.run()
        expected = [
            'state', 'queue', 'local_address',
            'peer_address',
        ]
        # 'Receive_Queue'
        # 'Send_Queue'
        self.assertTrue( result.result )
        self.assertIsInstance( result.result, list )
        for result in result.result:
            for field in expected:
                self.assertIn( field, result )

    def test_result_should_be_true( self ):
        command = SS.listening().tcp().processes().numeric()
        result = command.run()
        self.assertTrue( result.result )
        self.assertIsInstance( result.result, list )
        port = result.result[0]
        self.assertTrue( port.state )
        self.assertTrue( port.queue )
        self.assertTrue( port.queue.send )
        self.assertTrue( port.queue.receive )
        self.assertTrue( port.local_address )
        self.assertTrue( port.local_address.ip )
        self.assertTrue( port.local_address.port )
        self.assertTrue( port.peer_address.ip )
        self.assertTrue( port.peer_address.port )
        self.assertTrue( port.process )

    def test_port_is_open_should_be_true( self ):
        command = SS.listening().tcp().processes().numeric()
        result = command.run()
        self.assertTrue( result.result )
        self.assertIsInstance( result.result, list )
        expected = result.result[0]
        port = expected.local_address.port
        self.assertTrue( int( port ) )
        self.assertTrue( SS.port_is_open( port ) )

    def test_port_is_open_should_be_false( self ):
        self.assertFalse( SS.port_is_open( 999999 ) )
