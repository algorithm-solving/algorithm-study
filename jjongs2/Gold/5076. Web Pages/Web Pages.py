from sys import stdin

read = stdin.readline

NOT_FOUND = -1


def is_valid(html):
    tag_types = []
    tag_end = -1
    while (tag_start := html.find('<', tag_end + 1)) != NOT_FOUND:
        tag_end = html.find('>', tag_start + 1)
        tag = html[tag_start + 1:tag_end]
        if tag[-1] == '/':
            continue
        if tag[0] != '/':
            tag_types.append(tag.split()[0])
            continue
        if not tag_types:
            return False
        if tag[1:] != tag_types[-1]:
            return False
        tag_types.pop()
    return True if not tag_types else False


results = ['legal' if is_valid(html) else 'illegal' for html in iter(lambda: read().strip(), '#')]
print('\n'.join(results))
