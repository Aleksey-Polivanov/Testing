from Autofollow_Groups.get_autofollow_groups import \
    autofollow_no_location, \
    autofollow_US_Georgia_County_Muscogee, \
    autofollow_US_Georgia_County_Chatham, \
    autofollow_US_Kentucky_Fayette_County_Lexington

import unittest

class Tests(unittest.TestCase):
    def test_autofollow_US_Georgia_County_Muscogee(self):
        autofollow_US_Georgia_County_Muscogee(self)
    def test_autofollow_US_Georgia_County_Chatham(self):
        autofollow_US_Georgia_County_Chatham(self)
    def test_autofollow_US_Kentucky_Fayette_County_Lexington(self):
        autofollow_US_Kentucky_Fayette_County_Lexington(self)
    def test_autofollow_no_location(self):
        autofollow_no_location(self)


if __name__ == '__main__':
    unittest.main()

