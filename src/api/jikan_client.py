import requests
base_url = "https://api.jikan.moe/v4"

def search_anime(query):
    """Search for anime by title using the Jikan API."""
    url = f"{base_url}/anime?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_anime_details(anime_id):
    """Get detailed information about an anime by its ID."""
    url = f"{base_url}/anime/{anime_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_top_anime():
    """Get a list of top anime."""
    url = f"{base_url}/top/anime"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_anime_characters(anime_id):
    """Get characters of an anime by its ID."""
    url = f"{base_url}/anime/{anime_id}/characters"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
#score compare
def compare_anime_scores(anime_id1, anime_id2):
    details1 = get_anime_details(anime_id1)
    details2 = get_anime_details(anime_id2)
    assert details1['data']['score'] > 0
    assert details2['data']['score'] > 0

    return details1, details2
