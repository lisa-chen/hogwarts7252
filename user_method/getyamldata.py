# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:陈林莎
# datetime:2021/6/20 10:38
# software: PyCharm

import yaml
import os
from user_method.base_path import TEST_DATA


def openyaml(filename):
    file_path = os.path.join(TEST_DATA, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)



print(openyaml("add"))
