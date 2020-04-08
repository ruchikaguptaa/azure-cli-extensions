# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_operationsmanagement(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.operationsmanagement import OperationsManagementClient
    return get_mgmt_service_client(cli_ctx, OperationsManagementClient)


def cf_solution(cli_ctx, *_):
    return cf_operationsmanagement(cli_ctx).solution


def cf_management_association(cli_ctx, *_):
    return cf_operationsmanagement(cli_ctx).management_association


def cf_management_configuration(cli_ctx, *_):
    return cf_operationsmanagement(cli_ctx).management_configuration