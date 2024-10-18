from unittest import TestCase
from chibi_command.archilinux import Yay


class Test_yay( TestCase ):
    def test_preview_sync_should_be_expected( self ):
        yay = Yay.sync()
        expected = 'yay -Sy'
        self.assertEqual( yay.preview(), expected )

    def test_preview_upgrade_should_be_expected( self ):
        yay = Yay.upgrade()
        expected = 'yay -Syu'
        self.assertEqual( yay.preview(), expected )

    def test_preview_install_package_should_be_expected( self ):
        yay = Yay.install( 'python-chibi', 'python-chibi-command' )
        expected = 'yay -S python-chibi python-chibi-command'
        self.assertEqual( yay.preview(), expected )
