from chibi_command import command
from chibi_dict import Chibi_dict
import re


def iwconfig():
    command_result, error = command( 'iwconfig', stdout='pipe' )

    regex_separador_for_raw = re.compile( r'\s\s+' )
    regex_separador_items = re.compile( r'[:=]' )
    result = {}
    for raw_interface in command_result.split( '\n\n' ):
        if not raw_interface:
            continue
        list_values_interface = regex_separador_for_raw.split( raw_interface )
        interface_name = list_values_interface.pop( 0 )
        type_ieee = list_values_interface.pop( 0 )
        interface_result = Chibi_dict( ieee=type_ieee.split()[1] )
        result[ interface_name ] = interface_result

        for item_value in list_values_interface:
            if not item_value:
                continue
            item_value = item_value.lower()
            split_item = tuple( regex_separador_items.split( item_value, 1 ) )
            key, value = split_item
            interface_result[ key.replace( ' ', '_' ) ] = value

    return Chibi_dict(result)
