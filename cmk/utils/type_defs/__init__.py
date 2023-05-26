#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Checkmk wide type definitions"""

__all__ = [
    "ValidatedString",
    "ActiveCheckPluginName",
    "AgentRawData",
    "AgentTargetVersion",
    "BuiltInPluginNames",
    "BulkOutsideTimePeriodType",
    "CheckPluginNameStr",
    "ClusterMode",
    "ConditionEventConsoleAlertsType",
    "Contact",
    "ContactgroupName",
    "ContactName",
    "CustomPluginName",
    "Deserializer",
    "DisabledNotificationsOptions",
    "DiscoveryResult",
    "ECEventContext",
    "EmailBodyElementsType",
    "EvalableFloat",
    "EventConsoleOption",
    "EventContext",
    "EventRule",
    "EVERYTHING",
    "ExitSpec",
    "ensure_mrpe_configs",
    "FromOrToType",
    "Gateways",
    "GroupbyType",
    "HandlerName",
    "HandlerParameters",
    "HostAddress",
    "HostAgentConnectionMode",
    "HostEventType",
    "HostgroupName",
    "HostName",
    "HostOrServiceConditionRegex",
    "HostOrServiceConditions",
    "HostOrServiceConditionsNegated",
    "HostOrServiceConditionsSimple",
    "HostState",
    "HostsToUpdate",
    "HostTagAgentOrSpecialAgentType",
    "HostTagAgentType",
    "HostTagCheckMkAgentType",
    "HostTagCriticalType",
    "HostTagIpAddressFamilyType",
    "HostTagIpV4Type",
    "HostTagIpV6Type",
    "HostTagMonitorSNMPType",
    "HostTagNetworkType",
    "HostTagPiggyBackType",
    "HostTagPingType",
    "HostTagSNMPType",
    "HostTagTypes",
    "HTTPMethod",
    "InfluxDBConnectionSpec",
    "Item",
    "JsonSerializable",
    "IlertAPIKey",
    "LegacyCheckParameters",
    "MrpeConfig",
    "MrpeConfigDeprecated",
    "MatchRegex",
    "MetricName",
    "MetricTuple",
    "MgmntPriorityType",
    "MgmntUrgencyType",
    "NotificationContext",
    "NotificationRuleID",
    "NotificationType",
    "NotifyAnalysisInfo",
    "NotifyBulk",
    "NotifyBulkParameters",
    "NotifyBulks",
    "NotifyBulkType",
    "NotifyPluginInfo",
    "NotifyPluginName",
    "NotificationPluginNameStr",
    "NotifyPluginParams",
    "NotifyPluginParamsDict",
    "NotifyPluginParamsList",
    "NotifyRuleInfo",
    "OpsGeniePriorityPValueType",
    "OpsGeniePriorityStrType",
    "PluginOption",
    "ProxyUrl",
    "PushOverPriorityNumType",
    "PushOverPriorityStringType",
    "RegexModes",
    "RoutingKeyType",
    "ParametersTypeAlias",
    "ParsedSectionName",
    "PasswordType",
    "PhaseOneResult",
    "PluginNotificationContext",
    "RuleSetName",
    "Seconds",
    "SectionName",
    "Serializer",
    "ServiceAdditionalDetails",
    "ServiceDetails",
    "ServiceEventType",
    "ServicegroupName",
    "ServiceName",
    "ServiceState",
    "SNMPDetectBaseType",
    "state_markers",
    "ServiceLevels",
    "ServiceLevelsStr",
    "ServiceLevelsType",
    "SortOrder",
    "SoundType",
    "SysLogFacilityIntType",
    "SysLogFacilityStrType",
    "SyslogPriorityIntType",
    "SysLogPriorityStrType",
    "TimeperiodName",
    "TimeperiodSpec",
    "timeperiod_spec_alias",
    "TimeperiodSpecs",
    "TimeRange",
    "Timestamp",
    "UpdateDNSCacheResult",
    "UserId",
    "URLPrefix",
    "UUIDs",
    "WebHookUrl",
]


