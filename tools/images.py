def get_images(city: str):
    city = city.strip().title()

    images = {
        "Paris": [
            "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
            "https://images.unsplash.com/photo-1522098543979-ffc7f79a56b4",
            "https://images.unsplash.com/photo-1499856871958-5b9627545d1a",
        ],
        "Tokyo": [
            "https://images.unsplash.com/photo-1549693578-d683be217e58",
            "https://images.unsplash.com/photo-1505060893674-1a5a8a0e2d02",
            "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf",
        ],
        "New York": [
            "https://images.unsplash.com/photo-1549924231-f129b911e442",
            "https://images.unsplash.com/photo-1534447677768-be436bb09401",
            "https://images.unsplash.com/photo-1546436836-07a91091f160",
        ],
    }

    return images.get(
        city,
        [
            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
            "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1",
            "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        ],
    )
