# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
from collections import Counter
from collections import OrderedDict as od
from pathlib import Path
from typing import Dict, List, Union

import numpy as np
def read_manifest(manifest: Union[Path, str]) -> List[dict]:
    with open(manifest, "r", encoding="utf-8") as f:
        try:
            manifest = json.load(f)
            return manifest
        except json.JSONDecodeError:
            pass
    with open(manifest, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def write_manifest(output_path: Union[Path, str], target_manifest: List[dict], ensure_ascii: bool = True):
    """
    Write to manifest file

    Args:
        output_path (str or Path): Path to output manifest file
        target_manifest (list): List of manifest file entries
        ensure_ascii (bool): default is True, meaning the output is guaranteed to have all incoming
                             non-ASCII characters escaped. If ensure_ascii is false, these characters
                             will be output as-is.
    """
    with open(output_path, "w", encoding="utf-8") as outfile:
        for tgt in target_manifest:
            json.dump(tgt, outfile, ensure_ascii=ensure_ascii)
            outfile.write('\n')

