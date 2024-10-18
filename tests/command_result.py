from unittest import TestCase
from chibi_command import Command_result, Command_json_result, Result_error
from chibi.atlas import Chibi_atlas


class Test_result( TestCase ):
    def test_when_return_code_is_1_should_be_false( self ):
        result = Command_result( '', '', 1, None )
        self.assertFalse( result )

    def test_when_return_code_is_0_should_be_true( self ):
        result = Command_result( '', '', 0, None )
        self.assertTrue( result )

    def test_throw_when_result_is_true_should_no_raise( self ):
        result = Command_result( '', '', 0, None )
        result.throw()

    def test_throw_when_result_is_false_should_no_raise( self ):
        result = Command_result( '', '', 1, None )
        with self.assertRaises( Result_error ):
            result.throw()


class Test_result_json( TestCase ):
    def test_on_send_json_should_be_chibi_atlas( self ):
        result = Command_json_result( '{"asdf":"zxcv"}', '', 0, None )
        self.assertIsInstance( result.result, Chibi_atlas )

    def test_should_containt_the_expected_keys( self ):
        result = Command_json_result( '{"asdf":"zxcv"}', '', 0, None )
        expected = { 'asdf': 'zxcv' }
        self.assertEqual( result.result, expected )
