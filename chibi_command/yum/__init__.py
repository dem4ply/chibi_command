from chibi_command import command


def yum( opcion, *args ):
    return command( 'yum', opcion, '-y', *args )


def update():
    return yum( 'update' )


def install( *pkgs ):
    return yum( 'install', *pkgs )
