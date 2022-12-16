#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import glob
import os

test_pattern = 'test_*.py'

if __name__ == '__main__':

    # Find all files matching pattern
    module_files = sorted(glob.glob(test_pattern))
    module_names = [os.path.splitext(os.path.basename(module_file))[0] for module_file in module_files]

    # Iterate over the found files
    print('Importing:')
    for module in module_names:
        print('    ', module)
        exec('import %s' % module)

    print('Done!')
    print()

    unittest.main(defaultTest=module_names)
