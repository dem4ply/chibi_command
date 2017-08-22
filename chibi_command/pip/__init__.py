import pip


def install(*packages):
    return pip.main( [ 'install', *packages] )


def upgrade(*packages):
    return pip.main( [ 'install', '--upgrade', *packages] )
