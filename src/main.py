from api.jikan_client import ( 
    search_anime,
    get_anime_details, 
    get_top_anime, 
    get_anime_characters
) 
def main():
    # Example usage of the Jikan API client     
    while True:
        print("Welcome to the Anime Search App!")
        print("1. Search for an anime")
        print("2. Get details of an anime by ID")
        print("3. Get top anime")
        print("4. Get characters of an anime by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':   
            query = input("Enter anime title to search: ")
            results = search_anime(query)
            if results:
                for anime in results['data']:
                    print(f"{anime['mal_id']}: {anime['title']}")
        elif choice == '2':
            anime_id = input("Enter anime ID: ")
            details = get_anime_details(anime_id)
            if details:
                print(details['data'])
        elif choice == '3':
            top_anime = get_top_anime()
            if top_anime:
                for anime in top_anime['data']:
                    print(f"{anime['mal_id']}: {anime['title']}")
        elif choice == '4':
            anime_id = input("Enter anime ID: ")
            characters = get_anime_characters(anime_id)
            if characters:
                for character in characters['data']:
                    print(f"{character['character']['name']} - {character['role']}")

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")