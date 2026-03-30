import codecs

with codecs.open('roovon_clone/newkit.creativemox.com/roovon/index.html', 'r', 'utf-8') as f:
    html = f.read()

hdr_end = html.find('</header>')
print("Header ends at:", hdr_end)

footer_start = html.find('<footer')
print("Footer starts at:", footer_start)

# what is between them? Let's check the first 500 chars after </header>
print("After header:\n", html[hdr_end:hdr_end+500])
