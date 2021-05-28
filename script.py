import os
import os.path
import shutil

FILE_DIR = 'C:\\Program Files\\Microsoft SQL Server\\MSSQL13.MSSQLSERVER\\MSSQL\\Backup\\trn_bkp'
SAVE_DIR = FILE_DIR+"\\output"
DATABASE_NAME = "DEMO"

if os.path.exists(SAVE_DIR):
    shutil.rmtree(SAVE_DIR)
# all_file_names = os.listdir(FILE_DIR)
all_trn_files = [file for file in os.listdir(FILE_DIR) if (file.lower().endswith('.trn'))]
def get_timestamp(file_name):
    return file_name.split("_")[-2].split('.')[0]

all_file_names = sorted(all_trn_files, key=get_timestamp)


if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

completeName = os.path.join(SAVE_DIR, "output.txt")         
f = open(completeName, "w")

total_number_of_files = len(all_file_names)
print("============ Total number of files found "+str(total_number_of_files)+" ============")
print("===============Statting to convert====================")
count= 1;
for single_file in all_file_names:
	print(single_file)
	if (count==len(all_file_names)) :
		f.write("RESTORE LOG ["+DATABASE_NAME+"] FROM  DISK = N'"+FILE_DIR+"\\"+single_file+"' WITH  FILE = 1, NOUNLOAD,  STATS = 10")
	else :
		f.write("RESTORE LOG ["+DATABASE_NAME+"] FROM  DISK = N'"+FILE_DIR+"\\"+single_file+"' WITH  FILE = 1, NORECOVERY, NOUNLOAD,  STATS = 10")
	f.write("\n")
	f.write("GO")
	f.write("\n")
	f.write("\n")
	f.write("\n")
	count=count+1
f.close()
print("===============Conversation completed=================")
print("please find the output in "+SAVE_DIR)

