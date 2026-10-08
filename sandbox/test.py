gtfs_time = "25:10:00"
hours, minutes, seconds = map(int, gtfs_time.split(":"))
total_seconds = hours * 3600 + minutes * 60 + seconds
print(total_seconds)