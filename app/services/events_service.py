from ..entities.event_entity import EventEntity


class EventsService:
    def create_event(self):
        return EventEntity().create({
            'ts': "'2022-01-01 00:00:00'",
            'review_id': 1,
            'intact': 1,
            'stable_electricity': 1,
            'accessible': 1,
            'stable_water': 1,
            'gas_station': 1,
            'medical_facilities': 1,
            'comment': 1,
            'status': 1,
            'type': 1,
        })
