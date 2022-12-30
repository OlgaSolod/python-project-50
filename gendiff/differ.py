from gendiff import make_diff, parsing



def generate_diff(filepath1, filepath2):
    file1 = parsing(filepath1)
    file2 = parsing(filepath2)
    diff = make_diff(file1, file2)
    return diff
   
    
   

