from unittest import TestCase
from chibi.atlas import Chibi_atlas
from chibi_command import Result_error
from chibi_command.nix import Systemctl
from chibi_command.nix.systemd import Journal_status, Journal_show


class Test_systemctl( TestCase ):
    def test_status( self ):
        with self.assertRaises( Result_error ):
            result = Systemctl.status( "unkown" ).run()

        result = Systemctl.status( "NetworkManager" ).run()
        self.assertIsNotNone( result )
        self.assertTrue( result )
        self.assertIsInstance( result, Journal_status )
        self.assertEqual(
            'NetworkManager.service', result.result.service )

    def test_status_no_fail( self ):
        result = Systemctl.status( "unkown", no_fail=True )
        self.assertFalse( result.raise_on_fail )

    def test_status_has_the_show_properites( self ):
        result = Systemctl.status( "NetworkManager" ).run()
        self.assertIn( 'properties', result.result )
        self.assertIsInstance( result.result.properties, Chibi_atlas )
        self.assertTrue( result.result.properties )

    def test_show( self ):
        result = Systemctl.show( "NetworkManager" ).run()
        self.assertIsNotNone( result )
        self.assertTrue( result )
        self.assertIsInstance( result, Journal_show )
        self.assertIsInstance( result.result, Chibi_atlas )

    def test_list_units( self ):
        result = Systemctl.list_units().run()
        for unit in result.result:
            self.assertIn( 'active', unit )
            self.assertIn( 'description', unit )
            self.assertIn( 'load', unit )
            self.assertIn( 'sub', unit )
            self.assertIn( 'unit', unit )


class Test_systemctl_preview( TestCase ):
    def test_disable_should_be_expected( self ):
        result = Systemctl.disable( 'some_service.service' ).preview()
        self.assertTrue( result.endswith( 'disable some_service.service' ) )

    def test_stop_should_be_expected( self ):
        result = Systemctl.stop( 'some_service.service' ).preview()
        self.assertTrue( result.endswith( 'stop some_service.service' ) )

    def test_start_should_be_expected( self ):
        result = Systemctl.start( 'some_service.service' ).preview()
        self.assertTrue( result.endswith( 'start some_service.service' ) )

    def test_enable_should_be_expected( self ):
        result = Systemctl.enable( 'some_service.service' ).preview()
        self.assertTrue( result.endswith( 'enable some_service.service' ) )
