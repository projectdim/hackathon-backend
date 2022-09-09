SELECT * FROM dim_db.events
{% if data %}WHERE {% if 'marker_ids' in data %}marker_id IN {{data.marker_ids}} AND {% endif %}{% if 'statuses' in data %}status IN {{data.statuses}} AND {% endif %}1{% endif %}
ORDER BY marker_id, timestamp DESC;