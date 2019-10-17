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
import ast
import json
import sys


def main(*argv):
    input_str = "\n".join(sys.stdin)
    as_py_data_type = ast.literal_eval(input_str)
    print(json.dumps(as_py_data_type))
