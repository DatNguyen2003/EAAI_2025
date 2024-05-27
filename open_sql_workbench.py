import subprocess

def open_sql_workbench():
  # Replace 'path_to_mysql_workbench' with the actual path to MySQL Workbench executable
  mysql_workbench_path = r'C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe'

  # Launch MySQL Workbench
  subprocess.run([mysql_workbench_path])