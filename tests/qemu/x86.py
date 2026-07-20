from unittest import TestCase
from chibi_command.qemu.x86 import Qemu_system_x86


class Test_qemu_86( TestCase ):
    def test_should_return_expected_sport_preview( self ):
        expected = (
            "qemu-system-x86_64 -enable-kvm -m 2048 -smp 4 "
            "-drive file=arch_min.qcow2,format=qcow2 "
            "-cdrom arch.iso "
            "-nic user,hostfwd=tcp:127.0.0.1:2222-:22 -boot d"
        )
        command = Qemu_system_x86.enable_kvm().memory( 2048 )
        command = command.smp( 4 )
        command = command.drive( file='arch_min.qcow2' )
        command = command.cdrom( 'arch.iso' )
        command = command.nic( 'user,hostfwd=tcp:127.0.0.1:2222-:22' )
        command = command.boot( 'd' )

        preview = command.preview()
        self.assertEqual( preview, expected )
