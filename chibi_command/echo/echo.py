from chibi_command import command


def echo( text, capture=False):
    if capture:
        stdout = 'pipe'
    else:
        stdout = None
    return command( 'echo', text, stdout=stdout )
