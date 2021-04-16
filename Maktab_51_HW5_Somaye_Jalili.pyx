class Book:
    def __init__(self, title, authors, publish_year, number_pages, language, price, status=None, progress=None):
        self.title = title
        self.authors = authors
        self.publish_year = publish_year
        self.number_pages = number_pages
        self.language = language
        self.price = price
        self.status = status
        self.progress = progress

    def read(self,number_page_read):
        """

        :param number_page_read:
        :return:
        """
        if self.number_pages == number_page_read:
            self.progress='100%'
            print('you read book full')
        elif self.number_pages < number_page_read:
            self.progress = (number_page_read / self.number_pages) *100
            print('upper than page number of book')
        elif self.number_pages > number_page_read:
            print('you read :', number_page_read, 'from', self.number_pages, 'and',self.number_pages - number_page_read, 'left')
            self.progress = (number_page_read / self.number_pages) *100
        print(self.progress)
        return number_page_read

    def get_status(self,number_page_read):
        if self.number_pages == number_page_read:
            self.status = "finished"
        elif self.number_pages < number_page_read:
            self.status = "reading"
        elif  number_page_read == 0:
            self.status = "unread"
        return

    def get_data(list_of_info_data):
        list_empty_bookshelf = input('enter title,authors,publish_year,number_pages,language,price of book:').split(',')
        list_empty_bookshelf = [int(x.strip()) if x.isdigit() else x for x in list_empty_bookshelf]
        obj = Book(list_empty_bookshelf[0], list_empty_bookshelf[1], list_empty_bookshelf[2], list_empty_bookshelf[3],
                   list_empty_bookshelf[4], list_empty_bookshelf[5])
        list_of_info_data.append(obj)
        return list_of_info_data

    def __str__(self):
        return f"{self.title} is title"


class Magazin(Book):
    def __init__(self, title, authors, publish_year, number_pages, language, price, issue, status=None, progress=None):
        super().__init__(title, authors, publish_year, number_pages, language, price, status, progress)
        self.issue = issue

    def get_data(self,list_of_info_data):
        list_empty_bookshelf = input('enter title,authors,publish_year,number_pages,language,price,issue of magazin:').split(',')
        list_empty_bookshelf = [int(x.strip()) if x.isdigit() else x for x in list_empty_bookshelf]
        objm = magazin(list_empty_bookshelf[0], list_empty_bookshelf[1], list_empty_bookshelf[2], list_empty_bookshelf[3],
                   list_empty_bookshelf[4], list_empty_bookshelf[5],list_empty_bookshelf[6])
        list_of_info_data.append(objm)
        return list_of_info_data

    def __str__(self):
        return f"{self.title} is title"


class Podcastepisode(Book):
    def __init__(self,title,speaker,publish_year,time,language,price,status=None, progress=None):
        super().__init__(title, publish_year, language, price, status, progress)
        self.speaker = speaker
        self.time = time

    def get_data(self):
        list_empty_bookshelf = input('enter title,speaker,publish_year,time,language,price of podcastepisode:').split(',')
        list_empty_bookshelf = [int(x.strip()) if x.isdigit() else x for x in list_empty_bookshelf]
        objp =  Podcastepisode(list_empty_bookshelf[0], list_empty_bookshelf[1], list_empty_bookshelf[2],list_empty_bookshelf[3],
                       list_empty_bookshelf[4], list_empty_bookshelf[5])
        list_of_info_data.append(objp)
        return

    def read(self,time_of_audio):
        if self.time == time_of_audio:
            print('you listen book full')
        elif self.time < time_of_audio:
            print('upper than listen of book')
        elif self.time > time_of_audio:
            print('you listen :',time_of_audio, 'from',time, 'and', time - time_of_audio,'left')
        return

    def __str__(self):
        return f"{self.title} is title"


class Audiobook(Podcastepisode):
    def __init__(self, title, speaker, authors, publish_year, number_pages, time, book_language, audio_language, price,
                 status=None, progress=None):
        super().__init__(title, speaker, publish_year, authors, language, time, number_pages, price, status, progress)
        self.audio_language = audio_language
        self.book_language = book_language

    def get_data(list_of_info_data):
        list_empty_bookshelf = input('enter title,speaker,authors,publish_year,number_pages,time,book_language,audio_language,price of audiobook:').split(',')
        list_empty_bookshelf = [int(x.strip()) if x.isdigit() else x for x in list_empty_bookshelf]
        list_empty_bookshelf.append(list_empty_bookshelf)
        obja = Audiobook(list_empty_bookshelf[0], list_empty_bookshelf[1], list_empty_bookshelf[2],
                              list_empty_bookshelf[4], list_empty_bookshelf[5], list_empty_bookshelf[6])
        list_of_info_data.append(obja)
        return


    def read(self,time_of_audio):
        if self.time == time_of_audio:
            print('you listen book full')
        elif self.time < time_of_audio:
            print('upper than listen of book')
        elif self.time > time_of_audio:
            print('you listen :', time_of_audio, 'from', self.time, 'and', self.time - time_of_audio, 'left')
        return

    def __str__(self):
        return f"{self.title} is title"

sort_bookshelf=[]
list_empty_bookshelf = []
while True:
    menu = int(input("1-add a book/magazin/podcastepisode/audiobook\n"
          "2-show my bookshelf\n"
          "3-add read page or time listen\n"
          "4-sort my bookshelf\n"
         "5-quit:\n"))
    if menu==1:
        menu2=int(input("1-add  book\n"
              "2-add  magazin \n"
              "3-add  podcastepisode\n"
              "4-add audiobook:\n"))
    elif menu==2:
        for obj in list_empty_bookshelf:
            print(obj)


    elif  menu==3:
        for obj in list_empty_bookshelf:
            number_page_read = int(input('enter number page of read:'))
            obj.get_status(number_page_read)
            obj.read(number_page_read)
    elif menu==5:
        os.exit()

    elif menu==4:
        for i in list_empty_bookshelf:
            sort_bookshelf.append(sorted(i, key=lambda i: i['progres'], reverse=True))
        print(sort_bookshelf)


    if menu2==1:
        Book.get_data(list_empty_bookshelf)
    elif menu2==2:
        Magazin.get_data(list_empty_bookshelf)
    elif menu2==3:
        Podcastepisode.get_data(list_empty_bookshelf)
    elif menu2==4:
        Audiobook.get_data(list_empty_bookshelf)



