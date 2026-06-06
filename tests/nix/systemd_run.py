from unittest import TestCase
from unittest.mock import patch
from chibi_command.nix.systemd_run import System_run


class Test_systemd_run( TestCase ):
    def test_should_work( self ):
        result = System_run().preview()
        self.assertEqual(
            result, (
                f'systemd-run --unit={System_run.kw["unit"]} '
                '--property=Delegate=yes --user --scope'
            ) )

    def test_set_command( self ):
        result = System_run( 'lxc-ls', '-f' )
        self.assertEqual(
            result, (
                f'systemd-run --unit={System_run.kw["unit"]} '
                '--property=Delegate=yes --user --scope lxc-ls -f'
            ) )

    @patch( 'os.getuid' )
    def test_when_user_is_root_should_no_send_user_arg( self, getuid ):
        getuid.return_value = 0
        result = System_run().preview()
        self.assertEqual(
            result, (
                f'systemd-run --unit={System_run.kw["unit"]} '
                '--property=Delegate=yes --scope'
            ) )
