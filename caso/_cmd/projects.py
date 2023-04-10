# -*- coding: utf-8 -*-

# Copyright 2014 Spanish National Research Council (CSIC)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys

from oslo_config import cfg
from oslo_log import log

import caso.config
import caso.manager

CONF = cfg.CONF


def main():
    """Get cASO configured projects."""
    caso.config.parse_args(sys.argv)
    log.setup(cfg.CONF, "caso")
    manager = caso.manager.Manager()
    for prj, vo in manager.projects_and_vos():
        print(f"'{prj} mapped to VO '{vo}'")


if __name__ == "__main__":
    main()
