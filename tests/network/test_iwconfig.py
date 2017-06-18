from chibi_command.network import iwconfig
from chibi_dict import Chibi_dict
from expects import expect, contain, have_keys, have_properties, have_property
from unittest.mock import patch
import pytest


@pytest.fixture
def iwconfig_output():
    return (
        'wlan0     IEEE 802.11bgn  ESSID:"TP-LINK_E758"  \n          '
        'Mode:Managed  Frequency:2.417 GHz  Access Point: 84:16:F9:EB:E7:58 '
        '  \n          Bit Rate=72 Mb/s   Tx-Power=1496 dBm   \n          '
        'Retry short limit:7   RTS thr:off   Fragment thr:off\n          '
        'Encryption key:off\n          Power Management:on\n          '
        'Link Quality=66/70  Signal level=-44 dBm  \n          '
        'Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0\n        '
        '  Tx excessive retries:0  Invalid misc:0   Missed beacon:0\n\n'
        'wlan1mon  IEEE 802.11bgn  Mode:Monitor  Frequency:2.457 GHz  '
        'Tx-Power=20 dBm   \n          Retry short limit:7   RTS thr:off   '
        'Fragment thr:off\n          Power Management:off\n          \n',
        None
    )


@pytest.fixture
def expected_iwconfig_output():
    return {
        'wlan0': {
            'access_point': ' 84:16:f9:eb:e7:58', 'bit_rate': '72 mb/s',
            'fragment_thr': 'off', 'retry_short_limit': '7',
            'frequency': '2.417 ghz', 'rts_thr': 'off',
            'tx_excessive_retries': '0', 'rx_invalid_crypt': '0',
            'link_quality': '66/70', 'essid': '"tp-link_e758"',
            'mode': 'managed', 'rx_invalid_nwid': '0', 'missed_beacon': '0',
            'rx_invalid_frag': '0', 'ieee': '802.11bgn',
            'tx-power': '1496 dbm', 'power_management': 'on',
            'encryption_key': 'off', 'signal_level': '-44 dbm',
            'invalid_misc': '0'
        },
        'wlan1mon': {
            'fragment_thr': 'off', 'ieee': '802.11bgn',
            'retry_short_limit': '7', 'power_management': 'off',
            'frequency': '2.457 ghz', 'rts_thr': 'off', 'tx-power': '20 dbm',
            'mode': 'monitor'
    }
}


@pytest.fixture
def expected_interfaces():
    return [ 'wlan0', 'wlan1mon', ]


@pytest.fixture
def result_iwconfig( iwconfig_output ):
    with patch( 'chibi_command.network.command' ) as command_mock:
        command_mock.return_value = iwconfig_output
        result = iwconfig()
    return result


class Test_iwconfig:
    def test_the_return_should_have_the_expected_interfaces(
            self, result_iwconfig, expected_interfaces ):
        for interface in expected_interfaces:
            expect( result_iwconfig.keys() ).to( contain( interface ) )

    def test_the_return_can_be_read_like_a_object( self, result_iwconfig,
                                                   expected_interfaces ):
        for interface in expected_interfaces:
            expect( result_iwconfig ).to( have_property( interface ) )

    def test_the_return_is_equal_to_the_expected( self, result_iwconfig,
                                                  expected_iwconfig_output ):
        for interce, data in expected_iwconfig_output.items():
            expect( result_iwconfig[ interce ] ).to( have_keys( data ) )

    def test_the_return_can_read_like_object( self, result_iwconfig,
                                              expected_iwconfig_output ):
        for interce, data in expected_iwconfig_output.items():
            expect( result_iwconfig[ interce ] ).to( have_properties( data ) )
