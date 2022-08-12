import datetime as dt

from src.storage import write_file


def handler(event, context):

    timestamp = dt.datetime.now().timestamp()
    filename = f'file_{timestamp}.txt'

    was_uploaded = write_file(filename)
    print('Child:', event)

    return {
        'httpStatus': 200 if was_uploaded else 400,
        'body': {'some': 'data'}
    }
