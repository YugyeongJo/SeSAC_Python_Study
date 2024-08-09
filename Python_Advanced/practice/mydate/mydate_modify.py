class MyDate: 
    @staticmethod
    def day_check(year, month):
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31 
        
    # Date 요소
    MONTH = [x for x in range(1, 13)]
    HOUR = [x for x in range(24)]
    MINUTE = [x for x in range(60)]
    SECOND = [x for x in range(60)]
    table = {0:lambda lst:12, 1:lambda lst: MyDate.day_check(lst[0], lst[1]), 2:lambda lst: 24, 3:lambda lst: 60, 4:lambda lst: 60}
    
    def __init__(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, sec = 0):
        
        if year < 0:
            raise ValueError("Please enter only positive numbers for the year.")
        
        if month != 0:
            if month not in MyDate.MONTH:
                raise ValueError("Month must be between 1 and 12.")
            max_days = MyDate.day_check(year, month)
            if day < 1 or day > max_days:
                raise ValueError(f"The month you entered only has {max_days} days.")
                
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
        
        self.args = (year, month, day, hour, minute, sec)
        
    def __add__(self, other):
        
        new_second = self.sec + other.sec
        new_second %= 60
        plus_minute = new_second // 60
        
        new_minute = self.minute + other.minute + plus_minute
        new_minute %= 60
        plus_hour = new_second // 60
        
        new_hour = self.hour + other.hour + plus_hour
        new_hour %= 24
        plus_day = new_hour // 24
        
        new_day = self.day + other.day + plus_day
        new_month = self.month
        new_year = self.year
        
        while new_day > MyDate.day_check(new_year, new_month):
            new_day -= MyDate.day_check(new_year, new_month)
            new_month += 1
            if new_month > 12:
                new_month -= 12
                new_year += 1
        
        new_month += other.month
        new_month %= 12
        plus_year = new_month // 12
        
        new_year += plus_year
        
        return MyDate(new_year, new_month, new_day, new_hour, new_minute, new_second)

    def __sub__(self, other):
        r = [
            self.year - other.year
            , self.month - other.month
            , self.day - other.day
            , self.hour - other.hour
            , self.minute - other.minute
            , self.sec - other.sec
        ]
        
        res = []
        flag = False 
        for e in r[::-1]:
            
            if e != 0:
                res.append(e)
                flag = True 
            
            elif flag:
                res.append(e)
        res = res[::-1]
            
        # 작은거에서 큰거 빼면 에러
        cmp = [a-b for a, b in zip(self.args, other.args)]
        for idx, e in enumerate(cmp):
            if e > 0:
                break
            
            if idx == 0 or idx > 2:
                if e < 0:
                    raise ValueError("Unable to execute")
            else: 
                if e <= 0:
                    raise ValueError("Unable to execute")
            
        for idx, elem in enumerate(res[1::-1]):
            idx = len(res)-idx-1
            cur_max = MyDate.table[idx-1](res)
            print('before', idx, cur_max, res)
            if idx == 0 or idx > 2:
                while res[idx] < 0:
                    res[idx] = cur_max+res[idx]
                    res[idx-1] -= 1
                    cur_max = MyDate.table[idx-1](res)
            else:
                while res[idx] <= 0:
                    res[idx] = cur_max+res[idx]
                    res[idx-1] -= 1
                    cur_max = MyDate.table[idx-1](res)
            print('after', idx, cur_max, res)
        return MyDate(*res)   

    def __eq__(self, other):
        return (self.year == other.year \
                and self.month == other.month \
                and self.day == other.day \
                and self.hour == other.hour \
                and self.minute == other.minute \
                and self.sec == other.sec)

    # d1 < d2 less than
    def __lt__(self, other):
        for a, b in zip(self.args, other.args):
            if a < b:
                return True 
            elif a > b:
                return False 
                
        return False 
    
    # less equl
    def __le__(self, other):
        return self < other or self == other 
    
    # greater than
    def __gt__(self, other):
        return not self < other and not self == other 

    # greater equl
    def __ge__(self, other):
        return self > other or self == other 

    def __str__(self):
        return f'{self.year}/{self.month}/{self.day} {self.hour}:{self.minute}:{self.sec}'

if __name__ == '__main__':
    # d0 = MyDate()
    # d1 = MyDate(2022, 4, 1, 14, 30)
    # d2 = MyDate(2024, 8, 100, 23, 10) # should raise an error 
    # d3 = MyDate(2024, 2, 30)

    # d3 = MyDate(day = 1)
    # assert d1 + d3 == MyDate(2022, 4, 2, 14, 30)
    
    d4 = MyDate(2022, 1, 1)
    MyDate.__init__(d4, 2022, 1, 1)
    d5 = MyDate(day = 2)

    # print(d4 + d5)
    # assert d4 + d5 == MyDate(2022, 4, 1)

    # print(d1 - d3)
    print(d4 - d5)
    assert d4 - d5 == MyDate(2021, 12, 30) 
    [2022, 1, -1]

    # assert d1 < d2 