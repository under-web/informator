from Spider import Spider

news = Spider()
bit_fobos = news.get_list_block('https://cryptocurrencytracker.info/ru/fear-and-greed-index',
                    tag1='div', tag2='historical-records',
                    tag3='div', tag4='right')
print(bit_fobos)