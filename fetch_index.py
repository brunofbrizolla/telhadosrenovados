import urllib.request
import os
import re

url = "https://newkit.creativemox.com/roovon/"
dest = "roovon_clone/newkit.creativemox.com/roovon/index.html"

print(f"Fetching {url}...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8', errors='ignore')

print("Applying safe CORS fixes to the original HTML...")

# 1. Remove <link> tags pointing to newkit.creativemox.com
html = re.sub(
    r'<link\b[^>]*href="https?://newkit\.creativemox\.com[^"]*"[^>]*/?>',
    '',
    html, flags=re.IGNORECASE
)

# 2. Remove external <script src="...newkit..."> blocks
html = re.sub(
    r'<script\b[^>]+src="https?://newkit\.creativemox\.com[^"]*"[^>]*>\s*</script>',
    '',
    html, flags=re.IGNORECASE
)

# 3. Fix Elementor/WordPress inline JS safely (DO NOT REMOVE THE SCRIPT TAG CONTENT ENTIRELY)
# Just erase the specific URLs causing issues within the JSON.
html = re.sub(
    r'"ajaxurl":"https?:\\/\\/newkit\.creativemox\.com[^"]*"',
    '"ajaxurl":""',
    html, flags=re.IGNORECASE
)

html = re.sub(
    r'"nonce":"[a-zA-Z0-9]+"([^}]*)"ajaxurl"',
    r'"nonce":""\1"ajaxurl"',
    html, flags=re.IGNORECASE
)

# 4. Remove speculationrules scripts
html = re.sub(
    r'<script type="speculationrules">.*?</script>',
    '',
    html, flags=re.DOTALL | re.IGNORECASE
)

# 5. Fix broken phone regex pattern
html = html.replace('pattern="[0-9()#&amp;+*-=.]+"', 'pattern="[0-9()#&amp;+*=.-]+"')

print("Writing to file...")
with open(dest, "w", encoding="utf-8") as f:
    f.write(html)

print("Done restoring and fixing index.html!")
