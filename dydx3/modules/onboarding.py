import base64

# from web3 import Web3

from dydx3.constants import OFF_CHAIN_ONBOARDING_ACTION
from dydx3.constants import OFF_CHAIN_KEY_DERIVATION_ACTION
from dydx3.eth_signing import SignOnboardingAction
from dydx3.helpers.requests import request
from dydx3.starkex.helpers import private_key_to_public_key_pair_hex


class Onboarding(object):

    def __init__(
        self,
        host,
        eth_signer,
        network_id,
        default_address,
        api_timeout,
        stark_public_key=None,
        stark_public_key_y_coordinate=None,
    ):
        self.host = host
        self.default_address = default_address
        self.api_timeout = api_timeout
        self.stark_public_key = stark_public_key
        self.stark_public_key_y_coordinate = stark_public_key_y_coordinate

        self.signer = SignOnboardingAction(eth_signer, network_id)

    # ============ Request Helpers ============

    def _post(
        self,
        endpoint,
        data,
        opt_ethereum_address,
    ):
        ethereum_address = opt_ethereum_address or self.default_address

        signature = self.signer.sign(
            ethereum_address,
            action=OFF_CHAIN_ONBOARDING_ACTION,
        )

        request_path = '/'.join(['/v3', endpoint])
        return request(
            self.host + request_path,
            'post',
            {
                'DYDX-SIGNATURE': signature,
                'DYDX-ETHEREUM-ADDRESS': ethereum_address,
            },
            data,
            self.api_timeout,
        )

    # ============ Requests ============

    def create_user(
        self,
        stark_public_key=None,
        stark_public_key_y_coordinate=None,
        ethereum_address=None,
        referred_by_affiliate_link=None,
        country=None,
    ):
        raise NotImplementedError('This function is not yet implemented.')

    # ============ Key Derivation ============

    def derive_stark_key(
        self,
        ethereum_address=None,
    ):
        raise NotImplementedError('This function is not yet implemented.')

    def recover_default_api_key_credentials(
        self,
        ethereum_address=None,
    ):
        raise NotImplementedError('This function is not yet implemented.')
