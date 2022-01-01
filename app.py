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
    return text.replace(" ", "%20").lower()


def main():
    keywords = ["programming", "software development", "coding", "python", "java", "php", "web", "ai", "machine learning"]
    country = "uk"
    location = "Doncaster"
    for keyword in keywords:
        url = f"https://{country}.indeed.com/jobs?q={text_to_html(keyword)}&l={location}&vjk=38d83016285aee43"
        print(get_element_by_tag(url, "title"))


if __name__ == "__main__":
    main()
