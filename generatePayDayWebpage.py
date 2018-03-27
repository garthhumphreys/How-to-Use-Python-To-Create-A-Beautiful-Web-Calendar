#!/usr/bin/python -tt

from PayDayCalendar import PayDayCalendar
from datetime import datetime

"""
    
    @Project:		CIG Payday Calendar
    @Author:		Garth Humphreys
    @Description:	Yearly CIG Payday Calendar
    @Created:		01/18/2013
    @Version:		1.0.1
    @Docs:			www.gov.ky
    
"""

def main():
    # a list of tuples, month then day
    pay_days = [
                    (1,23), # January, 23rd
                    (2,25),
                    (3,26),
                    (4,25),
                    (5,28),
                    (6,25),
                    (7,25),
                    (8,27),
                    (9,25),
                    (10,28),
                    (11,26),
                    (12,18)
                ]
    current_year = datetime.today().year # get from today, the current year
    c = PayDayCalendar(pay_days).formatyearpage(current_year, 4)
    print c

if __name__ == '__main__':
    main()