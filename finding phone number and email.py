import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
     )''', re.VERBOSE)

text = str(paperclip.paste())
match = []
for groups in phoneRegex.finadall(text):
    numbers = '-'.join([group[1],groups[3],groups[5]])
    if group[8] != ' ':
        numbers += ' x' + groups[8]
    match.append(numbers)
for groups in emailRegex.findall(text):
     match.append(groups[0])

if len(match) > 0:
    paperclip.copy('\n'.join(match))
    print('copied to clipboard')
    print('\n'.join(match))
else:
    print('no numbers or email found')
