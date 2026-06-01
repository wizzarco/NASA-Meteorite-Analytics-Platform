class NeoParser:
    def parse(self, data):
        records = []
        neo_objects = data["near_earth_objects"]
        for date_key, asteroids in neo_objects.items():
            for asteroid in asteroids:
                approach = asteroid["close_approach_data"][0]
                # Change the name to friendly 
                records.append({
                    "asteroid_id": asteroid["id"],
                    "asteroid_name": asteroid["name"],
                    "absolute_magnitude": asteroid["absolute_magnitude_h"],
                    "diameter_min_m":
                        asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"],
                    "diameter_max_m":
                        asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"],
                    "hazardous_flag":
                        asteroid["is_potentially_hazardous_asteroid"],
                    "sentry_flag":
                        asteroid["is_sentry_object"],
                    "approach_date":
                        approach["close_approach_date"],
                    "velocity_kmh":
                        float(
                            approach["relative_velocity"]["kilometers_per_hour"]
                        ),
                    "miss_distance_km":
                        float(
                            approach["miss_distance"]["kilometers"]
                        ),
                    "orbiting_body":
                        approach["orbiting_body"]
                })

        return records