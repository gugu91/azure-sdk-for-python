# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TransferBillingSubscriptionResult(Model):
    """Request parameters to transfer billing subscription.

    :param billing_subscription_id: The destination billing subscription id.
    :type billing_subscription_id: str
    """

    _attribute_map = {
        'billing_subscription_id': {'key': 'properties.billingSubscriptionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TransferBillingSubscriptionResult, self).__init__(**kwargs)
        self.billing_subscription_id = kwargs.get('billing_subscription_id', None)
