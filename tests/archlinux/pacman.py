from unittest import TestCase
from chibi_command.archilinux import Pacman
from chibi_command.archilinux.pacman import join_parted_lines


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
        expected = 'pacman -S python-chibi python-chibi-command'
        self.assertEqual( pacman.preview(), expected )

    def test_preview_query_info_package( self ):
        pacman = Pacman.query().info( 'sudo' )
        expected = 'pacman -Q -i sudo'
        self.assertEqual( pacman.preview(), expected )

    def test_query_info_result_should_work( self ):
        pacman = Pacman.query().info( 'sudo' )
        result = pacman.run()
        self.assertTrue( result )

    def test_query_info_result_should_have_name( self ):
        pacman = Pacman.query().info( 'sudo' )
        result = pacman.run()
        self.assertIn( 'name', result.result )
        self.assertEqual( result.result.name, 'sudo' )

    def test_query_info_with_no_package_should_return_false( self ):
        pacman = Pacman.query().info( 'adsffdas' )
        result = pacman.run()
        self.assertFalse( result )


class Test_join_parted_lines( TestCase ):
    def test_should_work( self ):
        example = [
            'Depends On      : pacman>6.1  git',
            'Optional Deps   : sudo: privilege elevation [installed]',
            '                  doas: privilege elevation',
        ]
        result = list( join_parted_lines( iter( example ) ) )
        self.assertEqual(
            result,
            [
                'Depends On      : pacman>6.1  git',
                'Optional Deps   : sudo: privilege elevation [installed]\n'
                '                  doas: privilege elevation',
            ]
        )
