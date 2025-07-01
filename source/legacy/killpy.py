# encoding: utf-8


# author: Ankit Singh
# email: singhanki67@gmail.com


import subprocess


# import os
# os.system('taskkill /f /im Python.exe')
cmd = 'taskkill /f /im Python.exe'
p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
raw_data = p.communicate()[0]
p.stdin.close()
p.stdout.close()
p.stderr.close()
