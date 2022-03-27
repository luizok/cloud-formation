def handler(event, context):
    print('Child:', event)

    event['childData'] = 'Im being called by my father'

    print(event)

    return {
        'httpStatus': 200,
        'body': {'some': 'data'}
    }
