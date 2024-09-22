from unittest import TestCase
from chibi_command.archilinux import Pacman


class Test_pacman( TestCase ):
    def test_preview_sync_should_be_expected( self ):
        pacman = Pacman.sync()
        expected = 'pacman -Sy'
        self.assertEqual( pacman.preview(), expected )

    def test_preview_upgrade_should_be_expected( self ):
        pacman = Pacman.upgrade()
        expected = 'pacman -Syu'
        self.assertEqual( pacman.preview(), expected )

    def test_preview_install_package_should_be_expected( self ):
        pacman = Pacman.install( 'python-chibi', 'python-chibi-command' )
        expected = 'pacman -S pythhon-chibi python-chibi-command'
        self.assertEqual( pacman.preview(), expected )
