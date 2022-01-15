from urllib.request import urlopen


def get_element_by_tag(url, html_tag):
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    index = html.find(f"<{html_tag}>")
    start_index = index + len(f"<{html_tag}>")
    end_index = html.find(f"</{html_tag}>")
    element = html[start_index:end_index]
    return element


def text_to_html(text):
    return text.replace(" ", "%20").replace(",", "%2C").lower()


def main():
    search_terms = ["programming", "software development", "coding", "python", "java", "php", "web", "ai", "machine learning"]
    country = "uk"
    location = "Doncaster, South Yorkshire"
    for search_term in search_terms:
        url = f"https://{country}.indeed.com/jobs?q={text_to_html(search_term)}&l={text_to_html(location)}&vjk=38d83016285aee43"
        print(get_element_by_tag(url, "title"))


if __name__ == "__main__":
    main()



# for the wrapper!!!!!!! (make it send emails instead)
# params = {
#     'publisher': "",    # publisher ID (Required)
#     'q': "",            # Job search query
#     'l': "",            # location (city / state)
#     'co': "",           # Two letter Country Code
#     'sort': "",         # Sort order, date or relevance
#     'days': ""          # number of days to fetch jobs, maximum is 7 days
# }
