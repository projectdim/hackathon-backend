from .base_entity import BaseEntity
from images_entity import ImageEntity


class ReviewEntity(BaseEntity):
    table_name = 'reviews'

    fields = [
        'id',
        'latitude',
        'longitude',
        'ts',
        'intact',
        'stable_electricity',
        'accessible',
        'stable_water',
        'gas_station',
        'medical_facilities',
        'comment',
        'status',
    ]

    def createReview(self, payload, images):
        map(
            lambda image: ImageEntity.createImage(image['review_id'], image['image_ref']),
            images
        )

        return self.create(payload)
