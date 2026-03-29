"""Swap Experience and Projects sections in index.html so Experience comes first"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find section markers
projects_start = content.find('<!-- PROJECTS SECTION -->')
projects_end = content.find('<!-- EXPERIENCE SECTION -->')
experience_end = content.find('<!-- ACHIEVEMENTS SECTION -->')

# Extract sections
before_projects = content[:projects_start]
projects_section = content[projects_start:projects_end]
experience_section = content[projects_end:experience_end]
after_experience = content[experience_end:]

# Swap the background classes
# Experience should have no bg (plain dark), Projects should have bg-white/[0.01]
experience_section = experience_section.replace('class="py-32 px-6 bg-white/[0.01]"', 'class="py-32 px-6"')
projects_section = projects_section.replace('class="py-32 px-6"', 'class="py-32 px-6 bg-white/[0.01]"')

# Rebuild with swapped order: Experience first, then Projects
new_content = before_projects + experience_section + projects_section + after_experience

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Sections swapped successfully!")
print("   Experience now appears before Projects on the page")
