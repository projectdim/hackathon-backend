from .base_entity import BaseEntity


class EventEntity(BaseEntity):
    table_name = 'events'

    fields = [
        'ts',
        'review_id',
        'intact',
        'stable_electricity',
        'accessible',
        'stable_water',
        'gas_station',
        'medical_facilities',
        'comment',
        'status',
        'type',
    ]
