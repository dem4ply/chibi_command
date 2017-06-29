
from chibi_command import yum
from unittest.mock import patch, ANY


class Test_yum:
    @patch( 'chibi_command.Popen' )
    def test_update_use_the_argument_yes( self, popen_mock ):
        popen_mock.side_effect = Exception
        try:
            yum.yum( 'some_command' )
        except Exception:
            pass
        popen_mock.assert_called_with( ( 'yum', 'some_command', '-y', ),
                                       stderr=ANY, stdout=ANY )
