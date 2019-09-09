from chibi_command import Command


class Mariadb( Command ):
    command = 'mariadb'
    captive = False

    @classmethod
    def user( cls, user ):
        return cls( *{ '-u': user } )
