#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _l
from cmk.gui.type_defs import PainterSpec, VisualLinkSpec
from cmk.gui.views.store import multisite_builtin_views

multisite_builtin_views.update(
    {
        "topology_filters": {
            "browser_reload": 30,
            "column_headers": "pergroup",
            "datasource": "hosts",
            "description": _l(
                "Configures the number of available filters in the network topology view."
            ),
            "group_painters": [],
            "hidden": True,
            "hidebutton": True,
            "layout": "table",
            "mustsearch": False,
            "name": "topology_filters",
            "num_columns": 3,
            "owner": "",
            "painters": [PainterSpec(name="host_state")],
            "play_sounds": False,
            "public": True,
            "sorters": [],
            "title": _l("Topology filters"),
            "topic": "Topology",
            "user_sortable": True,
            "single_infos": [],
            "context": {
                "topology_max_nodes": {},
                "topology_mesh_depth": {},
                "hoststate": {},
                "hostalias": {},
                "siteopt": {},
                "hostregex": {},
                "hostgroups": {},
                "host_labels": {},
                "opthost_contactgroup": {},
                "host_tags": {},
            },
            "link_from": {},
            "icon": None,
            "add_context_to_title": True,
            "sort_index": 99,
            "is_show_more": False,
        },
        "bi_map_hover_host": {
            "browser_reload": 0,
            "column_headers": "pergroup",
            "datasource": "hosts",
            "description": _l("Host hover menu shown in BI visualization"),
            "hidden": True,
            "hidebutton": True,
            "group_painters": [],
            "icon": None,
            "layout": "dataset",
            "mobile": False,
            "mustsearch": False,
            "name": "bi_map_hover_host",
            "num_columns": 1,
            "owner": "",
            "painters": [
                PainterSpec(
                    name="host",
                    parameters={"color_choices": []},
                    link_spec=VisualLinkSpec(type_name="views", name="hoststatus"),
                ),
                PainterSpec(name="host_state"),
                PainterSpec(name="host_plugin_output"),
            ],
            "play_sounds": False,
            "public": True,
            "single_infos": ["host"],
            "sorters": [],
            "title": _l("BI host details"),
            "user_sortable": True,
            "context": {},
            "link_from": {},
            "topic": "",
            "add_context_to_title": True,
            "sort_index": 99,
            "is_show_more": False,
        },
        "bi_map_hover_service": {
            "browser_reload": 0,
            "column_headers": "pergroup",
            "datasource": "services",
            "description": _l("Service hover menu shown in BI visualization"),
            "hidden": True,
            "hidebutton": True,
            "group_painters": [],
            "icon": None,
            "layout": "dataset",
            "mobile": False,
            "mustsearch": False,
            "name": "bi_map_hover_service",
            "num_columns": 1,
            "painters": [
                PainterSpec(
                    name="host",
                    parameters={"color_choices": []},
                    link_spec=VisualLinkSpec(type_name="views", name="hoststatus"),
                ),
                PainterSpec(
                    name="service_description",
                    link_spec=VisualLinkSpec(type_name="views", name="service"),
                ),
                PainterSpec(name="service_state"),
                PainterSpec(name="host_check_age"),
                PainterSpec(name="svc_acknowledged"),
                PainterSpec(name="svc_in_downtime"),
            ],
            "play_sounds": False,
            "public": True,
            "single_infos": ["service", "host"],
            "sorters": [],
            "title": _l("BI service details"),
            "owner": "",
            "user_sortable": True,
            "context": {},
            "link_from": {},
            "topic": "",
            "add_context_to_title": True,
            "sort_index": 99,
            "is_show_more": False,
        },
        "topology_hover_host": {
            "browser_reload": 0,
            "column_headers": "pergroup",
            "datasource": "hosts",
            "description": _l("Host hover menu shown in topolgoy visualization"),
            "hidden": True,
            "hidebutton": True,
            "group_painters": [],
            "icon": None,
            "layout": "dataset",
            "mobile": False,
            "mustsearch": False,
            "name": "topology_hover_host",
            "num_columns": 1,
            "owner": "",
            "painters": [
                PainterSpec(
                    name="host",
                    parameters={"color_choices": []},
                    link_spec=VisualLinkSpec(type_name="views", name="hoststatus"),
                ),
                PainterSpec(name="host_state"),
                PainterSpec(name="host_plugin_output"),
                PainterSpec(name="host_parents"),
                PainterSpec(name="host_childs"),
            ],
            "play_sounds": False,
            "public": True,
            "single_infos": ["host"],
            "sorters": [],
            "title": _l("Toplogy host details"),
            "user_sortable": True,
            "context": {},
            "link_from": {},
            "topic": "",
            "add_context_to_title": True,
            "sort_index": 99,
            "is_show_more": False,
        },
    }
)
