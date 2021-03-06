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


class ConnectedClusterPatch(Model):
    """Object containing updates for patch operations.

    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param agent_public_key_certificate: Base64 encoded public certificate
     used by the agent to do the initial handshake to the backend services in
     Azure.
    :type agent_public_key_certificate: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'agent_public_key_certificate': {'key': 'properties.agentPublicKeyCertificate', 'type': 'str'},
    }

    def __init__(self, *, tags=None, agent_public_key_certificate: str=None, **kwargs) -> None:
        super(ConnectedClusterPatch, self).__init__(**kwargs)
        self.tags = tags
        self.agent_public_key_certificate = agent_public_key_certificate
