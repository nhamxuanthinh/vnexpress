from crontab import CronTab

cron = CronTab(user='nhamthinh')
job = cron.new(command='cd ~/projects/vnexpress && scrapy crawl home', comment='minute')
job.hour.every(1)
# job.minute.every(1)
# cron.remove_all()
cron.write()