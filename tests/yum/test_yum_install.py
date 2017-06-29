from chibi_command import yum
from unittest.mock import patch, ANY


class Test_yum_install:
    @patch( 'chibi_command.Popen' )
    def test_install_use_the_argument_yes( self, popen_mock ):
        popen_mock.side_effect = Exception
        try:
            yum.install( 'ruby' )
        except Exception:
            pass
        popen_mock.assert_called_with( ( 'yum', 'install', '-y', ANY, ),
                                       stderr=ANY, stdout=ANY )
