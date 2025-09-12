import urllib.parse

def update_index_features(full_index_md: str, new_title: str, new_details: str, new_link: str) -> str:    
    features = full_index_md.split('features:')[-1].split('---')[0].strip()    

    feature_list = [f for f in features.split('- ') if len(f.strip()) > 0]
    features_descontructed: list[dict[str, str]] = []
    new_features: list[dict[str, str]] = []

    for feature in feature_list:
        title = feature.split('title:')[-1].split('details:')[0].strip()
        details = feature.split('details:')[-1].split('link:')[0].strip()
        link = feature.split('link:')[-1].strip()

        features_descontructed.append({
            'title': title,
            'details': details,
            'link': link
        })
    
    new_features.append({
        'title': f"'{new_title}'",
        'details': f'"{new_details}"',
        'link': f"'{urllib.parse.quote(new_link)}'"
    })

    new_features.append({
        'title': features_descontructed[0]['title'],
        'details': features_descontructed[0]['details'],
        'link': features_descontructed[0]['link'],
    })

    new_features.append({
        'title': features_descontructed[1]['title'],
        'details': features_descontructed[1]['details'],
        'link': features_descontructed[1]['link'],
    })

    # Reconstrcut the full index.md
    new_features_md = "features:\n"
    for feature in new_features:
        new_features_md += f"  - title: {feature['title']}\n    details: {feature['details']}\n    link: {feature['link']}\n"
    new_features_md += "---\n"

    return full_index_md.split('features:')[0] + new_features_md + full_index_md.split('---')[-1]

