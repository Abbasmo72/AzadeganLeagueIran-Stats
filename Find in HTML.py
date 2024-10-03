from html.parser import HTMLParser

# کلاس جدید برای پردازش HTML
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # وقتی تگ شروع پیدا شد
        print('Encountered a start tag:', tag)
        pos = self.getpos()
        print('At line:', pos[0], 'position', pos[1])
        
        # اگر تگ دارای ویژگی (attribute) باشد، آن‌ها را نمایش می‌دهیم
        if len(attrs) > 0:
            print('Attributes:')
            for a in attrs:
                print('\t', a[0], '=', a[1]) 
    
    def handle_endtag(self, tag):
        # وقتی تگ پایان پیدا شد
        print('Encountered an end tag:', tag)
        pos = self.getpos()
        print('At line:', pos[0], 'position', pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        # وقتی متن پیدا شد
        print('Encountered Text data:', data)
        pos = self.getpos()
        print('At line:', pos[0], 'position', pos[1])

# تابع اصلی
def main():
    # فایل HTML را باز کرده و پردازش می‌کنیم
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # کل محتوا را می‌خوانیم
        parser.feed(contents)

if __name__ == "__main__":
    main()
