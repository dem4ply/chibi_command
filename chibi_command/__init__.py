from subprocess import Popen, PIPE


def command(str_command, *args, stdout=None, stderr=None ):
    if isinstance( stdout, str) and stdout.lower() == 'pipe':
        stdout = PIPE
    if isinstance( stderr, str) and stderr.lower() == 'pipe':
        stdout = PIPE

    proc = Popen( ( str_command, *args ), stdout=stdout, stderr=stdout )
    result, error = proc.communicate()
    if result is not None:
        result = result.decode( 'utf-8' )
    if error is not None:
        error = error.decode( 'utf-8' )
    return result, error
