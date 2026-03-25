from unittest.mock import patch, Mock
import functools
import logging


logger = logging.getLogger( 'chibi_command.unittests' )


def patch_empty( func, target='chibi_command.Popen' ):
    """
    decorador para parchear la funcion Popen de chibi command
    """
    @functools.wraps( func )
    def wrapper( *args, **kw ):
        patcher = patch( target )
        with patcher as popen:
            proccess = Mock()
            popen.return_value = proccess
            proccess.returncode = 0
            proccess.communicate.return_value = ( b"", b"" )

            func( *args, popen, **kw )
    return wrapper
