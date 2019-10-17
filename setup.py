#
# OMNIVORE CONFIDENTIAL
# __________________
#
#  [2013] - [2019] Omnivore Technologies
#  All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of Omnivore Technologies and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Omnivore Technologies
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Omnivore Technologies.
#
import sys

import os
from setuptools import setup

sys.path.insert(0, os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "src"
))

setup(
    name="py-to-json",
    version="1.0",
    description="Script to convert a string representation of standard python data types to json.",
    url="https://github.com/jlevitt/py-to-json",
    author="Jake Levitt",
    license="MIT",
    package_dir={"": "src"},
    packages=["py_to_json"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "py-to-json = py_to_json.cli:main",
        ],
    },
)