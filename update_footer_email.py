import os
import glob
import re

directory = r"C:\Users\Lenovo\Downloads\TELHADOS RENOVADOS\roovon_clone\newkit.creativemox.com\roovon"
html_files = glob.glob(os.path.join(directory, "*.html"))

# 1. Update Email
email_pattern = re.compile(r'contacto@telhadosrenovados\.pt', re.IGNORECASE)
new_email = 'telhadosrenovados@outlook.pt'

# 2. Update Footer Services
# Look for the "As Nossas Especialidades" or "Especialidades" section in footer
footer_services_pattern = re.compile(r'(<h4>(?:As Nossas )?Especialidades</h4>\s*<ul>)([\s\S]*?)(</ul>)', re.IGNORECASE)

new_footer_services = """
                    <li><a href="instalacao-telhados.html">Instala&ccedil;&atilde;o de Telhados</a></li>
                    <li><a href="reparacao-telhados.html">Repara&ccedil;&atilde;o de Telhados</a></li>
                    <li><a href="sistemas-impermeabilizacao.html">Impermeabiliza&ccedil;&atilde;o</a></li>
                    <li><a href="limpeza-telhados.html">Limpeza e Manuten&ccedil;&atilde;o</a></li>"""

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update email
        updated_content = email_pattern.sub(new_email, content)
        
        # Update footer services
        # Check if the pattern matches
        if footer_services_pattern.search(updated_content):
            updated_content = footer_services_pattern.sub(r'\1' + new_footer_services + r'\3', updated_content)
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated {os.path.basename(file_path)}")
        else:
            print(f"No changes in {os.path.basename(file_path)}")
            
    except Exception as e:
        print(f"Error in {os.path.basename(file_path)}: {e}")

print("Site-wide update complete!")
