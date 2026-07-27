from unittest import TestCase

from chibi_command.archlinux import Makepkg  # ajusta el import a tu ruta real


class Test_makepkg( TestCase ):
    def setUp( self ):
        self.command = Makepkg()

    def test_should_have_the_correct_base_command( self ):
        self.assertEqual( self.command.preview(), 'makepkg' )


class Test_makepkg_syncdeps( TestCase ):
    def test_when_call_as_classmethod_should_add_the_syncdeps_flag( self ):
        command = Makepkg.syncdeps()
        self.assertEqual( command.preview(), 'makepkg --syncdeps' )

    def test_when_call_as_instance_method_should_add_the_syncdeps_flag( self ):
        command = Makepkg()
        command.syncdeps()
        self.assertEqual( command.preview(), 'makepkg --syncdeps' )


class Test_makepkg_install( TestCase ):
    def test_when_call_as_classmethod_should_add_the_install_flag( self ):
        command = Makepkg.install()
        self.assertEqual( command.preview(), 'makepkg --install' )

    def test_when_call_as_instance_method_should_add_the_install_flag( self ):
        command = Makepkg()
        command.install()
        self.assertEqual( command.preview(), 'makepkg --install' )


class Test_makepkg_clean( TestCase ):
    def test_when_call_as_classmethod_should_add_the_clean_flag( self ):
        command = Makepkg.clean()
        self.assertEqual( command.preview(), 'makepkg --clean' )

    def test_when_call_as_instance_method_should_add_the_clean_flag( self ):
        command = Makepkg()
        command.clean()
        self.assertEqual( command.preview(), 'makepkg --clean' )


class Test_makepkg_no_confirm( TestCase ):
    def test_when_call_as_classmethod_should_add_the_no_confirm_flag( self ):
        command = Makepkg.no_confirm()
        self.assertEqual( command.preview(), 'makepkg --noconfirm' )

    def test_when_call_as_instance_method_should_add_the_no_confirm_flag( self ):
        command = Makepkg()
        command.no_confirm()
        self.assertEqual( command.preview(), 'makepkg --noconfirm' )


class Test_makepkg_chaining_multiple_flags( TestCase ):
    def test_should_be_able_to_combine_syncdeps_install_and_no_confirm( self ):
        command = Makepkg()
        command.syncdeps()
        command.install()
        command.no_confirm()
        self.assertEqual(
            command.preview(), 'makepkg --syncdeps --install --noconfirm'
        )

    def test_classmethod_and_instancemethod_should_be_combinable( self ):
        command = Makepkg.syncdeps()
        command.install()
        self.assertEqual( command.preview(), 'makepkg --syncdeps --install' )
