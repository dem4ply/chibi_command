from unittest import TestCase
from chibi_command.script import Bash, Python


class Test_bash( TestCase ):
    def test_preview_should_have_expected_command( self ):
        script = Bash( 'some_script.sh' )
        self.assertEqual( script.preview(), 'bash some_script.sh' )


class Test_python( TestCase ):
    def test_preview_should_have_expected_command( self ):
        script = Python( 'some_script.py' )
        self.assertEqual( script.preview(), 'python some_script.py' )
