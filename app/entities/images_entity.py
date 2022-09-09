from .base_entity import BaseEntity


class ImageEntity(BaseEntity):
    table_name = 'images'

    fields = [
        'review_id'
        'image_ref'
    ]

    def createImage(self, review_id: int, image_ref: str):
        return self.create(
            {
                'review_id': review_id,
                'image_ref': image_ref
            }
        )
