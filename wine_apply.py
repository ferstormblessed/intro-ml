import pandas as pd


def remean_points(row):
    row.points = row.points - review_points_mean
    return row


wine_reviews = pd.read_json("winemag-data-130k-v2.json")
review_points_mean = wine_reviews.points.mean()

wine_map = wine_reviews.apply(remean_points, axis='columns')
print(wine_map)
