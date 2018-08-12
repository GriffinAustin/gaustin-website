def sluggify(title):
    title = title.lower()
    acceptable_chars = "abcdefghijklmnopqrstuvwxyz1234567890-_"
    slug = ""
    for i in range(len(title)):
        if title[i] in acceptable_chars:
            slug += title[i]
        elif title[i] == " ":
            slug += "-"
    slug = list(slug)
    while slug[len(slug)-1] == "-" or slug[len(slug)-1] == "_":
        slug.pop()
    slug = "".join(slug)
    return slug
