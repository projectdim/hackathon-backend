SELECT * FROM images
{% if data %}WHERE{% if 'review_ids' in data %} review_id IN {{data.review_ids}}{% endif %}{% endif %};