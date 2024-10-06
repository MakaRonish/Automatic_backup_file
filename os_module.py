import os




# print(os.getcwd())

# os.chdir("C:/Users/ronis\OneDrive - Global College of Management/automatic_back")
# os.chdir("C:/Users/ronis\OneDrive - Global College of Management/automatic_back")
# print(os.getcwd())
# print(os.listdir())

"""make"""
# os.mkdir("test1")
# os.makedirs("test2/sub")

"""delete"""
# os.rmdir("test1")
# os.removedirs("test2/sub")

"""rename"""
# os.mkdir("test1")
# os.rename("test1","demo")


"""detail"""
from datetime import datetime
# print(os.stat('demo'))
# mode_time=os.stat('demo').st_mtime
# print(datetime.fromtimestamp(mode_time))


# os.chdir("C:/Users/ronis/OneDrive - Global College of Management/2nd cloud")


# for dirpath, dirnames , filenames in os.walk(os.getcwd()):
#     print("current path: ", dirpath)
#     print("Directories: ", dirnames)
#     print("FIles: ",filenames)
#     print()


# for dirpath, dirnames , filenames in os.walk(os.getcwd()):
#     for file in filenames:
#         if file=="error.html":
#             print("current path: ", dirpath)
#             print("Directories: ", dirnames)
#             print("FIles: ",filenames)
#             print("run")
#             print()


# print(os.path.basename('C:/Users/ronis/OneDrive - Global College of Management/2nd cloud'))
# print(os.path.split('C:/Users/ronis/OneDrive - Global College of Management/2nd cloud'))
# print(os.path.exists('C:/Users/ronis/OneDrive - Global College of Management/2nd cloud'))
# print(os.path.splitext('test.txt'))


print(dir(os.path))




