from subprocess import Popen, PIPE


class Command_result:
    def __init__( self, result, error, return_code ):
        self.result = result
        self.error = error
        self.return_code = return_code

    def __str__( self ):
        return self.result

    def __bool__( self ):
        return self.return_code == 0


class Command:
    command = ''
    captive = False
    args = None
    kw = None
    kw_format = "{key} {value}"
    result_class = Command_result

    def __init__( self, *args, captive=None, command=None, **kw ):
        if captive is not None:
            self.captive = captive

        if command is not None:
            self.command = command

        if not command and not self.command and args:
            self.command = args[0]
            args = args[1:]
        if self.args is None:
            self.args = tuple()
        else:
            self.args = tuple( self.args )
        self.args = ( *self.args, *args )

        if self.kw is None:
            self.kw = {}
        else:
            self.kw = self.kw.copy()
        self.kw.update( kw )

    @property
    def stdout( self ):
        if self.captive:
            return PIPE
        return None

    @property
    def stderr( self ):
        if self.captive:
            return PIPE
        return None

    def _build_proccess( self, *args ):
        proc = Popen(
            self.build_tuple( *args ),
            stdout=self.stdout, stderr=self.stderr )
        return proc

    def build_tuple( self, *args, **kw ):
        return ( self.command, *self.build_kw( **kw ), *self.args, *args )

    def build_kw( self, **kw ):
        params = self.kw.copy()
        params.update( kw )
        return tuple(
            self.kw_format.format( key=k, value=v )
            for k, v in params.items() )

    def preview( self, *args, **kw ):
        tuples = self.build_tuple( *args )
        return " ".join( tuples )

    def run( self, *args, **kw ):
        proc = self._build_proccess( *args )
        result, error = proc.communicate()
        if result is not None:
            result = result.decode( 'utf-8' )
        if error is not None:
            error = error.decode( 'utf-8' )
        return self.result_class( result, error, proc.returncode )

    def __call__( self, *args, **kw ):
        return self.run( *args, **kw )

    def __hash__( self ):
        return hash( self.preview() )

    def __eq__( self, other ):
        if isinstance( other, Command ):
            return self.preview() == other.preview()
        else:
            raise NotImplementedError

    def __copy__( self ):
        args = tuple( *self.args )
        kw = self.kw.copy()
        new_command = type( self )(
            *args, command=self.command, captive=self.captive, **kw )
        return new_command
