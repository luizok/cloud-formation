import unittest

import mock

from src.storage import write_file


class StorageTestCase(unittest.TestCase):

    @mock.patch('boto3.resource')
    def test_write_file_success(self, br):

        br.return_value = s3_client = mock.Mock()
        s3_client.Bucket.return_value = bucket = mock.Mock()

        filename = 'test.txt'
        ret_val = write_file(filename)

        bucket.upload_file.assert_called_with('/tmp/test.txt', filename)
        self.assertTrue(ret_val)

    @mock.patch('boto3.resource')
    def test_write_file_not_ends_with_txt(self, br):

        br.return_value = s3_client = mock.Mock()
        s3_client.Bucket.return_value = mock.Mock()

        filename = 'test.not'
        ret_val = write_file(filename)

        self.assertFalse(ret_val)
