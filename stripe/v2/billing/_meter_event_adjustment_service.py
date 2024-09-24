# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.v2.billing._meter_event_adjustment_v2 import MeterEventAdjustmentV2
from typing import cast
from typing_extensions import Literal, TypedDict


class MeterEventAdjustmentService(StripeService):
    class CreateParams(TypedDict):
        cancel: "MeterEventAdjustmentService.CreateParamsCancel"
        """
        Specifies which event to cancel.
        """
        event_name: str
        """
        The name of the meter event. Corresponds with the `event_name` field on a meter.
        """
        type: Literal["cancel"]
        """
        Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
        """

    class CreateParamsCancel(TypedDict):
        identifier: str
        """
        Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.
        """

    def create(
        self,
        params: "MeterEventAdjustmentService.CreateParams",
        options: RequestOptions = {},
    ) -> MeterEventAdjustmentV2:
        """
        Creates a meter event adjustment to cancel a previously sent meter event.
        """
        return cast(
            MeterEventAdjustmentV2,
            self._request(
                "post",
                "/v2/billing/meter_event_adjustments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "MeterEventAdjustmentService.CreateParams",
        options: RequestOptions = {},
    ) -> MeterEventAdjustmentV2:
        """
        Creates a meter event adjustment to cancel a previously sent meter event.
        """
        return cast(
            MeterEventAdjustmentV2,
            await self._request_async(
                "post",
                "/v2/billing/meter_event_adjustments",
                base_address="api",
                params=params,
                options=options,
            ),
        )
