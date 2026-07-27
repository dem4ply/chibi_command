from chibi.file import Chibi_path
from chibi_hybrid.chibi_hybrid import Chibi_hybrid

from chibi_command import Command


class Qemu_system_x86( Command ):
    command = 'qemu-system-x86_64'
    captive = False
    # delegate = System_run

    @Chibi_hybrid
    def memory( cls, amount ):
        return cls( '-m', amount )

    @memory.instancemethod
    def memory( self, amount ):
        self.add_args( '-m', amount )
        return self

    @Chibi_hybrid
    def cdrom( cls, iso ):
        return cls( '-cdrom', iso )

    @cdrom.instancemethod
    def cdrom( self, iso ):
        self.add_args( '-cdrom', iso )
        return self

    @Chibi_hybrid
    def boot( cls, kind ):
        return cls( '-boot', kind )

    @boot.instancemethod
    def boot( self, kind ):
        self.add_args( '-boot', kind )
        return self

    @Chibi_hybrid
    def nic( cls, parameter ):
        return cls( '-nic', parameter )

    @nic.instancemethod
    def nic( self, parameter ):
        self.add_args( '-nic', parameter )
        return self

    @Chibi_hybrid
    def smp( cls, parameter ):
        return cls( '-smp', parameter )

    @smp.instancemethod
    def smp( self, parameter ):
        self.add_args( '-smp', parameter )
        return self

    @Chibi_hybrid
    def enable_kvm( cls ):
        return cls( '-enable-kvm' )

    @enable_kvm.instancemethod
    def enable_kvm( self ):
        self.add_args( '-enable-kvm' )
        return self

    @Chibi_hybrid
    def drive( cls, *args, file=None, format=None, **kw ):
        return cls().drive( *args, file=file, format=format, **kw )

    @drive.instancemethod
    def drive( self, *args, file=None, format=None, **kw ):
        if file:
            if not isinstance( file, Chibi_path ):
                file = Chibi_path( file )
            file.raise_not_exists()
            if format is None:
                if file.extension == 'qcow2':
                    format = 'qcow2'
            else:
                raise NotImplementedError
            self.add_args( '-drive', f"file={file},format={format}" )
        else:
            raise NotImplementedError
        return self

    @Chibi_hybrid
    def daemonize( cls ):
        return cls( '-daemonize' )

    @daemonize.instancemethod
    def daemonize( self ):
        self.add_args( '-daemonize' )
        return self

    @Chibi_hybrid
    def pidfile( cls, path ):
        return cls( '-pidfile', path )

    @pidfile.instancemethod
    def pidfile( self, path ):
        self.add_args( '-pidfile', path )
        return self

    @Chibi_hybrid
    def monitor( cls, path ):
        return cls( '-monitor', path )

    @monitor.instancemethod
    def monitor( self, path ):
        # -monitor unix:/tmp/qemu-arch.sock,server,nowait
        self.add_args( '-monitor', path )
        return self
