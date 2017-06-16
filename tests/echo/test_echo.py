import pytest
from expects import expect, be_none, start_with

from chibi_command.echo.echo import echo


@pytest.fixture
def str_hello():
    return "hello world"



@pytest.fixture
def echo_hello( str_hello ):
    return echo( str_hello )


@pytest.fixture
def capture_echo_hello( str_hello ):
    return echo( str_hello, capture=True )


class Test_echo:

    def test_can_send_spaces( self, echo_hello ):
        """
        no deberia de lanzar alguna exceptions
        """
        out, error = echo_hello
        expect( out ).to( be_none )
        expect( error ).to( be_none )


    def test_capture_the_output( self, capture_echo_hello, str_hello ):
        """
        deberia de capturar el output del echo
        """
        out, err = capture_echo_hello
        expect( out ).to( start_with( str_hello ) )
