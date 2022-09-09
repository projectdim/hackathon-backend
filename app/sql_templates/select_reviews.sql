SELECT * FROM reviews
{% if ('latitude_1' in data and 'latitude_2' in data) or ('longitude_1' in data and 'longitude_2' in data) or 'statuses' in data %}WHERE {% if 'latitude_1' in data and 'latitude_2' in data %}(latitude BETWEEN {{data.latitude_1}} AND {{data.latitude_2}}) AND {% endif %}{% if 'longitude_1' in data and 'longitude_2' in data %}(longitude BETWEEN {{data.longitude_1}} AND {{data.longitude_2}}) AND {% endif %}{% if 'statuses' in data %}status IN {{data.statuses}} AND {% endif %}1{% endif %}
ORDER BY timestamp DESC;
