import requests

def main():
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "5JCTgW3KWZrZ302j2ouhQ", "isbns": "9781632168146"})
    print(res.json())

if __name__ == "__main__":
    main()
