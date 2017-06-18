from chibi_command import command


def ponysay( text, capture=False):
    if capture:
        stdout = 'pipe'
    else:
        stdout = None
    return command( 'ponysay', text, stdout=stdout )
