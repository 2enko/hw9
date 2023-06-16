def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def get_article(title):
    article_content = f"This is the content of the article: {title}"
    return article_content

def article_content_generator(filename):
    titles_generator = read_titles(filename)
    for title in titles_generator:
        article_content = get_article(title)
        yield article_content

def calculate_average_letter_count(filename):
    letter_count = 0
    article_count = 0

    for article_content in article_content_generator(filename):
        letter_count += len(article_content)
        article_count += 1

    if article_count > 0:
        average_letter_count = letter_count / article_count
        return average_letter_count
    else:
        return 0

filename = 'small.txt'
average_letter_count = calculate_average_letter_count(filename)
print(f"Average letter count per article: {average_letter_count}")
