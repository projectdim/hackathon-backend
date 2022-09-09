def transform_contact(record):
    return {
        'label': record['label'],
        'telephoneNumber': record['phone'],
        'email': record['email']
    }


def transform_photo(record):
    return {
        'url': record['image_ref']
    }


def transform_address(record):
    return {
        'city': record['city'],
        'zipcode': record['zipcode'],
        'street': record['street']
    }


def transform_pin(record):
    return {
        'id': record['id'],
        'lat': record['latitude'],
        'lng': record['longitude']
    }


def transform_status(record, status_type):
    return {
        'type': 'status_type'.replace('_', ' '),
        'statusKey': record[f'{status_type}_status'],
        'safetyLevel': record[f'{status_type}_safety_level'],
        'modifiedDate': '',
        'description': record[f'{status_type}_description']
    }


def transform_marker(record, photo_records):
    return {
        'id': record['id'],
        'address': transform_address(record),
        'photos': [transform_photo(ph)for ph in photo_records],
        'statuses': [transform_status(record, status_type)
                     for status_type in ['building', 'electricity', 'water', 'road', 'fuel', 'medical_facilities']]
    }


def transform_data(records):
    return {
        'markers': [transform_pin(record) for record in records]
    }
