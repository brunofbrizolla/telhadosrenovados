import os
import glob
import re

directory = r"C:\Users\Lenovo\Downloads\TELHADOS RENOVADOS\roovon_clone\newkit.creativemox.com\roovon"
html_files = glob.glob(os.path.join(directory, "*.html"))

new_dropdown = """<ul class="crh-dropdown">
                        <li><a href="instalacao-telhados.html">Instala&ccedil;&atilde;o de Telhados</a></li>
                        <li><a href="reparacao-telhados.html">Repara&ccedil;&atilde;o de Telhados</a></li>
                        <li><a href="sistemas-impermeabilizacao.html">Impermeabiliza&ccedil;&atilde;o</a></li>
                        <li><a href="limpeza-telhados.html">Limpeza e Manuten&ccedil;&atilde;o</a></li>
                    </ul>"""

# The regex will find <ul class="crh-dropdown"> ... </ul> and replace it.
# We need to be careful not to match too much.
pattern = re.compile(r'<ul\s+class="crh-dropdown"\s*>.*?</ul>', re.IGNORECASE | re.DOTALL)

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, count = pattern.subn(new_dropdown, content)
        
        if count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated dropdown in {os.path.basename(file_path)} ({count} replacements)")
    except Exception as e:
        print(f"Error processing {os.path.basename(file_path)}: {e}")

print("Update complete!")
