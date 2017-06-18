import pytest
from expects import expect, be_none, contain

from chibi_command.echo.cowsay import cowsay


@pytest.fixture
def str_hello():
    return "hello world"


@pytest.fixture
def cowsay_hello( str_hello ):
    return cowsay( str_hello )


@pytest.fixture
def capture_cowsay_hello( str_hello ):
    return cowsay( str_hello, capture=True )


class Test_cowsay:

    def test_can_send_spaces( self, cowsay_hello ):
        """
        no deberia de lanzar alguna exceptions
        """
        out, error = cowsay_hello
        expect( out ).to( be_none )
        expect( error ).to( be_none )


    def test_capture_the_output( self, capture_cowsay_hello, str_hello ):
        """
        deberia de capturar el output del cowsay
        """
        out, err = capture_cowsay_hello
        expect( out ).to( contain( str_hello ) )
