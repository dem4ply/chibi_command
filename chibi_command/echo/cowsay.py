from chibi_command import command


def cowsay( text, capture=False):
    if capture:
        stdout = 'pipe'
    else:
        stdout = None
    return command( 'cowsay', text, stdout=stdout )
