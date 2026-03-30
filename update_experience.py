import os
import glob
import re

directory = r"C:\Users\Lenovo\Downloads\TELHADOS RENOVADOS\roovon_clone\newkit.creativemox.com\roovon"
html_files = glob.glob(os.path.join(directory, "*.html"))

# Patterns to update experience
# 1. Stat item: <span class="stat-num">+15</span> or similar
stat_pattern = re.compile(r'(<span class="stat-num">)\+?\d+(</span><span class="stat-label">Anos Experi&ecirc;ncia</span>)', re.IGNORECASE)

# 2. SEO text in about section
# Find the paragraph starting with "Na Telhados Renovados, somos especialistas..."
about_pattern = re.compile(r'(Na Telhados Renovados, somos especialistas na instala&ccedil;&atilde;o e repara&ccedil;&atilde;o de coberturas\. Com )([\w\s&;]+)( experi&ecirc;ncia acumulada)', re.IGNORECASE)

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update stats
        updated_content = stat_pattern.sub(r'\1+25\2', content)
        
        # Update about text
        updated_content = about_pattern.sub(r'\1mais de 25 anos de\3', updated_content)
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated experience in {os.path.basename(file_path)}")
        else:
            print(f"No changes needed in {os.path.basename(file_path)}")
            
    except Exception as e:
        print(f"Error processing {os.path.basename(file_path)}: {e}")

print("Update complete!")
