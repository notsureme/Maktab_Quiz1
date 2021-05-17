import jdatetime

class Open_Date(object):

    def __init__(self, file_name, method):
        self.file = open(file_name, method)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        date1 = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        self.file.write("\nOpened At: "+ str(date1))

        self.file.close()

with Open_Date('text1.txt', 'w') as file:
    file.write('This is a test')



class Nex_date:

    def __init__(self, start_date, end_date, week_day):
        self.start_date = start_date
        self.end_date = end_date
        self.week_day = week_day
        self.file =

    def __next__(self):

