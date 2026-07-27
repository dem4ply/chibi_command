from chibi_hybrid.chibi_hybrid import Chibi_hybrid

from chibi_command import Command


class Makepkg( Command ):
    command = 'makepkg'
    captive = False

    @Chibi_hybrid
    def syncdeps( cls ):
        return cls( '--syncdeps' )

    @syncdeps.instancemethod
    def syncdeps( self ):
        self.add_args( '--syncdeps' )
        return self

    @Chibi_hybrid
    def install( cls ):
        return cls( '--install' )

    @install.instancemethod
    def install( self ):
        self.add_args( '--install' )
        return self

    @Chibi_hybrid
    def clean( cls ):
        return cls( '--clean' )

    @clean.instancemethod
    def clean( self ):
        self.add_args( '--clean' )
        return self

    @Chibi_hybrid
    def no_confirm( cls ):
        return cls( '--noconfirm' )

    @no_confirm.instancemethod
    def no_confirm( self ):
        self.add_args( '--noconfirm' )
        return self
