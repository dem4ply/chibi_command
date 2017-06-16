from chibi_command import command
from expects import expect, be_a, equal, be_none, be_empty
import pytest


@pytest.fixture
def sample_text():
    return "SAMPLE_TEXT"


@pytest.fixture
def simple_echo(sample_text):
    result = command( 'echo', sample_text )
    return result


@pytest.fixture
def cp_with_error():
    result = command( 'cp', 'FILE_NOT_FOUND', 'TO_ANOTHER_IMPOSIBLE_PLACE' )
    return result

@pytest.fixture
def stderr_cp_with_error():
    result = command( 'cp', 'FILE_NOT_FOUND', 'TO_ANOTHER_IMPOSIBLE_PLACE',
                      stderr='pipe' )
    return result


@pytest.fixture
def stdout_simple_echo( sample_text ):
    result = command( 'echo', sample_text, stdout='pipe' )
    return result


class Test_command():

    def test_return_a_tuple( self, simple_echo ):
        """
        deberia de regresar una tupla
        """
        expect( simple_echo).to( be_a( tuple ) )

    def test_return_a_tuple_of_2_elements( self, simple_echo ):
        """
        deberia te tener 2 elementos la tupla
        """
        expect( len(simple_echo) ).to( equal( 2 ) )

    def test_if_not_send_the_stdout_params_return_none( self, simple_echo ):
        """
        cuando no se especifique el parametro de stdout deberia de regresar
        None en el primer elemento de la tupla
        """
        out, error = simple_echo
        expect( out ).to( be_none )

    def test_if_not_send_the_stderr_params_return_none( self,
                                                        cp_with_error):
        """
        cuando no se especifique el parametro de stderr deberia de regresar
        None en el segundo elemento de la tupla
        """
        out, error = cp_with_error
        expect( error ).to( be_none )

    def test_if_send_pipe_in_the_stdout_return_the_value_of_the_command(
            self, stdout_simple_echo, sample_text ):
        """
        deberia se mande el parametro de PIPE en el stdout deberia de regresar
        el resultado del comando
        """
        out, error = stdout_simple_echo
        expect( out ).not_to( be_empty )
        expect( out ).to( equal( "{}\n".format( sample_text ) ) )

    def test_if_send_the_stderr_params_return_text( self,
                                                    stderr_cp_with_error ):
        """
        deberia se mande el parametro de PIPE en el stderr deberia de regresar
        el error del commando
        """
        out, error = stderr_cp_with_error
        expect( error ).to( be_a( str ) )
        expect( error ).not_to( be_empty )
