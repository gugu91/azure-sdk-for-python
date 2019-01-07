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


class UploadCertificateRequest(Model):
    """The Upload certificate request.

    All required parameters must be populated in order to send to Azure.

    :param authentication_type: The authentication type. Possible values
     include: 'Invalid', 'AzureActiveDirectory'
    :type authentication_type: str or
     ~azure.mgmt.edgegateway.models.AuthenticationType
    :param certificate: Required. The base64 encoded certificate raw data.
    :type certificate: str
    """

    _validation = {
        'certificate': {'required': True},
    }

    _attribute_map = {
        'authentication_type': {'key': 'properties.authenticationType', 'type': 'str'},
        'certificate': {'key': 'properties.certificate', 'type': 'str'},
    }

    def __init__(self, *, certificate: str, authentication_type=None, **kwargs) -> None:
        super(UploadCertificateRequest, self).__init__(**kwargs)
        self.authentication_type = authentication_type
        self.certificate = certificate
