UPDATE reviews
SET timestamp = {{data.timestamp}}, intact = {{data.intact}}, stable_electricity = {{data.stable_electricity}}, accessible = {{data.accessible}}, stable_water = {{data.stable_water}}, gas_station = {{data.gas_station}}, medical_facilities = {{data.medical_facilities}}, comment = {{data.comment}}, status = {{data.status}}
WHERE id = {{data.id}}