# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._invoice_line_item import InvoiceLineItem
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class InvoiceUpcomingLinesService(StripeService):
    class ListParams(TypedDict):
        automatic_tax: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsAutomaticTax"
        ]
        """
        Settings for automatic tax lookup for this invoice preview.
        """
        coupon: NotRequired["str"]
        """
        The identifier of the coupon to apply to this phase of the subscription schedule. This field has been deprecated and will be removed in a future API version. Use `discounts` instead.
        """
        currency: NotRequired["str"]
        """
        The currency to preview this invoice in. Defaults to that of `customer` if not specified.
        """
        customer: NotRequired["str"]
        """
        The identifier of the customer whose upcoming invoice you'd like to retrieve. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
        """
        customer_details: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsCustomerDetails"
        ]
        """
        Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsDiscount]"
        ]
        """
        The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the customer or subscription. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        invoice_items: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsInvoiceItem]"
        ]
        """
        List of invoice items to add or update in the upcoming invoice preview.
        """
        issuer: NotRequired["InvoiceUpcomingLinesService.ListParamsIssuer"]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
        """
        preview_mode: NotRequired["Literal['next', 'recurring']"]
        """
        Customizes the types of values to include when calculating the invoice. Defaults to `next` if unspecified.
        """
        schedule: NotRequired["str"]
        """
        The identifier of the schedule whose upcoming invoice you'd like to retrieve. Cannot be used with subscription or subscription fields.
        """
        schedule_details: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetails"
        ]
        """
        The schedule creation or modification params to apply as a preview. Cannot be used with `subscription` or `subscription_` prefixed fields.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        subscription: NotRequired["str"]
        """
        The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.
        """
        subscription_billing_cycle_anchor: NotRequired[
            "Literal['now', 'unchanged']|int"
        ]
        """
        For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. For existing subscriptions, the value can only be set to `now` or `unchanged`. This field has been deprecated and will be removed in a future API version. Use `subscription_details.billing_cycle_anchor` instead.
        """
        subscription_cancel_at: NotRequired["Literal['']|int"]
        """
        A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period. This field has been deprecated and will be removed in a future API version. Use `subscription_details.cancel_at` instead.
        """
        subscription_cancel_at_period_end: NotRequired["bool"]
        """
        Boolean indicating whether this subscription should cancel at the end of the current period. This field has been deprecated and will be removed in a future API version. Use `subscription_details.cancel_at_period_end` instead.
        """
        subscription_cancel_now: NotRequired["bool"]
        """
        This simulates the subscription being canceled or expired immediately. This field has been deprecated and will be removed in a future API version. Use `subscription_details.cancel_now` instead.
        """
        subscription_default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        If provided, the invoice returned will preview updating or creating a subscription with these default tax rates. The default tax rates will apply to any line item that does not have `tax_rates` set. This field has been deprecated and will be removed in a future API version. Use `subscription_details.default_tax_rates` instead.
        """
        subscription_details: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionDetails"
        ]
        """
        The subscription creation or modification params to apply as a preview. Cannot be used with `schedule` or `schedule_details` fields.
        """
        subscription_items: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsSubscriptionItem]"
        ]
        """
        A list of up to 20 subscription items, each with an attached price. This field has been deprecated and will be removed in a future API version. Use `subscription_details.items` instead.
        """
        subscription_prebilling: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionPrebilling"
        ]
        """
        The pre-billing to apply to the subscription as a preview. This field has been deprecated and will be removed in a future API version. Use `subscription_details.prebilling` instead.
        """
        subscription_proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. This field has been deprecated and will be removed in a future API version. Use `subscription_details.proration_behavior` instead.
        """
        subscription_proration_date: NotRequired["int"]
        """
        If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period and within the current phase of the schedule backing this subscription, if the schedule exists. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration_behavior` cannot be set to 'none'. This field has been deprecated and will be removed in a future API version. Use `subscription_details.proration_date` instead.
        """
        subscription_resume_at: NotRequired["Literal['now']"]
        """
        For paused subscriptions, setting `subscription_resume_at` to `now` will preview the invoice that will be generated if the subscription is resumed. This field has been deprecated and will be removed in a future API version. Use `subscription_details.resume_at` instead.
        """
        subscription_start_date: NotRequired["int"]
        """
        Date a subscription is intended to start (can be future or past). This field has been deprecated and will be removed in a future API version. Use `subscription_details.start_date` instead.
        """
        subscription_trial_end: NotRequired["Literal['now']|int"]
        """
        If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required. This field has been deprecated and will be removed in a future API version. Use `subscription_details.trial_end` instead.
        """

    class ListParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://stripe.com/docs/api/tax_rates), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices.
        """
        liability: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class ListParamsAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ListParamsCustomerDetails(TypedDict):
        address: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsCustomerDetailsAddress"
        ]
        """
        The customer's address.
        """
        shipping: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsCustomerDetailsShipping"
        ]
        """
        The customer's shipping information. Appears on invoices emailed to this customer.
        """
        tax: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsCustomerDetailsTax"
        ]
        """
        Tax details about the customer.
        """
        tax_exempt: NotRequired[
            "Literal['']|Literal['exempt', 'none', 'reverse']"
        ]
        """
        The customer's tax exemption. One of `none`, `exempt`, or `reverse`.
        """
        tax_ids: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsCustomerDetailsTaxId]"
        ]
        """
        The customer's tax IDs.
        """

    class ListParamsCustomerDetailsAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State, county, province, or region.
        """

    class ListParamsCustomerDetailsShipping(TypedDict):
        address: "InvoiceUpcomingLinesService.ListParamsCustomerDetailsShippingAddress"
        """
        Customer shipping address.
        """
        name: str
        """
        Customer name.
        """
        phone: NotRequired["str"]
        """
        Customer phone (including extension).
        """

    class ListParamsCustomerDetailsShippingAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State, county, province, or region.
        """

    class ListParamsCustomerDetailsTax(TypedDict):
        ip_address: NotRequired["Literal['']|str"]
        """
        A recent IP address of the customer used for tax reporting and tax location inference. Stripe recommends updating the IP address when a new PaymentMethod is attached or the address field on the customer is updated. We recommend against updating this field more frequently since it could result in unexpected tax location/reporting outcomes.
        """

    class ListParamsCustomerDetailsTaxId(TypedDict):
        type: Literal[
            "ad_nrt",
            "ae_trn",
            "ar_cuit",
            "au_abn",
            "au_arn",
            "bg_uic",
            "bo_tin",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "ch_vat",
            "cl_tin",
            "cn_tin",
            "co_nit",
            "cr_tin",
            "do_rcn",
            "ec_ruc",
            "eg_tin",
            "es_cif",
            "eu_oss_vat",
            "eu_vat",
            "gb_vat",
            "ge_vat",
            "hk_br",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kr_brn",
            "li_uid",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "no_vat",
            "no_voec",
            "nz_gst",
            "pe_ruc",
            "ph_tin",
            "ro_tin",
            "rs_pib",
            "ru_inn",
            "ru_kpp",
            "sa_vat",
            "sg_gst",
            "sg_uen",
            "si_tin",
            "sv_nit",
            "th_vat",
            "tr_tin",
            "tw_vat",
            "ua_vat",
            "us_ein",
            "uy_ruc",
            "ve_rif",
            "vn_tin",
            "za_vat",
        ]
        """
        Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`
        """
        value: str
        """
        Value of the tax ID.
        """

    class ListParamsDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsInvoiceItem(TypedDict):
        amount: NotRequired["int"]
        """
        The integer amount in cents (or local equivalent) of previewed invoice item.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Only applicable to new invoice items.
        """
        description: NotRequired["str"]
        """
        An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
        """
        discountable: NotRequired["bool"]
        """
        Explicitly controls whether discounts apply to this invoice item. Defaults to true, except for negative invoice items.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsInvoiceItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the invoice item in the preview.
        """
        invoiceitem: NotRequired["str"]
        """
        The ID of the invoice item to update in preview. If not specified, a new invoice item will be added to the preview of the upcoming invoice.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        period: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsInvoiceItemPeriod"
        ]
        """
        The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
        """
        price: NotRequired["str"]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsInvoiceItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Non-negative integer. The quantity of units for the invoice item.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        tax_code: NotRequired["Literal['']|str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates that apply to the item. When set, any `default_tax_rates` do not apply to this item.
        """
        unit_amount: NotRequired["int"]
        """
        The integer unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This unit_amount will be multiplied by the quantity to get the full amount. If you want to apply a credit to the customer's account, pass a negative unit_amount.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsInvoiceItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsInvoiceItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsInvoiceItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsInvoiceItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsInvoiceItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsInvoiceItemPeriod(TypedDict):
        end: int
        """
        The end of the period, which must be greater than or equal to the start. This value is inclusive.
        """
        start: int
        """
        The start of the period. This value is inclusive.
        """

    class ListParamsInvoiceItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ListParamsScheduleDetails(TypedDict):
        amendments: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendment]"
        ]
        """
        Changes to apply to the phases of the subscription schedule, in the order provided.
        """
        billing_behavior: NotRequired[
            "Literal['prorate_on_next_phase', 'prorate_up_front']"
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        end_behavior: NotRequired["Literal['cancel', 'release']"]
        """
        Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
        """
        phases: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhase]"
        ]
        """
        List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase.
        """
        prebilling: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsPrebilling]"
        ]
        """
        Provide any time periods to bill in advance.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        In cases where the `schedule_details` params update the currently active phase, specifies if and how to prorate at the time of the request.
        """

    class ListParamsScheduleDetailsAmendment(TypedDict):
        amendment_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentAmendmentEnd"
        ]
        """
        Details to identify the end of the time range modified by the proposed change. If not supplied, the amendment is considered a point-in-time operation that only affects the exact timestamp at `amendment_start`, and a restricted set of attributes is supported on the amendment.
        """
        amendment_start: "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentAmendmentStart"
        """
        Details to identify the earliest timestamp where the proposed change should take effect.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['amendment_start', 'automatic']"
        ]
        """
        For a point-in-time amendment, this attribute lets you set or update whether the subscription's billing cycle anchor is reset at the `amendment_start` timestamp.
        """
        discount_actions: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentDiscountAction]"
        ]
        """
        Changes to the coupons being redeemed or discounts being applied during the amendment time span.
        """
        item_actions: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemAction]"
        ]
        """
        Changes to the subscription items during the amendment time span.
        """
        metadata_actions: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentMetadataAction]"
        ]
        """
        Instructions for how to modify phase metadata
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Changes to how Stripe handles prorations during the amendment time span. Affects if and how prorations are created when a future phase starts. In cases where the amendment changes the currently active phase, it is used to determine whether or how to prorate now, at the time of the request. Also supported as a point-in-time operation when `amendment_end` is `null`.
        """
        set_pause_collection: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentSetPauseCollection"
        ]
        """
        Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
        """
        set_schedule_end: NotRequired[
            "Literal['amendment_end', 'amendment_start']"
        ]
        """
        Ends the subscription schedule early as dictated by either the accompanying amendment's start or end.
        """
        trial_settings: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentTrialSettings"
        ]
        """
        Settings related to subscription trials.
        """

    class ListParamsScheduleDetailsAmendmentAmendmentEnd(TypedDict):
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentAmendmentEndDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentAmendmentEndDuration"
        ]
        """
        Time span for the amendment starting from the `amendment_start`.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the amendment to end. Must be after the `amendment_start`.
        """
        type: Literal[
            "discount_end",
            "duration",
            "schedule_end",
            "timestamp",
            "trial_end",
            "trial_start",
            "upcoming_invoice",
        ]
        """
        Select one of three ways to pass the `amendment_end`.
        """

    class ListParamsScheduleDetailsAmendmentAmendmentEndDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class ListParamsScheduleDetailsAmendmentAmendmentEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsScheduleDetailsAmendmentAmendmentStart(TypedDict):
        amendment_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentAmendmentStartAmendmentEnd"
        ]
        """
        Details of another amendment in the same array, immediately after which this amendment should begin.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentAmendmentStartDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the amendment to start.
        """
        type: Literal[
            "amendment_end",
            "discount_end",
            "now",
            "schedule_end",
            "timestamp",
            "trial_end",
            "trial_start",
            "upcoming_invoice",
        ]
        """
        Select one of three ways to pass the `amendment_start`.
        """

    class ListParamsScheduleDetailsAmendmentAmendmentStartAmendmentEnd(
        TypedDict,
    ):
        index: int
        """
        The position of the previous amendment in the `amendments` array after which this amendment should begin. Indexes start from 0 and must be less than the index of the current amendment in the array.
        """

    class ListParamsScheduleDetailsAmendmentAmendmentStartDiscountEnd(
        TypedDict,
    ):
        discount: str
        """
        The ID of a specific discount.
        """

    class ListParamsScheduleDetailsAmendmentDiscountAction(TypedDict):
        add: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentDiscountActionAdd"
        ]
        """
        Details of the discount to add.
        """
        remove: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentDiscountActionRemove"
        ]
        """
        Details of the discount to remove.
        """
        set: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentDiscountActionSet"
        ]
        """
        Details of the discount to replace the existing discounts with.
        """
        type: Literal["add", "remove", "set"]
        """
        Determines the type of discount action.
        """

    class ListParamsScheduleDetailsAmendmentDiscountActionAdd(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to redeem.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount for a coupon that was already redeemed.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentDiscountActionAddDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        index: NotRequired["int"]
        """
        The index, starting at 0, at which to position the new discount. When not supplied, Stripe defaults to appending the discount to the end of the `discounts` array.
        """
        promotion_code: NotRequired["str"]
        """
        The promotion code to redeem.
        """

    class ListParamsScheduleDetailsAmendmentDiscountActionAddDiscountEnd(
        TypedDict,
    ):
        type: Literal["amendment_end"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsScheduleDetailsAmendmentDiscountActionRemove(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to remove from the `discounts` array.
        """
        discount: NotRequired["str"]
        """
        The ID of a discount to remove from the `discounts` array.
        """
        promotion_code: NotRequired["str"]
        """
        The ID of a promotion code to remove from the `discounts` array.
        """

    class ListParamsScheduleDetailsAmendmentDiscountActionSet(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to replace the `discounts` array with.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount to replace the `discounts` array with.
        """
        promotion_code: NotRequired["str"]
        """
        An ID of an existing promotion code to replace the `discounts` array with.
        """

    class ListParamsScheduleDetailsAmendmentItemAction(TypedDict):
        add: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionAdd"
        ]
        """
        Details of the subscription item to add. If an item with the same `price` exists, it will be replaced by this new item. Otherwise, it adds the new item.
        """
        remove: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionRemove"
        ]
        """
        Details of the subscription item to remove.
        """
        set: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionSet"
        ]
        """
        Details of the subscription item to replace the existing items with. If an item with the `set[price]` already exists, the `items` array is not cleared. Instead, all of the other `set` properties that are passed in this request will replace the existing values for the configuration item.
        """
        type: Literal["add", "remove", "set"]
        """
        Determines the type of item action.
        """

    class ListParamsScheduleDetailsAmendmentItemActionAdd(TypedDict):
        discounts: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionAddDiscount]"
        ]
        """
        The discounts applied to the item. Subscription item discounts are applied before subscription discounts.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired["List[str]"]
        """
        The tax rates that apply to this subscription item. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.
        """
        trial: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionAddTrial"
        ]
        """
        Options that configure the trial on the subscription item.
        """

    class ListParamsScheduleDetailsAmendmentItemActionAddDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionAddDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsScheduleDetailsAmendmentItemActionAddDiscountDiscountEnd(
        TypedDict,
    ):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionAddDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsScheduleDetailsAmendmentItemActionAddDiscountDiscountEndDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsScheduleDetailsAmendmentItemActionAddTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class ListParamsScheduleDetailsAmendmentItemActionRemove(TypedDict):
        price: str
        """
        ID of a price to remove.
        """

    class ListParamsScheduleDetailsAmendmentItemActionSet(TypedDict):
        discounts: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionSetDiscount]"
        ]
        """
        If an item with the `price` already exists, passing this will override the `discounts` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `discounts`.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        If an item with the `price` already exists, passing this will override the `metadata` on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        If an item with the `price` already exists, passing this will override the quantity on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `quantity`.
        """
        tax_rates: NotRequired["List[str]"]
        """
        If an item with the `price` already exists, passing this will override the `tax_rates` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `tax_rates`.
        """
        trial: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionSetTrial"
        ]
        """
        If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
        """

    class ListParamsScheduleDetailsAmendmentItemActionSetDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionSetDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsScheduleDetailsAmendmentItemActionSetDiscountDiscountEnd(
        TypedDict,
    ):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentItemActionSetDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsScheduleDetailsAmendmentItemActionSetDiscountDiscountEndDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsScheduleDetailsAmendmentItemActionSetTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class ListParamsScheduleDetailsAmendmentMetadataAction(TypedDict):
        add: NotRequired["Dict[str, str]"]
        """
        Key-value pairs to add to schedule phase metadata. These values will merge with existing schedule phase metadata.
        """
        remove: NotRequired["List[str]"]
        """
        Keys to remove from schedule phase metadata.
        """
        set: NotRequired["Literal['']|Dict[str, str]"]
        """
        Key-value pairs to set as schedule phase metadata. Existing schedule phase metadata will be overwritten.
        """
        type: Literal["add", "remove", "set"]
        """
        Select one of three ways to update phase-level `metadata` on subscription schedules.
        """

    class ListParamsScheduleDetailsAmendmentSetPauseCollection(TypedDict):
        set: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentSetPauseCollectionSet"
        ]
        """
        Details of the pause_collection behavior to apply to the amendment.
        """
        type: Literal["remove", "set"]
        """
        Determines the type of the pause_collection amendment.
        """

    class ListParamsScheduleDetailsAmendmentSetPauseCollectionSet(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class ListParamsScheduleDetailsAmendmentTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsAmendmentTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class ListParamsScheduleDetailsAmendmentTrialSettingsEndBehavior(
        TypedDict
    ):
        prorate_up_front: NotRequired["Literal['defer', 'include']"]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class ListParamsScheduleDetailsPhase(TypedDict):
        add_invoice_items: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseAddInvoiceItem]"
        ]
        """
        A list of prices and quantities that will generate invoice items appended to the next invoice for this phase. You may pass up to 20 items.
        """
        application_fee_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
        """
        automatic_tax: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseAutomaticTax"
        ]
        """
        Automatic tax settings for this phase.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['automatic', 'phase_start']"
        ]
        """
        Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
        """
        billing_thresholds: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
        """
        coupon: NotRequired["str"]
        """
        The identifier of the coupon to apply to this phase of the subscription schedule. This field has been deprecated and will be removed in a future API version. Use `discounts` instead.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        default_payment_method: NotRequired["str"]
        """
        ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will set the Subscription's [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates), which means they will be the Invoice's [`default_tax_rates`](https://stripe.com/docs/api/invoices/create#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.
        """
        description: NotRequired["Literal['']|str"]
        """
        Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseDiscount]"
        ]
        """
        The coupons to redeem into discounts for the schedule phase. If not specified, inherits the discount from the subscription's customer. Pass an empty string to avoid inheriting any discounts.
        """
        end_date: NotRequired["int|Literal['now']"]
        """
        The date at which this phase of the subscription schedule ends. If set, `iterations` must not be set.
        """
        invoice_settings: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseInvoiceSettings"
        ]
        """
        All invoices will be billed using the specified settings.
        """
        items: List[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItem"
        ]
        """
        List of configuration items, each with an attached price, to apply during this phase of the subscription schedule.
        """
        iterations: NotRequired["int"]
        """
        Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`. If set, `end_date` must not be set.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered, adding new keys and replacing existing keys in the subscription's `metadata`. Individual keys in the subscription's `metadata` can be unset by posting an empty value to them in the phase's `metadata`. To unset all keys in the subscription's `metadata`, update the subscription directly or unset every key individually from the phase's `metadata`.
        """
        on_behalf_of: NotRequired["str"]
        """
        The account on behalf of which to charge, for each of the associated subscription's invoices.
        """
        pause_collection: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhasePauseCollection"
        ]
        """
        If specified, payment collection for this subscription will be paused.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Whether the subscription schedule will create [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when transitioning to this phase. The default value is `create_prorations`. This setting controls prorations when a phase is started asynchronously and it is persisted as a field on the phase. It's different from the request-level [proration_behavior](https://stripe.com/docs/api/subscription_schedules/update#update_subscription_schedule-proration_behavior) parameter which controls what happens if the update request affects the billing configuration of the current phase.
        """
        start_date: NotRequired["int|Literal['now']"]
        """
        The date at which this phase of the subscription schedule starts or `now`. Must be set on the first phase.
        """
        transfer_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the associated subscription's invoices.
        """
        trial: NotRequired["bool"]
        """
        If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.
        """
        trial_continuation: NotRequired["Literal['continue', 'none']"]
        """
        Specify trial behavior when crossing phase boundaries
        """
        trial_end: NotRequired["int|Literal['now']"]
        """
        Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`
        """
        trial_settings: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseTrialSettings"
        ]
        """
        Settings related to subscription trials.
        """

    class ListParamsScheduleDetailsPhaseAddInvoiceItem(TypedDict):
        discounts: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseAddInvoiceItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the item.
        """
        price: NotRequired["str"]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseAddInvoiceItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item. Defaults to 1.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
        """

    class ListParamsScheduleDetailsPhaseAddInvoiceItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseAddInvoiceItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsScheduleDetailsPhaseAddInvoiceItemDiscountDiscountEnd(
        TypedDict,
    ):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseAddInvoiceItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsScheduleDetailsPhaseAddInvoiceItemDiscountDiscountEndDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsScheduleDetailsPhaseAddInvoiceItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsScheduleDetailsPhaseAutomaticTax(TypedDict):
        enabled: bool
        """
        Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
        """
        liability: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class ListParamsScheduleDetailsPhaseAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ListParamsScheduleDetailsPhaseBillingThresholds(TypedDict):
        amount_gte: NotRequired["int"]
        """
        Monetary threshold that triggers the subscription to advance to a new billing period
        """
        reset_billing_cycle_anchor: NotRequired["bool"]
        """
        Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
        """

    class ListParamsScheduleDetailsPhaseDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsScheduleDetailsPhaseDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsScheduleDetailsPhaseDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsScheduleDetailsPhaseInvoiceSettings(TypedDict):
        account_tax_ids: NotRequired["Literal['']|List[str]"]
        """
        The account tax IDs associated with this phase of the subscription schedule. Will be set on invoices generated by this phase of the subscription schedule.
        """
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
        """
        issuer: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseInvoiceSettingsIssuer"
        ]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class ListParamsScheduleDetailsPhaseInvoiceSettingsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ListParamsScheduleDetailsPhaseItem(TypedDict):
        billing_thresholds: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItemBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the subscription item.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a configuration item. Metadata on a configuration item will update the underlying subscription item's `metadata` when the phase is entered, adding new keys and replacing existing keys. Individual keys in the subscription item's `metadata` can be unset by posting an empty value to them in the configuration item's `metadata`. To unset all keys in the subscription item's `metadata`, update the subscription item directly or unset every key individually from the configuration item's `metadata`.
        """
        plan: NotRequired["str"]
        """
        The plan ID to subscribe to. You may specify the same ID in `plan` and `price`.
        """
        price: NotRequired["str"]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for the given price. Can be set only if the price's `usage_type` is `licensed` and not `metered`.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
        """
        trial: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItemTrial"
        ]
        """
        Options that configure the trial on the subscription item.
        """

    class ListParamsScheduleDetailsPhaseItemBillingThresholds(TypedDict):
        usage_gte: int
        """
        Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
        """

    class ListParamsScheduleDetailsPhaseItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsScheduleDetailsPhaseItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsScheduleDetailsPhaseItemDiscountDiscountEndDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsScheduleDetailsPhaseItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseItemPriceDataRecurring"
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsScheduleDetailsPhaseItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class ListParamsScheduleDetailsPhaseItemTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class ListParamsScheduleDetailsPhasePauseCollection(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class ListParamsScheduleDetailsPhaseTransferData(TypedDict):
        amount_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class ListParamsScheduleDetailsPhaseTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPhaseTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class ListParamsScheduleDetailsPhaseTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired["Literal['defer', 'include']"]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class ListParamsScheduleDetailsPrebilling(TypedDict):
        bill_until: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPrebillingBillUntil"
        ]
        """
        The end of the prebilled time period.
        """
        iterations: NotRequired["int"]
        """
        This is used to determine the number of billing cycles to prebill.
        """

    class ListParamsScheduleDetailsPrebillingBillUntil(TypedDict):
        amendment_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPrebillingBillUntilAmendmentEnd"
        ]
        """
        End the prebilled period when a specified amendment ends.
        """
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsScheduleDetailsPrebillingBillUntilDuration"
        ]
        """
        Time span for prebilling, starting from `bill_from`.
        """
        timestamp: NotRequired["int"]
        """
        End the prebilled period at a precise integer timestamp, starting from the Unix epoch.
        """
        type: Literal["amendment_end", "duration", "schedule_end", "timestamp"]
        """
        Select one of several ways to pass the `bill_until` value.
        """

    class ListParamsScheduleDetailsPrebillingBillUntilAmendmentEnd(TypedDict):
        index: int
        """
        The position of the amendment in the `amendments` array at which prebilling should end. Indexes start from 0 and must be less than the total number of supplied amendments.
        """

    class ListParamsScheduleDetailsPrebillingBillUntilDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsSubscriptionDetails(TypedDict):
        billing_cycle_anchor: NotRequired["Literal['now', 'unchanged']|int"]
        """
        For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. For existing subscriptions, the value can only be set to `now` or `unchanged`.
        """
        cancel_at: NotRequired["Literal['']|int"]
        """
        A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
        """
        cancel_at_period_end: NotRequired["bool"]
        """
        Boolean indicating whether this subscription should cancel at the end of the current period.
        """
        cancel_now: NotRequired["bool"]
        """
        This simulates the subscription being canceled or expired immediately.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        If provided, the invoice returned will preview updating or creating a subscription with these default tax rates. The default tax rates will apply to any line item that does not have `tax_rates` set.
        """
        items: NotRequired[
            "List[InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsItem]"
        ]
        """
        A list of up to 20 subscription items, each with an attached price.
        """
        prebilling: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsPrebilling"
        ]
        """
        The pre-billing to apply to the subscription as a preview.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
        """
        proration_date: NotRequired["int"]
        """
        If previewing an update to a subscription, and doing proration, `subscription_details.proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period and within the current phase of the schedule backing this subscription, if the schedule exists. If set, `subscription`, and one of `subscription_details.items`, or `subscription_details.trial_end` are required. Also, `subscription_details.proration_behavior` cannot be set to 'none'.
        """
        resume_at: NotRequired["Literal['now']"]
        """
        For paused subscriptions, setting `subscription_details.resume_at` to `now` will preview the invoice that will be generated if the subscription is resumed.
        """
        start_date: NotRequired["int"]
        """
        Date a subscription is intended to start (can be future or past).
        """
        trial_end: NotRequired["Literal['now']|int"]
        """
        If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_details.items` or `subscription` is required.
        """

    class ListParamsSubscriptionDetailsItem(TypedDict):
        billing_thresholds: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsItemBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
        """
        clear_usage: NotRequired["bool"]
        """
        Delete all usage for a given subscription item. Allowed only when `deleted` is set to `true` and the current plan's `usage_type` is `metered`.
        """
        deleted: NotRequired["bool"]
        """
        A flag that, if set to `true`, will delete the specified item.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the subscription item.
        """
        id: NotRequired["str"]
        """
        Subscription item to update.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        plan: NotRequired["str"]
        """
        Plan ID for this item, as a string.
        """
        price: NotRequired["str"]
        """
        The ID of the price object. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided.
        """
        price_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
        """

    class ListParamsSubscriptionDetailsItemBillingThresholds(TypedDict):
        usage_gte: int
        """
        Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
        """

    class ListParamsSubscriptionDetailsItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsSubscriptionDetailsItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsSubscriptionDetailsItemDiscountDiscountEndDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsSubscriptionDetailsItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: "InvoiceUpcomingLinesService.ListParamsSubscriptionDetailsItemPriceDataRecurring"
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsSubscriptionDetailsItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class ListParamsSubscriptionDetailsPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """

    class ListParamsSubscriptionItem(TypedDict):
        billing_thresholds: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsSubscriptionItemBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
        """
        clear_usage: NotRequired["bool"]
        """
        Delete all usage for a given subscription item. Allowed only when `deleted` is set to `true` and the current plan's `usage_type` is `metered`.
        """
        deleted: NotRequired["bool"]
        """
        A flag that, if set to `true`, will delete the specified item.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsSubscriptionItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the subscription item.
        """
        id: NotRequired["str"]
        """
        Subscription item to update.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        plan: NotRequired["str"]
        """
        Plan ID for this item, as a string.
        """
        price: NotRequired["str"]
        """
        The ID of the price object. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided.
        """
        price_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
        """

    class ListParamsSubscriptionItemBillingThresholds(TypedDict):
        usage_gte: int
        """
        Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
        """

    class ListParamsSubscriptionItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsSubscriptionItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ListParamsSubscriptionItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ListParamsSubscriptionItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: "InvoiceUpcomingLinesService.ListParamsSubscriptionItemPriceDataRecurring"
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsSubscriptionItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class ListParamsSubscriptionPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """

    def list(
        self,
        params: "InvoiceUpcomingLinesService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceLineItem]:
        """
        When retrieving an upcoming invoice, you'll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject[InvoiceLineItem],
            self._request(
                "get",
                "/v1/invoices/upcoming/lines",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "InvoiceUpcomingLinesService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceLineItem]:
        """
        When retrieving an upcoming invoice, you'll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject[InvoiceLineItem],
            await self._request_async(
                "get",
                "/v1/invoices/upcoming/lines",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
