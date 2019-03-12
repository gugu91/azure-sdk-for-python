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


class ImageRegionProposal(Model):
    """ImageRegionProposal.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar project_id: Required.
    :vartype project_id: str
    :ivar image_id: Required.
    :vartype image_id: str
    :ivar proposals: Required.
    :vartype proposals:
     list[~azure.cognitiveservices.vision.customvision.training.models.RegionProposal]
    """

    _validation = {
        'project_id': {'required': True, 'readonly': True},
        'image_id': {'required': True, 'readonly': True},
        'proposals': {'required': True, 'readonly': True},
    }

    _attribute_map = {
        'project_id': {'key': 'projectId', 'type': 'str'},
        'image_id': {'key': 'imageId', 'type': 'str'},
        'proposals': {'key': 'proposals', 'type': '[RegionProposal]'},
    }

    def __init__(self, **kwargs):
        super(ImageRegionProposal, self).__init__(**kwargs)
        self.project_id = None
        self.image_id = None
        self.proposals = None
