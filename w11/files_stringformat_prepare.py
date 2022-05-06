# FILES DEMO
# create a .txt file to call information from
# courses_file = open("/Users/celestegeorge/Downloads/vs/w11/courses.txt")
# ######## open(filename)
# ######## with open(filename) as file_variable:
# 
# with open("/Users/celestegeorge/Downloads/vs/w11/courses.txt") as courses_file: # same thing as line 3 BUT better than line 3 bc it can close file
#     for line in courses_file:
#         print(line)
#     print("Goodbye") # not needed
# print("The file is closed now.") # not needed






# SPLITTING STRINGS
# colors = "red,green,blue,yellow"

# color_parts = colors.split(",")
## PRINTS OUT ['red', 'green', 'blue', 'yellow']

# print(colors)
# print(color_parts)

# for color in color_parts:
#     print(color)
## PRINTS OUT one color on every line

# second = color_parts[1]
# print(second)




# REMOVING WHITESPACE IN STRINGS
# name = "      Tete Register       "

# # clean = name.strip() # get rid of leading or trailing whitespace 
# name = name.strip()

# print(f"---{name}---")
# # print(f"---{clean}---")






# READING FILES & PARSING STRINGS
with open("/Users/celestegeorge/Downloads/vs/w11/courses.txt") as courses_file:
    for line in courses_file:
        # line = "CSE 110,98.5"
        line = line.strip()  # cleaning whitespace
        parts = line.split(",")  # splitting string into pieces

        # parts = ["CSE 110", "98.5"]
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f"{name} - Grade: {grade}, after bonus: {bonus_grade}")