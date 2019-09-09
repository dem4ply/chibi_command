from chibi_command import Command


class Mariadb( Command ):
    command = 'mysql'
    captive = False

    @classmethod
    def user( cls, user ):
        return cls( **{ '-u': user } )


class Mysql( Mariadb ):
    pass
