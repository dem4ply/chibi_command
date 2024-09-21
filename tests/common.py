from unittest import TestCase
from chibi_command.common import Cp


class Test_ssh( TestCase ):
    def test_cp( self ):
        cp = Cp( 'path/one', 'path/two' )
        self.assertEqual( cp.preview(), 'cp -v path/one path/two' )
