#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# {
#     'port': 8080,
#     'password': 'marchingband',
#     'sections': ['instance', 'jobs', 'nodes', 'queue'],
#     'user': 'kitty'
# }


from collections.abc import Mapping, Sequence
from typing import Any

from cmk.base.check_api import passwordstore_get_cmdline
from cmk.base.config import special_agent_info


def agent_jenkins_arguments(
    params: Mapping[str, Any], hostname: str, ipaddress: str | None
) -> Sequence[str | tuple[str, str, str]]:
    args = [
        "-P",
        params["protocol"],
        "-u",
        params["user"],
        "-s",
        passwordstore_get_cmdline("%s", params["password"]),
    ]

    if "sections" in params:
        args += ["-m", " ".join(params["sections"])]

    if "port" in params:
        args += ["-p", params["port"]]

    args.append(params["instance"])

    return args


special_agent_info["jenkins"] = agent_jenkins_arguments
