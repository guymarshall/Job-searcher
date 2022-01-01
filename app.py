# web scrape for jobs on totaljobs and indeed
# email results daily
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


def main():

    url = "http://olympus.realpython.org/profiles/aphrodite"

    # page = urlopen(url)

    # print(page)

    # html_bytes = page.read()
    # html = html_bytes.decode("utf-8")

    # title_index = html.find("<title>")
    # start_index = title_index + len("<title>")
    # end_index = html.find("</title>")
    # title = html[start_index:end_index]

    print(get_element_by_tag(url, "title"))

if __name__ == "__main__":
    main()

# keywords = ["programming", "software development", "coding", "python", "java", "php", "web", "ai", "machine learning"]
