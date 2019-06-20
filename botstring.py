# - *- coding: utf- 8 - *-
# (c) by Alex (t.me/gobi_todic)
botstring = {
    "start":
    """Hi, I am the Bot 🤖 from Border Violence Monitoring (www.borderviolence.eu)
I am quite new, I don't have many functions and not everything is working.
To get some statistics 📊 about our reports, please press or type /statistics
To export the reports as a pdf 📄, please press or type /createpdf
To export the reports as a csv 🗒, please press or type /createcsv
If you need any help ⁉️, please press or type /help""",
    "createpdf":
    """I will export the reports for a certain timeframe in a pdf 📄 for you.
To do so I will need the begin date of the timeframe.
Please give me the begin date in the following format:
'/begin YYYY-MM-DD'
Example: '/begin 2019-10-31'""",
    "createcsv":
    """I will export the reports for a certain timeframe in a csv 📊 for you.
To do so I will need the begin date of the timeframe.
Please give me the begin date in the following format:
'/begin YYYY-MM-DD'
Example: '/begin 2019-10-31'""",
    "begin_error":
    """❌❌❌ The date you gave me was not correct. Please give in the correct format for the begin date:
'/begin YYYY-MM-DD'
Example: '/begin 2019-04-20'""",
    "begin_correct":
"""You gave me a correct ✅ begin date: 📅 %s/%s/%s""",
    "begin_to_end":
    """Now I need the end date from you.
Please give me the end date in the following format:
'/end YYYY-MM-DD'
Example: '/end 2019-04-20'""",
    "end_no_begin":
    """You didn't give me any begin date 😔
Please give me the begin date in the following format:
'/begin YYYY-MM-DD'
Example: '/begin 2019-10-31'""",
    "end_error":
    """❌❌❌ The date you gave me was not correct. Please give in the correct format for the end date:
'/end YYYY-MM-DD'
Example: '/end 2019-04-20'""",
    "end_before_start":
    """"I don't have a time machine 🕰 The end date must be AFTER the starting date.
Please change '/start YYYY-MM-DD' or '/end YYYY-MM-DD'""",
    "end_correct":
     """You gave me a correct ✅ end date: 📅 %s/%s/%s""",
    "end":
    """Do you want me to export the reports 📄 for you?
📅 The start date is: %s/%s/%s
📅 End date: %s/%s/%s
Please press or type /export%s""",
"exportpdf_start":
"""The exporting started. This can take some minutes. Go & have a ☕️""",
"exportpdf_info":
"""I found %d reports in the timeframe you selected.""",
"exportpdf":
""" ✅ Export is done 😌""",
"exportpdf_no_reports":
"""For the selected timeframe there are not respors. Please try another timeframe.
/createpdf""",
"exportcsv_start":
"""The exporting started. This can take some minutes. Go & have a ☕️""",
"exportcsv_info":
"""I found %d reports in the timeframe you selected.""",
"exportcsv":
""" ✅ Export is done 😌""",
"exportcsv_no_reports":
"""For the selected timeframe there are not respors. Please try another timeframe.
/createcsv""",
"undefined":
"""What are you trying to tell me? I don't understand 🙉
Do you need /help?""",
"help":
"""The website www.borderviolence.eu documents illegal push-backs and police violence inflicted by EU member state authorities.I am a bot trying to help you with our reports.
Sorry if not everything is working perfect. I am quite new and I don't have many functions yet.
To get some statistics 📊 about our reports, please press or type /statistics
To export the reports as a pdf 📄, please press or type /createpdf
To export the reports as a csv 🗒, please press or type /createcsv
If you want to give feedback or talk to my CREATOR 🧟‍, write a message to t.me/gobi_todic""",
"statistics":
""" 📊 So far I can only tell you the amount of reports in our database:
There are currently %d reports."""
}