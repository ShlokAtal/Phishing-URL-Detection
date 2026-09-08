from feature_extraction import extract_url_features

urls = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "http://192.168.1.100/login"
]

for url in urls:
    print("\n" + "=" * 60)
    print("URL:", url)
    print("=" * 60)
    features = extract_url_features(url)
    for key, value in features.items():
        print(f"{key}: {value}")