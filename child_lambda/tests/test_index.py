import unittest

import mock

from index import handler


class HandlerTestCase(unittest.TestCase):

    @mock.patch('index.write_file')
    def test_write_file_success(self, sswf):

        sswf.return_value = True

        ret_val = handler(None, None)

        self.assertEqual(ret_val, {
            'httpStatus': 200,
            'body': {'some': 'data'}}
        )

    @mock.patch('index.write_file')
    def test_write_file_fail(self, sswf):

        sswf.return_value = False

        ret_val = handler(None, None)

        self.assertEqual(ret_val, {
            'httpStatus': 400,
            'body': {'some': 'data'}}
        )
