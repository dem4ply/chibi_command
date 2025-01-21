from unittest import TestCase
from chibi_command.ssh import Ssh
from chibi_command.common import Cp


class Test_ssh( TestCase ):
    def test_preview_should_have_expected_command( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        self.assertEqual( ssh.preview(), 'ssh some_user@8.8.8.8' )

    def test_preview_when_add_commands_should_be_append( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append( Cp( 'path/one', 'path/two' ) )
        expected = "ssh some_user@8.8.8.8 cp -v path/one path/two"
        preview = ssh.preview()
        self.assertEqual( preview, expected )

    def test_preview_when_use_sudo_on_run_should_append_sudo( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append( Cp( 'path/one', 'path/two' ) )
        expected = "ssh some_user@8.8.8.8 sudo cp -v path/one path/two"
        preview = ssh.preview( sudo=True )
        self.assertEqual( preview, expected )

    def test_append_from_commands_work_with_multi( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append(
            Cp( 'path/one', 'path/two' ),
            Cp( 'path/one', 'path/two' ),
        )
        expected = (
            "ssh some_user@8.8.8.8 sudo cp -v path/one path/two && "
            "sudo cp -v path/one path/two"
        )
        preview = ssh.preview( sudo=True )
        self.assertEqual( preview, expected )

    def test_ssh_test_should_work( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.set_to_test()
        expected = (
            "ssh -q some_user@8.8.8.8 exit"
        )
        preview = ssh.preview()
        self.assertEqual( preview, expected )
