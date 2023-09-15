import json
preName = 'ACCT'
# Initialize variables to store section data
sections = []
current_section = {}
jumpToNextLine = False
# Open the input file for reading
with open(f'{preName}.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    read_course_name = False

    for line in lines:
        line = line.strip()

        if not line:
            continue
        print(line)
        # Check if the line contains a course name
        if line.startswith(preName):
            current_section['name of course'] = line.split()[0]
            print(current_section['name of course'])
            read_course_name = True
            continue

        # Skip unneeded data lines
        if read_course_name:
            read_course_name = False
            continue

        # Check if the line contains section information

        # print(match)
        if line.split('\t')[0] == 'Lecture':
            current_section['sec'] = int(line.split('\t')[1])
            # print(match.group(1))
            current_section['name of instructor'] = line.split('\t')[2]
            current_section['number of students'] = line.split('\t')[3]
            jumpToNextLine = True
            continue

        # Check if the line contains days, time, and place
        if jumpToNextLine:
            current_section['days'] = line.split('\t')[0]
            current_section['time'] = line.split('\t')[1]
            current_section['place'] = line.split('\t')[2]
            sections.append(current_section.copy())
            print(sections)
            jumpToNextLine = False

# Save the sections data as a JSON file
with open(f'{preName}.json', 'w', encoding='utf-8') as json_file:
    json.dump(sections, json_file, ensure_ascii=False, indent=4)

print("Data has been extracted and saved to 'sections.json'.")
