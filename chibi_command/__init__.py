from subprocess import Popen, PIPE


class Command_result:
    def __init__( self, result, error, return_code ):
        self.result = result
        self.error = error
        self.return_code = return_code

    def __str__( self ):
        return result


class Command:
    command = None
    captive = False

    def __init__( self, *args, captive=None, **kw ):
        if captive is not None:
            self.captive = captive
        self._args = args
        self._kw = kw

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

    def build_tuple( self, *args ):
        return ( self.command, *self._args, *args )

    def run( self, *args, **kw ):
        if kw.get( '___mock', False ):
            return " ".join( self.build_tuple( *args ) )
        proc = self._build_proccess( *args )
        result, error = proc.communicate()
        if result is not None:
            result = result.decode( 'utf-8' )
        if error is not None:
            error = error.decode( 'utf-8' )
        return Command_result( result, error, proc.returncode )

    def __call__( self, *args, **kw ):
        return self.run( *args, **kw )
