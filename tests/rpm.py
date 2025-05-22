from unittest import TestCase
from unittest.mock import Mock, patch
from chibi_command.rpm import RPM


class Test_RPM( TestCase ):
    def test_q_should_work( self ):
        result = RPM.query()
        self.assertIsNotNone( result )
        self.assertEqual( "rpm -q", result.preview() )

    def test_instance_q_should_work( self ):
        result = RPM().query()
        self.assertIsNotNone( result )
        self.assertEqual( "rpm -q", result.preview() )

    def test_changelog_should_work( self ):
        result = RPM.query().changelog()
        self.assertIsNotNone( result )
        self.assertEqual( "rpm -q --changelog", result.preview() )

    def test_instance_changelog_should_work( self ):
        result = RPM().query().changelog()
        self.assertIsNotNone( result )
        self.assertEqual( "rpm -q --changelog", result.preview() )

    @patch( 'chibi_command.Popen' )
    def test_push_should_work( self, popen ):
        proccess = Mock()
        popen.return_value = proccess
        proccess.returncode = 0
        proccess.communicate.return_value = ( b"", b"" )
        RPM.query().changelog().run( 'some.rpm' )

        popen.assert_called_once()
        called_args = popen.call_args[0][0][-1]
        self.assertEqual( called_args, "some.rpm" )

    def test_query_make_captive_the_command( self ):
        result = RPM.query()
        self.assertTrue( result.captive )
