#!/bin/sh
# INSTRUCTIONS ON HOW TO MAKE A SHELL SCRIPT WATCH FOR tcqBot.py DEATH, AND IF SO RESURRECT IT:

# 1) nano tcbots.sh
# 	 copy paste the following into tcbots.sh

ps auxw | grep tcqBot.py | grep -v grep > /dev/null
if [ $? != 0 ]
then
        torsocks python /home/bots/tcqBot.py > /dev/null
fi

# 2) Once you have saved the script, you must give it executable permissions in order to be able to run it:
#    chmod +x tcbots.sh

# 3) With the script in hand, we need to set up the schedule on which it will run. The cron utility allows us to schedule at what intervals the script should execute. Start by opening up the cron file:
#    crontab -e

# 4) Every five minutes would be set up like this:
#    */5 * * * * ~/tcbots.sh
