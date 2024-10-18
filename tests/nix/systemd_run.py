from unittest import TestCase
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
