class MyDate:

    # Date 요소
    MONTH = [x for x in range(13)]
    MONTH_30 = [4, 6, 9, 11]
    DAY_31 = [x for x in range(32)]
    DAY_30 = [x for x in range(31)]
    DAY_29 = [x for x in range(30)]
    DAY_28 = [x for x in range(29)]
    HOUR = [x for x in range(24)]
    MINUTE = [x for x in range(60)]
    SECOND = [x for x in range(60)]
    
    @classmethod
    def day_check(year, month, day):
        # 월 유효성 check
        if month not in MyDate.MONTH:
            raise ValueError("Month must be between 1 and 12.")
        
        # 월별 일자 check
        ## 2월일때
        if month == 2:
            # 윤년일떄
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if day not in MyDate.DAY_29:
                    raise ValueError("February in leap years only has 29 days.")
            # 윤년이 아닐때
            else: 
                if day not in MyDate.DAY_28:
                    raise ValueError("February only has 28 days.")
        ## 30일까지 있는 월일때
        elif month in MyDate.MONTH_30:
                if day not in MyDate.DAY_30:
                    raise ValueError("The month you entered only has 30 days.")
        ## 31일까지 있는 월일떄
        else:
            if day not in MyDate.DAY_31:
                raise ValueError("The month you entered only has 31 days.")
    
    def __init__(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, sec = 0):
        
        if year < 0:
            raise ValueError("Please enter only positive numbers for the year.")
        
        if month != 0:
            MyDate.day_check(year, month, day)
                
        if hour not in MyDate.HOUR:
            raise ValueError("Hour must be between 0 and 23.")
            
        if minute not in MyDate.MINUTE:
            raise ValueError("Minute must be between 0 and 59.")
        
        if sec not in MyDate.SECOND:
            raise ValueError("Second must be between 0 and 59.")
        
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.sec = sec
        
    def __add__(self, other):
        new_second = self.sec + other.sec
        new_minute = self.minute + other.minute
        new_hour = self.hour + other.hour
        new_day = self.day + other.day
        new_month = self.month + other.month
        new_year = self.year + other.year
        
        new_second = new_second % 60
        new_minute = (new_minute + (new_second // 60)) % 60
        new_hour = (new_hour + (new_minute // 60)) % 24
        
        if new_day == 
        new_day = (new_day + (new_hour // 24)) % ?
        new_month = (new_month + (new_day // 24))
        
        new_year = (new_year + (new_month // 12)) % 12
        
        return MyDate(new_year, new_month, new_day, new_hour, new_minute, new_second)

    def __sub__(self, other):
        pass 

    def __eq__(self, other):
        pass 

    # d1 < d2 less than
    def __lt__(self, other):
        pass 
    
    # less equl
    def __le__(self, other):
        pass 
    
    def __gt__(self, other):
        pass 

    def __ge__(self, other):
        pass 

if __name__ == '__main__':
    d0 = MyDate()
    d1 = MyDate(2022, 4, 1, 14, 30)
    # d2 = MyDate(2024, 8, 100, 23, 10) # should raise an error 
    # d3 = MyDate(2024, 2, 30)

    d3 = MyDate(day = 1)
    
    assert d1 + d3 == MyDate(2022, 4, 2, 14, 30)
        
    # assert d1 - d3 == MyDate(2022, 3, 31, 14, 30) 

    # assert d1 < d2 