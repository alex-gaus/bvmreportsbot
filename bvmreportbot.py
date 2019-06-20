# - *- coding: utf- 8 - *-
# (c) by Alex (t.me/gobi_todic)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from credentials import telegram_bot_token
from check_date import (check_date, check_date_logic)
from reports import (get_reports,sort_reports,json_to_csv)
from html_to_pdf import html_to_pdf
from merge_pdf import merge_pdf
from add_footer import add_footer
from botstring import (botstring)
import os
import logging
import sys
logging.basicConfig(level=logging.INFO)

users = {}
    

def start(bot, update):
    update.message.reply_text(botstring["start"])
    
def createpdf (bot, update):
    update.message.reply_text(botstring["createpdf"])
    users[update.message.chat.id] = {"type":"pdf"}

def createcsv (bot, update):
    update.message.reply_text(botstring["createcsv"])
    users[update.message.chat.id] = {"type":"csv"}

    
def begin (bot, update):
    try:
        users[update.message.chat.id]
    except KeyError:
        undefined(bot,update)
    date = check_date(update.message.text[6:])
    if date == False:
        update.message.reply_text(botstring["begin_error"])
    else:
        users[update.message.chat.id].update({
            "begin_year" : date["year"],
            "begin_month" : ("0%s"%(date["month"]))[-2:],
            "begin_day" : ("0%s"%(date["day"]))[-2:]})
        update.message.reply_text(botstring["begin_correct"]%(users[update.message.chat.id]["begin_year"],users[update.message.chat.id]["begin_month"],users[update.message.chat.id]["begin_day"]))
        update.message.reply_text(botstring["begin_to_end"])
    return users


def end (bot, update):
    try:
        users[update.message.chat.id]
    except KeyError:
        undefined(bot,update)
    try:
        y= users[update.message.chat.id]["begin_year"]
    except:
        update.message.reply_text(botstring["end_no_begin"])
        return
    date = check_date(update.message.text[4:])
    if date == False:
        update.message.reply_text(botstring["end_error"])
        return
    else:
        users[update.message.chat.id].update({
                "end_year" : str(date["year"]),
                "end_month" : ("0%s"%(date["month"]))[-2:],
                "end_day" : ("0%s"%(date["day"]))[-2:]})
        if check_date_logic(users[update.message.chat.id]) == False:
            update.message.reply_text(botstring["end_before_start"])
            return
        else:
            update.message.reply_text(botstring["end_correct"]%(users[update.message.chat.id]["end_year"],users[update.message.chat.id]["end_month"],users[update.message.chat.id]["end_day"]))
            update.message.reply_text(botstring["end"]%(users[update.message.chat.id]["begin_year"],users[update.message.chat.id]["begin_month"],users[update.message.chat.id]["begin_day"],users[update.message.chat.id]["end_year"],users[update.message.chat.id]["end_month"],users[update.message.chat.id]["end_day"],users[update.message.chat.id]["type"]))
    return  users

def exportpdf (bot, update):
    try:
        users[update.message.chat.id]
    except KeyError:
        undefined(bot,update)
    print(users[update.message.chat.id])
    update.message.reply_text(botstring["exportpdf_start"])
    reports = get_reports()
    start="%s%s%s"%(users[update.message.chat.id]["begin_year"],users[update.message.chat.id]["begin_month"],users[update.message.chat.id]["begin_day"])
    end="%s%s%s"%(users[update.message.chat.id]["end_year"],users[update.message.chat.id]["end_month"],users[update.message.chat.id]["end_day"])
    reports_sorted = sort_reports(reports,str(start),str(end))
    if len(reports_sorted)>0:
        update.message.reply_text(botstring["exportpdf_info"]%(len(reports_sorted)))
        mergeList = []
        for report in reports_sorted:
            name = "%s.pdf"%((report["report_link"][46:-1]))
            mergeList.append(name)
            link = report["report_link"]
            html_to_pdf (link,name, False)
        merge_pdf(mergeList,"pdfs",str(update.message.chat.id))
        add_footer("pdfs/%s"%(update.message.chat.id),"pdfs/%s"%(update.message.chat.id))
        update.message.reply_text(botstring["exportpdf"])
        try:
            bot.send_document(chat_id=update.message.chat.id, timeout=360, document=open('pdfs/%s.pdf'%(str(update.message.chat.id)), 'rb'))
            logging.info("The file pdfs/%s.pdf was sent"%(str(update.message.chat.id))) 
            if os.path.exists('pdfs/%s.pdf'%(str(update.message.chat.id))):
                os.remove('pdfs/%s.pdf'%(str(update.message.chat.id)))
            else:
                logging.info("The file pdfs/%s.pdf does not exist"%(str(update.message.chat.id))) 
        except:
            logging.info("Sending of document not possible")
    else:
        logging.info("For timeframe no reports")
        update.message.reply_text(botstring["exportpdf_no_reports"])

def exportcsv (bot, update):
    try:
        users[update.message.chat.id]
    except KeyError:
        undefined(bot,update)
    update.message.reply_text(botstring["exportcsv_start"])
    reports = get_reports()
    start="%s%s%s"%(users[update.message.chat.id]["begin_year"],users[update.message.chat.id]["begin_month"],users[update.message.chat.id]["begin_day"])
    end="%s%s%s"%(users[update.message.chat.id]["end_year"],users[update.message.chat.id]["end_month"],users[update.message.chat.id]["end_day"])
    reports_sorted = sort_reports(reports,str(start),str(end))
    if len(reports_sorted)>0:
        update.message.reply_text(botstring["exportcsv_info"]%(len(reports_sorted)))
        json_to_csv(reports_sorted,str(update.message.chat.id))
        update.message.reply_text(botstring["exportcsv"])
        try:
            bot.send_document(chat_id=update.message.chat.id, timeout=360, document=open('%s.csv'%(str(update.message.chat.id)), 'rb'))
            logging.info("The file %s.csv was sent"%(str(update.message.chat.id))) 
            os.remove('%s.csv'%(str(update.message.chat.id)))
        except:
            logging.info("Sending of document not possible")
    else:
        logging.info("For timeframe no reports")
        update.message.reply_text(botstring["exportcsv_no_reports"])


def statistics(bot,update):
    reports = get_reports()
    update.message.reply_text(botstring["statistics"]%(len(reports)))

def help (bot,update):
    update.message.reply_text(botstring["help"])



    

def undefined(bot, update):
    update.message.reply_text(botstring["undefined"])
#   update.message.reply_text(update.message.text.upper())

def main():

    user = {}
    # Create Updater object and attach dispatcher to it
    updater = Updater(telegram_bot_token)
    dispatcher = updater.dispatcher
    logging.info("Bot started")

    # Add command handler to dispatcher
    start_handler = CommandHandler('start',start)
    pdf_handler = CommandHandler('createpdf',createpdf)
    csv_handler = CommandHandler('createcsv',createcsv)
    begin_handler = CommandHandler('begin',begin)
    end_handler = CommandHandler('end',end)
    exportpdf_handler = CommandHandler ('exportpdf', exportpdf)
    exportcsv_handler = CommandHandler ('exportcsv', exportcsv)
    help_handler = CommandHandler('help', help)
    statistics_handler = CommandHandler('statistics', statistics)
    upper_case = MessageHandler(Filters.text, undefined)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(upper_case)
    dispatcher.add_handler(pdf_handler)
    dispatcher.add_handler(csv_handler)
    dispatcher.add_handler(begin_handler)
    dispatcher.add_handler(end_handler)
    dispatcher.add_handler(exportpdf_handler)
    dispatcher.add_handler(exportcsv_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(statistics_handler)



    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()