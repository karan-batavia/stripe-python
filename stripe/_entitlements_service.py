# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.entitlements._feature_service import FeatureService


class EntitlementsService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.features = FeatureService(self._requestor)
