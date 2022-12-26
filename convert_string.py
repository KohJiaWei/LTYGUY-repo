""" FOR converting file paths to correct format for reading csv files """
# http://www.unit-conversion.info/texttools/replace-text/ good enough



def convert_string(string):
    string.replace("\\","/")
    print(string)
    return string

print(convert_string(r"C:\Users\kohji\example"))
