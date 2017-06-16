from chibi_command import command


def cowsay( text ):
    text.repace( '\'', '\\\'' )
    text = "'{}'".format( text )
    return command( 'cowsay', text )
