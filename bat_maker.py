print('Type path to folder where files will be stored')
path_to_bat_files_store = input()
print('Type path to studio')
path_to_studio = input()
print('Type path to repeater script')
path_to_repeater_script = input()
print('Type path to action log file')
path_to_log_file = input()
command = 'java -jar ' + path_to_studio + ' -r ' + path_to_repeater_script + ' -- ' + path_to_log_file
bat_path = path_to_bat_files_store + 'action.bat'
action_bat = open(bat_path,'w+')
action_bat.write(command)
action_bat.close()
vbs_path = path_to_bat_files_store + 'command_vbs.vbs'
vbs_file = open(vbs_path,'w+')
vbs_file_command = "Set WshShell = CreateObject(\"WScript.Shell\")\n WshShell.Run chr(34) & \"" + bat_path +"\" & Chr(34), 0\nSet WshShell = Nothing"
vbs_file.write(vbs_file_command)
vbs_file.close()


print('Do you want to create bat files to add your task in windows sheduler [y/n]?')
y_n = input()
if y_n == 'y':
    print('Type sheduletype (MINUTE,HOURLY,DAILY,WEEKLY e.t.c.)')
    shedule_type = input()
    print('Type taskname for sheduler')
    task_name = input()
    print('Type exact time in format HH:mm')
    exact_time = input()
    create_command = 'schtasks /create /sc ' + shedule_type +' /tn ' + task_name + ' /tr ' +  vbs_path + ' /st 11:25'
    delete_command = 'schtasks /delete /tn ' + task_name
    create_bat = open(path_to_bat_files_store + 'create.bat','w+')
    create_bat.write(create_command)
    create_bat.close()
    delete_bat = open(path_to_bat_files_store + 'delete.bat','w+')
    delete_bat.write(delete_command)
    delete_bat.close()


