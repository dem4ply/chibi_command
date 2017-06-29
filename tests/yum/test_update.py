from chibi_command import yum
from unittest.mock import patch, ANY


class Test_yum_update:
    @patch( 'chibi_command.Popen' )
    def test_update_use_the_argument_yes( self, popen_mock ):
        popen_mock.side_effect = Exception
        try:
            yum.update()
        except Exception:
            pass
        popen_mock.assert_called_with( ( 'yum', 'update', '-y', ),
                                       stderr=ANY, stdout=ANY )
