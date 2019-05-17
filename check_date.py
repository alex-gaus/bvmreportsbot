def check_date(date):
                        date_list = date.split("-")
                        try:
                            if int(date_list[0]) > 1900 and int(date_list[0])<2100:
                                year = str(date_list[0])
                            else: return False
                            if int(date_list[1]) > 0 and int(date_list[1])<13:
                                month = str(date_list[1])
                            else: return False
                            if int(date_list[2]) > 0 and int(date_list[2])<32:
                                day = str(date_list[2])
                            else: return False
                            return {
                                "year": year,
                                "month": month,
                                "day": day}
                        except:
                            return False
                            
def check_date_logic(date):
    start="%s%s%s"%(date["begin_year"],date["begin_month"],date["begin_day"])
    end="%s%s%s"%(date["end_year"],date["end_month"],date["end_day"])
    if int(start)<int(end):
        return True
    else:
        return False