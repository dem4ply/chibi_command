from unittest import TestCase

from chibi_command.rsync import Rsync
from chibi_command.ssh import Ssh
from chibi.file.temp import Chibi_temp_path


class Test_rsync( TestCase ):
    def test_single_option_work( self ):
        options = Rsync.options( '-a' )
        func = Rsync.archive_mode()
        self.assertEqual( options.preview(), func.preview() )

        options = Rsync.options( '-h' )
        func = Rsync.human()
        self.assertEqual( options.preview(), func.preview() )

        options = Rsync.options( '-v' )
        func = Rsync.verbose()
        self.assertEqual( options.preview(), func.preview() )

        options = Rsync.options( '-z' )
        func = Rsync.compress()
        self.assertEqual( options.preview(), func.preview() )

        options = Rsync.options( '--progress' )
        func = Rsync.progress()
        self.assertEqual( options.preview(), func.preview() )

    def test_clone_dir( self ):
        func = Rsync.clone_dir()
        self.assertEqual( 'rsync -a -u', func.preview() )

    def test_ignore_existing( self ):
        func = Rsync.ignore_existing()
        self.assertEqual( 'rsync --ignore-existing', func.preview() )

    def test_copy_no_existing( self ):
        func = Rsync.archive_mode().verbose().ignore_existing()
        self.assertEqual( 'rsync -a -v --ignore-existing', func.preview() )

    def test_when_add_ssh_should_add_argument_e( self ):
        temp = Chibi_temp_path()
        identity_file = temp.temp_file()
        ssh = Ssh(
            user="some_user", host="some_host", identity_file=identity_file )
        func = Rsync.archive_mode().verbose().ignore_existing().ssh( ssh )
        self.assertEqual(
            f'rsync e ssh -i {identity_file} -t some_user@some_host -a '
            '-v --ignore-existing',
            func.preview() )
