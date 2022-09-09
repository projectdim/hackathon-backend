SELECT * FROM dim_db.images
{% if data %}WHERE{% if 'marker_ids' in data %} marker_id IN {{data.marker_ids}}{% endif %}{% endif %};