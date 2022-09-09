SELECT * FROM events
{% if data %}WHERE {% if 'review_ids' in data %}review_id IN {{data.review_ids}} AND {% endif %}{% if 'statuses' in data %}status IN {{data.statuses}} AND {% endif %}1{% endif %}
ORDER BY review_id, timestamp DESC;