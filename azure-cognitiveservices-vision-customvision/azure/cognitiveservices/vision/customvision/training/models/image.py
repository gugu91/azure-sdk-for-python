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


class Image(Model):
    """Image model to be sent as JSON.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Required. Id of the image.
    :vartype id: str
    :ivar created: Required. Date the image was created.
    :vartype created: datetime
    :ivar width: Required. Width of the image.
    :vartype width: int
    :ivar height: Required. Height of the image.
    :vartype height: int
    :ivar resized_image_uri: Required. The URI to the (resized) image used for
     training.
    :vartype resized_image_uri: str
    :ivar thumbnail_uri: Required. The URI to the thumbnail of the original
     image.
    :vartype thumbnail_uri: str
    :ivar original_image_uri: Required. The URI to the original uploaded
     image.
    :vartype original_image_uri: str
    :ivar tags: Tags associated with this image.
    :vartype tags:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageTag]
    :ivar regions: Regions associated with this image.
    :vartype regions:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageRegion]
    """

    _validation = {
        'id': {'required': True, 'readonly': True},
        'created': {'required': True, 'readonly': True},
        'width': {'required': True, 'readonly': True},
        'height': {'required': True, 'readonly': True},
        'resized_image_uri': {'required': True, 'readonly': True},
        'thumbnail_uri': {'required': True, 'readonly': True},
        'original_image_uri': {'required': True, 'readonly': True},
        'tags': {'readonly': True},
        'regions': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
        'resized_image_uri': {'key': 'resizedImageUri', 'type': 'str'},
        'thumbnail_uri': {'key': 'thumbnailUri', 'type': 'str'},
        'original_image_uri': {'key': 'originalImageUri', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[ImageTag]'},
        'regions': {'key': 'regions', 'type': '[ImageRegion]'},
    }

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)
        self.id = None
        self.created = None
        self.width = None
        self.height = None
        self.resized_image_uri = None
        self.thumbnail_uri = None
        self.original_image_uri = None
        self.tags = None
        self.regions = None