from ._misc import (  # TODO(ML): We should clean this up some day.
    ActiveCheckPluginName,
    AgentRawData,
    AgentTargetVersion,
    CheckPluginNameStr,
    ClusterMode,
    ContactgroupName,
    DiscoveryResult,
    EvalableFloat,
    EVERYTHING,
    ExitSpec,
    HostOrServiceConditionRegex,
    HostOrServiceConditions,
    HostOrServiceConditionsNegated,
    HostOrServiceConditionsSimple,
    HTTPMethod,
    InfluxDBConnectionSpec,
    Item,
    JsonSerializable,
    LegacyCheckParameters,
    MetricName,
    MetricTuple,
    ParametersTypeAlias,
    Seconds,
    ServiceAdditionalDetails,
    ServiceDetails,
    ServicegroupName,
    ServiceName,
    ServiceState,
    SNMPDetectBaseType,
    state_markers,
    timeperiod_spec_alias,
    TimeperiodName,
    TimeperiodSpec,
    TimeperiodSpecs,
    TimeRange,
    Timestamp,
)
from .automations import PhaseOneResult
from .core_config import HostsToUpdate
from .host import HostAddress, HostAgentConnectionMode, HostgroupName, HostName, HostState
from .ip_lookup import UpdateDNSCacheResult
from .mrpe_config import ensure_mrpe_configs, MrpeConfig, MrpeConfigDeprecated
from .notify import (
    BuiltInPluginNames,
    BulkOutsideTimePeriodType,
    ConditionEventConsoleAlertsType,
    Contact,
    ContactName,
    CustomPluginName,
    DisabledNotificationsOptions,
    ECEventContext,
    EmailBodyElementsType,
    EventConsoleOption,
    EventContext,
    EventRule,
    FromOrToType,
    GroupbyType,
    HandlerName,
    HandlerParameters,
    HostEventType,
    HostTagAgentOrSpecialAgentType,
    HostTagAgentType,
    HostTagCheckMkAgentType,
    HostTagCriticalType,
    HostTagIpAddressFamilyType,
    HostTagIpV4Type,
    HostTagIpV6Type,
    HostTagMonitorSNMPType,
    HostTagNetworkType,
    HostTagPiggyBackType,
    HostTagPingType,
    HostTagSNMPType,
    HostTagTypes,
    IlertAPIKey,
    MatchRegex,
    MgmntPriorityType,
    MgmntUrgencyType,
    NotificationContext,
    NotificationPluginNameStr,
    NotificationRuleID,
    NotificationType,
    NotifyAnalysisInfo,
    NotifyBulk,
    NotifyBulkParameters,
    NotifyBulks,
    NotifyBulkType,
    NotifyPluginInfo,
    NotifyPluginName,
    NotifyPluginParams,
    NotifyPluginParamsDict,
    NotifyPluginParamsList,
    NotifyRuleInfo,
    OpsGeniePriorityPValueType,
    OpsGeniePriorityStrType,
    PasswordType,
    PluginNotificationContext,
    PluginOption,
    ProxyUrl,
    PushOverPriorityNumType,
    PushOverPriorityStringType,
    RegexModes,
    RoutingKeyType,
    ServiceEventType,
    ServiceLevels,
    ServiceLevelsStr,
    ServiceLevelsType,
    SortOrder,
    SoundType,
    SysLogFacilityIntType,
    SysLogFacilityStrType,
    SyslogPriorityIntType,
    SysLogPriorityStrType,
    URLPrefix,
    UUIDs,
    WebHookUrl,
)
from .parent_scan import Gateways
from .pluginname import ParsedSectionName, RuleSetName, SectionName, ValidatedString
from .protocol import Deserializer, Serializer
from .user_id import UserId
