# -*- coding: utf-8 -*-
"""Handle dashboard utility related tests.

Copyright (C) 2018 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
from dashboard.utils import clean_bounty_url, get_ordinal_repr, get_web3, humanize_event_name
from test_plus.test import TestCase
from web3 import WebsocketProvider
from web3.main import Web3
from web3.providers.rpc import HTTPProvider


class DashboardUtilsTest(TestCase):
    """Define tests for dashboard utils."""

    @staticmethod
    def test_get_web3():
        """Test the dashboard utility get_web3."""
        networks = ['mainnet', 'rinkeby', 'ropsten']
        for network in networks:
            web3_provider = get_web3(network)
            assert isinstance(web3_provider, Web3)
            assert len(web3_provider.providers) == 1
            assert isinstance(web3_provider.providers[0], WebsocketProvider)
            assert web3_provider.providers[0].endpoint_uri == f'wss://{network}.infura.io/_ws'

    @staticmethod
    def test_get_ordinal_repr():
        """Test the dashboard utility get_ordinal_repr."""
        assert get_ordinal_repr(1) == '1st'
        assert get_ordinal_repr(2) == '2nd'
        assert get_ordinal_repr(3) == '3rd'
        assert get_ordinal_repr(4) == '4th'
        assert get_ordinal_repr(10) == '10th'
        assert get_ordinal_repr(11) == '11th'
        assert get_ordinal_repr(21) == '21st'
        assert get_ordinal_repr(22) == '22nd'
        assert get_ordinal_repr(23) == '23rd'
        assert get_ordinal_repr(24) == '24th'

    @staticmethod
    def test_clean_bounty_url():
        """Test the cleaning of a bounty-esque URL of # sections."""
        assert clean_bounty_url(
            'https://github.com/gitcoinco/web/issues/9999#issuecomment-999999999'
        ) == 'https://github.com/gitcoinco/web/issues/9999'

    @staticmethod
    def test_humanize_event_name():
        """Test the humanized representation of an event name."""
        assert humanize_event_name('start_work') == 'WORK STARTED'
        assert humanize_event_name('remarket_funded_issue') == 'REMARKET_FUNDED_ISSUE'
