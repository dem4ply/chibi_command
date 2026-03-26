from unittest import TestCase
from chibi_command.ssh import Ssh
from chibi_command.common import Cp
from chibi.file.temp import Chibi_temp_path


class Test_ssh( TestCase ):
    def test_preview_should_have_expected_command( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        self.assertEqual( ssh.preview(), 'ssh -t some_user@8.8.8.8' )

    def test_preview_when_add_commands_should_be_append( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append( Cp( 'path/one', 'path/two' ) )
        expected = "ssh -t some_user@8.8.8.8 cp -v path/one path/two"
        preview = ssh.preview()
        self.assertEqual( preview, expected )

    def test_preview_when_use_sudo_on_run_should_append_sudo( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append( Cp( 'path/one', 'path/two' ) )
        expected = "ssh -t some_user@8.8.8.8 sudo cp -v path/one path/two"
        preview = ssh.preview( sudo=True )
        self.assertEqual( preview, expected )

    def test_append_from_commands_work_with_multi( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append(
            Cp( 'path/one', 'path/two' ),
            Cp( 'path/one', 'path/two' ),
        )
        expected = (
            "ssh -t some_user@8.8.8.8 sudo cp -v path/one path/two && "
            "sudo cp -v path/one path/two"
        )
        preview = ssh.preview( sudo=True )
        self.assertEqual( preview, expected )

    def test_ssh_test_should_work( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.set_to_test()
        expected = (
            "ssh -q -t some_user@8.8.8.8 exit"
        )
        preview = ssh.preview()
        self.assertEqual( preview, expected )

    def test_user_should_return_the_user( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        self.assertEqual( ssh.user, "some_user" )

    def test_host_should_return_the_host( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        self.assertEqual( ssh.host, "8.8.8.8" )

    def test_without_identity_file_should_be_fine( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        result = ssh.set_to_test().preview()
        self.assertEqual( result, "ssh -q -t some_user@8.8.8.8 exit" )

    def test_add_identity_file_to_intance_should_work( self ):
        temp = Chibi_temp_path()
        identity_file = temp.temp_file()
        ssh = Ssh( 'some_user', '8.8.8.8' )
        result = ssh.set_to_test()
        result.identity_file = identity_file
        self.assertEqual(
            result.preview(),
            f"ssh -i {identity_file} -q -t some_user@8.8.8.8 exit" )

    def test_set_identity_file_on_init( self ):
        temp = Chibi_temp_path()
        identity_file = temp.temp_file()
        ssh = Ssh( 'some_user', '8.8.8.8', identity_file=identity_file )
        result = ssh.set_to_test()
        self.assertEqual(
            result.preview(),
            f"ssh -i {identity_file} -q -t some_user@8.8.8.8 exit" )

    def test_preview_when_use_su_on_run_should_append_su( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append( Cp( 'path/one', 'path/two' ) )
        ssh.sudo_command = "su"

        expected = 'ssh -t some_user@8.8.8.8 su -c " cp -v path/one path/two "'
        preview = ssh.preview( sudo=True )
        self.assertEqual( preview, expected )

    def test_preview_when_is_set_sudo_should_return_su_commadn( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append( Cp( 'path/one', 'path/two' ) )
        ssh.sudo_command = "su"

        expected = 'ssh -t some_user@8.8.8.8 su -c " cp -v path/one path/two "'
        preview = ssh.preview()
        self.assertEqual( preview, expected )


    def test_append_from_commands_work_with_multi_with_su( self ):
        ssh = Ssh( 'some_user', '8.8.8.8' )
        ssh.commands.append(
            Cp( 'path/one', 'path/two' ),
            Cp( 'path/one', 'path/two' ),
        )
        ssh.sudo_command = "su"
        expected = (
            'ssh -t some_user@8.8.8.8 su -c " cp -v path/one path/two && '
            'cp -v path/one path/two "'
        )
        preview = ssh.preview( sudo=True )
        self.assertEqual( preview, expected )
