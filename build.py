"""Builds privacy.html from privacy-policy.md: python3 build.py"""
import markdown, pathlib
md = pathlib.Path('privacy-policy.md').read_text()
body = markdown.markdown(md)
tpl = pathlib.Path('_page.html').read_text()
pathlib.Path('privacy.html').write_text(tpl.replace('{{TITLE}}', 'Privacy Policy · Lyrichord').replace('{{BODY}}', body))
