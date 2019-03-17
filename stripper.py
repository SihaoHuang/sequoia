data = open("course_data.json", "r").read()
output = open("edited_course.json", "w")

data = data.replace("-", "_")
data = data.replace("GIR:", "GIR_")
data = data.replace("*", "_")
data = data.replace(";", "_")
data = data.replace("$", "_")
data = data.replace("!", ".")
data = data.replace("@", "_")
data = data.replace("%", " percent ")
data = data.replace("&", " and ")
data = data.replace("+", " plus ")
data = data.replace("?", ".")
data = data.replace("<em>", ".")
data = data.replace("</em>", ".")
# data = data.replace("Women: Dragon", "Women, Dragon")
# data = data.replace("ation: Feminist", "ation, Feminist")
# data = data.replace("ersections: Queer Li", "ersections, Queer Li")
# data = data.replace("and Beyond: A Psycho", "and Beyond, A Psycho")
# data = data.replace("Inequality: Reproduc", "Inequality, Reproduc")
# data = data.replace("ck Matters: Introduc", "ck Matters, Introduc")
# data = data.replace("Ind Stdy: Science", "Ind Stdy, Science")
# data = data.replace("ing Apollo: The Moon", "ing Apollo, The Moon")
# data = data.replace("questions: how have", "questions, how have")
# data = data.replace("DV Lab: Document", "DV Lab, Document")
# data = data.replace("with Risk: Threats", "with Risk, Threats")
# data = data.replace("Americans:Sci,Tech", "Americans. Sci,Tech")
# data = data.replace("ing People: A Histor", "ing People, A Histor")
# data = data.replace("DV Lab: Document", "DV Lab, Document")
    

list_chars = list(data)

print(list_chars[584443:584455])

i = 0
quote_count = 0
while i < len(list_chars):
    if (list_chars[i] == "\"") and (list_chars[i-1:i] != "\\:"):
        quote_count += 1
    if quote_count % 2 == 1 and list_chars[i] == ":":
        list_chars[i] = ","
    i += 1

new_file = ''.join(list_chars)


i = 1
while i < len(new_file):
    if new_file[i] == ":":
        if not(new_file[i - 1] == "\"" and (new_file[i + 1] == "\"" or new_file[i + 1] == "[")):
            print(new_file[i-10:i+10])
    i += 1

output.write(new_file)
output.close()



