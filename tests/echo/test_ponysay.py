import pytest
from expects import expect, be_none, contain

from chibi_command.echo import ponysay


@pytest.fixture
def str_hello():
    return "hello world"


@pytest.fixture
def ponysay_hello( str_hello ):
    return ponysay( str_hello )


@pytest.fixture
def capture_ponysay_hello( str_hello ):
    return ponysay( str_hello, capture=True )


class Test_ponysay:

    def test_can_send_spaces( self, ponysay_hello ):
        """
        no deberia de lanzar alguna exceptions
        """
        out, error = ponysay_hello
        expect( out ).to( be_none )
        expect( error ).to( be_none )


    def test_capture_the_output( self, capture_ponysay_hello, str_hello ):
        """
        deberia de capturar el output del ponysay
        """
        out, err = capture_ponysay_hello
        expect( out ).to( contain( str_hello ) )
