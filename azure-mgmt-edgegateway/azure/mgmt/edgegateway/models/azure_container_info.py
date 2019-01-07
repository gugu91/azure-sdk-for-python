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


class AzureContainerInfo(Model):
    """Azure container mapping of the endpoint.

    All required parameters must be populated in order to send to Azure.

    :param storage_account_credential_id: Required. ID of the Storage account
     credential to be used for accessing storage.
    :type storage_account_credential_id: str
    :param container_name: Required. Container name (Based on the data format
     specified, represents the name of Azure file/ Page blob / Block blob).
    :type container_name: str
    :param data_format: Required. Storage format used for the file represented
     by the share. Possible values include: 'BlockBlob', 'PageBlob',
     'AzureFile'
    :type data_format: str or
     ~azure.mgmt.edgegateway.models.AzureContainerDataFormat
    """

    _validation = {
        'storage_account_credential_id': {'required': True},
        'container_name': {'required': True},
        'data_format': {'required': True},
    }

    _attribute_map = {
        'storage_account_credential_id': {'key': 'storageAccountCredentialId', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'data_format': {'key': 'dataFormat', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureContainerInfo, self).__init__(**kwargs)
        self.storage_account_credential_id = kwargs.get('storage_account_credential_id', None)
        self.container_name = kwargs.get('container_name', None)
        self.data_format = kwargs.get('data_format', None)
