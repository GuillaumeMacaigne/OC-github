# -*- coding: utf-8 -*-
import csv

#SESSIONS CONCATENATION

data = []

with open('sessions_with_ID.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    # header = next(reader)
    for row in reader:
        session_str = "*"
        session_id = ""
        cell_number = 1
        for cell in row:
            if cell_number == 1:
                sessions_id = cell
                cell_number += 1
            elif cell_number < 4:
                session_str += cell + '|'
                cell_number += 1
            else:
                session_str += cell + "*"
        sessions_line = [sessions_id, session_str]
        data.append(sessions_line)

#write
with open('result.csv', 'w+') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(data)

#=> Merge both scripts
#LINES CONCATENATION

data = []

with open('result.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    formation_id = ""
    formation_sessions = ""
    for row in reader:
        if row[0] != formation_id:
            line = (formation_id, formation_sessions)
            data.append(line)
            formation_id = row[0]
            formation_sessions = row[1]
        else:
            formation_sessions += row[1]

#write
with open('result2.csv', 'w+') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(data)

