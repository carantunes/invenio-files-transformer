# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# Invenio-Files-Transformer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for transforming and/or processing files."""

from __future__ import absolute_import, print_function

from .ext import InvenioFilesTransformer
from .version import __version__

__all__ = ('__version__', 'InvenioFilesTransformer')
