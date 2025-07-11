from serpapi import GoogleSearch

params = {
    "engine": "google",
    "q": "site:allrecipes.com inurl:/recipe/",
    "num": "100",
    "api_key": "5e40ff678839123d9491dc9966513d67079c6c68ad89596de69387cd78b36cd5"
}

search = GoogleSearch(params)
results = search.get_dict()
urls = [res['link'] for res in results['organic_results']]

print(urls)