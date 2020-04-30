""" Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from crontab import CronTab

#Set cron environment within container
cron = CronTab(user='root')
cron.env['SHELL'] = '/bin/bash'
cron.env['PATH']='/usr/local/bin'
#Set cron timezone to EST
cron.env['TZ']='America/New_York'
job=cron.new(command='cd /app/ && python3.8 functions.py')
job.minute.every(1)
cron.write(user='root')

print("Cron job has been added!")
