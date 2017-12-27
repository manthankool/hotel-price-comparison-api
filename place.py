def search(city):
    try:
        from google import search
    except ImportError:
        return{'message':"No module named 'google' found"}
    k=list()
    # to search
    query = city + "hotels tripadvisor"

    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        k.append(j)
    return(k[0])
