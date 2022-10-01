#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import utila

import lists

DESCRIPTION = """\
Determine lists inside a document.

Supported:
    1.
    *
    -
    +
    •
"""

WORKPLAN = [
    utila.create_step(
        'result',
        inputs=[
            utila.ResultFile('rawmaker', 'oneline_text_text'),
            utila.ResultFile('rawmaker', 'oneline_text_positions'),
            utila.ResultFile('rawmaker', 'border_pages'),
            utila.ResultFile('headlines', 'result_result'),
            utila.ResultFile('footnote', 'result_result'),
        ],
        output=('result',),
    ),
    utila.create_step(
        'legacy',
        inputs=[
            utila.ResultFile('lists', 'result_result'),
        ],
        output=('legacy',),
    ),
]


def main():
    utila.featurepack(
        root=lists.ROOT,
        workplan=WORKPLAN,
        featurepackage='lists.features',
        config=utila.FeaturePackConfig(
            rename=rename,
            description=DESCRIPTION,
            name=lists.PROCESS,
            multiprocessed=True,
            pages=True,
            version=lists.__version__,
        ),
    )


def rename(path):
    if not isinstance(path, str):
        path = [rename(item) for item in path]
        return path
    path = utila.rreplace(
        path,
        pattern='lists__legacy_legacy',
        replace='words__list_list',
    )
    return path
