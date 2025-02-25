# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class PaymentAttemptRecord(ListableAPIResource["PaymentAttemptRecord"]):
    """
    A Payment Attempt Record represents an individual attempt at making a payment, on or off Stripe.
    Each payment attempt tries to collect a fixed amount of money from a fixed customer and payment
    method. Payment Attempt Records are attached to Payment Records. Only one attempt per Payment Record
    can have guaranteed funds.
    """

    OBJECT_NAME: ClassVar[Literal["payment_attempt_record"]] = (
        "payment_attempt_record"
    )

    class AmountCanceled(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class AmountFailed(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class AmountGuaranteed(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class AmountRequested(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class CustomerDetails(StripeObject):
        customer: Optional[str]
        """
        ID of the Stripe Customer associated with this payment.
        """
        email: Optional[str]
        """
        The customer's email address.
        """
        name: Optional[str]
        """
        The customer's name.
        """
        phone: Optional[str]
        """
        The customer's phone number.
        """

    class PaymentMethodDetails(StripeObject):
        class BillingDetails(StripeObject):
            class Address(StripeObject):
                city: Optional[str]
                """
                City, district, suburb, town, or village.
                """
                country: Optional[str]
                """
                Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                """
                line1: Optional[str]
                """
                Address line 1 (e.g., street, PO Box, or company name).
                """
                line2: Optional[str]
                """
                Address line 2 (e.g., apartment, suite, unit, or building).
                """
                postal_code: Optional[str]
                """
                ZIP or postal code.
                """
                state: Optional[str]
                """
                State, county, province, or region.
                """

            address: Address
            """
            A representation of a physical address.
            """
            email: Optional[str]
            """
            The billing email associated with the method of payment.
            """
            name: Optional[str]
            """
            The billing name associated with the method of payment.
            """
            phone: Optional[str]
            """
            The billing phone number associated with the method of payment.
            """
            _inner_class_types = {"address": Address}

        class Card(StripeObject):
            class Checks(StripeObject):
                address_line1_check: Optional[
                    Literal["fail", "pass", "unavailable", "unchecked"]
                ]
                address_postal_code_check: Optional[
                    Literal["fail", "pass", "unavailable", "unchecked"]
                ]
                cvc_check: Optional[
                    Literal["fail", "pass", "unavailable", "unchecked"]
                ]

            class NetworkToken(StripeObject):
                used: bool

            class ThreeDSecure(StripeObject):
                authentication_flow: Optional[
                    Literal["challenge", "frictionless"]
                ]
                result: Optional[
                    Literal[
                        "attempt_acknowledged",
                        "authenticated",
                        "exempted",
                        "failed",
                        "not_supported",
                        "processing_error",
                    ]
                ]
                result_reason: Optional[
                    Literal[
                        "abandoned",
                        "bypassed",
                        "canceled",
                        "card_not_enrolled",
                        "network_not_supported",
                        "protocol_error",
                        "rejected",
                    ]
                ]
                version: Optional[Literal["1.0.2", "2.1.0", "2.2.0"]]

            brand: Literal[
                "amex",
                "cartes_bancaires",
                "diners",
                "discover",
                "eftpos_au",
                "interac",
                "jcb",
                "link",
                "mastercard",
                "unionpay",
                "unknown",
                "visa",
            ]
            """
            Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
            """
            capture_before: Optional[int]
            """
            When using manual capture, a future timestamp at which the charge will be automatically refunded if uncaptured.
            """
            checks: Optional[Checks]
            """
            Check results by Card networks on Card address and CVC at time of payment.
            """
            country: Optional[str]
            """
            Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
            """
            exp_month: int
            """
            Two-digit number representing the card's expiration month.
            """
            exp_year: int
            """
            Four-digit number representing the card's expiration year.
            """
            fingerprint: Optional[str]
            """
            Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

            *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
            """
            funding: Literal["credit", "debit", "prepaid", "unknown"]
            """
            Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
            """
            last4: str
            """
            The last four digits of the card.
            """
            moto: Optional[bool]
            """
            True if this payment was marked as MOTO and out of scope for SCA.
            """
            network: Optional[
                Literal[
                    "amex",
                    "cartes_bancaires",
                    "diners",
                    "discover",
                    "eftpos_au",
                    "interac",
                    "jcb",
                    "link",
                    "mastercard",
                    "unionpay",
                    "unknown",
                    "visa",
                ]
            ]
            """
            Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
            """
            network_token: Optional[NetworkToken]
            """
            If this card has network token credentials, this contains the details of the network token credentials.
            """
            network_transaction_id: Optional[str]
            """
            This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.
            """
            three_d_secure: Optional[ThreeDSecure]
            """
            Populated if this transaction used 3D Secure authentication.
            """
            _inner_class_types = {
                "checks": Checks,
                "network_token": NetworkToken,
                "three_d_secure": ThreeDSecure,
            }

        class Custom(StripeObject):
            display_name: str
            """
            Display name for the custom (user-defined) payment method type used to make this payment.
            """
            type: Optional[str]
            """
            The custom payment method type associated with this payment.
            """

        billing_details: Optional[BillingDetails]
        """
        The billing details associated with the method of payment.
        """
        card: Optional[Card]
        """
        Details of the card used for this payment attempt.
        """
        custom: Optional[Custom]
        """
        Custom Payment Methods represent Payment Method types not modeled directly in
        the Stripe API. This resource consists of details about the custom payment method
        used for this payment attempt.
        """
        payment_method: Optional[str]
        """
        ID of the Stripe PaymentMethod used to make this payment.
        """
        type: Literal["card", "custom"]
        """
        The type of Payment Method used for this payment attempt.
        """
        _inner_class_types = {
            "billing_details": BillingDetails,
            "card": Card,
            "custom": Custom,
        }

    class ShippingDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Address
        """
        A representation of a physical address.
        """
        name: Optional[str]
        """
        The shipping recipient's name.
        """
        phone: Optional[str]
        """
        The shipping recipient's phone number.
        """
        _inner_class_types = {"address": Address}

    class ListParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_record: str
        """
        The ID of the Payment Record.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    amount_canceled: AmountCanceled
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    amount_failed: AmountFailed
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    amount_guaranteed: AmountGuaranteed
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    amount_requested: AmountRequested
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer_details: Optional[CustomerDetails]
    """
    Customer information for this payment.
    """
    customer_presence: Optional[Literal["off_session", "on_session"]]
    """
    Indicates whether the customer was present in your checkout flow during this payment.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["payment_attempt_record"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_method_details: Optional[PaymentMethodDetails]
    """
    Information about the Payment Method debited for this payment.
    """
    payment_record: Optional[str]
    """
    ID of the Payment Record this Payment Attempt Record belongs to.
    """
    payment_reference: Optional[str]
    """
    An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.
    """
    shipping_details: Optional[ShippingDetails]
    """
    Shipping information for this payment.
    """

    @classmethod
    def list(
        cls, **params: Unpack["PaymentAttemptRecord.ListParams"]
    ) -> ListObject["PaymentAttemptRecord"]:
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["PaymentAttemptRecord.ListParams"]
    ) -> ListObject["PaymentAttemptRecord"]:
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentAttemptRecord.RetrieveParams"]
    ) -> "PaymentAttemptRecord":
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PaymentAttemptRecord.RetrieveParams"]
    ) -> "PaymentAttemptRecord":
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "amount_canceled": AmountCanceled,
        "amount_failed": AmountFailed,
        "amount_guaranteed": AmountGuaranteed,
        "amount_requested": AmountRequested,
        "customer_details": CustomerDetails,
        "payment_method_details": PaymentMethodDetails,
        "shipping_details": ShippingDetails,
    }
