import requests

def main():
    # res = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    result = requests.get("https://www.googleapis.com/books/v1/volumes?q=T. + E. + Grau")
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = result.json()

    for info in data["items"]:
    	details = info["volumeInfo"]
        print("")
        print("Title: " + details["title"])
        print("Author(s): ")
    	for author in  details["authors"]:
            print(author.encode("latin-1"))
        # print("Author(s): " + ', '.join(str(author.encode("latin-1")) for author in details["authors"]))
        if "publisher" in details:
            print("Publisher: " + details["publisher"])
        else:
            print("No publisher indicated.")
        print(details["imageLinks"]["thumbnail"])
        print("More information at " + details["canonicalVolumeLink"])

if __name__ == "__main__":
    main()