from unittest import TestCase

from chibi_command.disk.lsblk import Lsblk


class Test_lsblk( TestCase ):
    def test_should_work( self ):
        result = Lsblk().run()
        self.assertTrue( result )

    def test_retrieve_sda_from_result_should_work( self ):
        result = Lsblk().run()
        sda = result[ 'sda' ]
        self.assertTrue( sda )
        list( sda )

    def test_blocks_can_be_iter_to_get_childrens( self ):
        result = Lsblk().run()
        sda = result[ 'sda' ]
        sda_childrens = list( sda.childs )
        self.assertTrue( sda_childrens )

    def test_block_children_should_have_uuid( self ):
        result = Lsblk().run()
        sda = result[ 'sda' ]
        sda_childrens = list( sda.childs )
        self.assertIn( "uuid", sda_childrens[0] )
