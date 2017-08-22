import chibi_command


def command( str_command, *args ):
    return chibi_command.command_exit_code( 'command',
                                            ( *args, str_command ) )
