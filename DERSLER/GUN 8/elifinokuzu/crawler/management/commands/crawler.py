from bs4 import BeautifulSoup
import requests
from dictionary.models import Node,Edge
from django.core.management import BaseCommand

class Command(BaseCommand):

    help = 'Crawling data from etimolojiksozluk'

    def __init__(self, *args ,**kwargs):
        super().__init__(*args, **kwargs)
        self.main_url = "https://www.etimolojiturkce.com/kelime/{}"
        self.word = ""

    def add_arguments(self, parser):
        parser.add_argument('word', type=str)

    def origin_crawler(self,word):
        webpage = requests.get(self.main_url.format(word).lower())
        content = webpage.content
        if webpage.status_code == 404:
            return None
        soup = BeautifulSoup(content,"lxml")
        origin_language = soup.find('h2',{"id" : "koken"})
        origin_language = str(origin_language.find_next_sibling('p'))
        first = origin_language.find("<b>")+3
        end = origin_language.find("</b>")
        origin_language = origin_language[first:end]
        self.origin_word(soup)
        return origin_language,self.word

    def origin_word(self,html):
         origin = html.find('span',{"class" : "ety2"}).get_text()
         origin2 = html.find('span',{'class' :"ety4"}).get_text()
         self.word = str(origin)+" "+str(origin2)

    def new_node(self,node_name="null",node_lang="null"):
        n = Node.objects.get_or_create(name=node_name,language=node_lang)[0]
        n.save()

    def new_edge(self,destination,source):
        e = Edge.objects.get_or_create\
                    (
                    source=Node.objects.get(name=source),
                    destination=Node.objects.get(name=destination),
                    type_of_edge= "derives_from",
                    is_directed = True,
                    )[0]
        e.save()

    def handle(self, *args, **options):
        word = options['word']
        try:
            destination,origin = self.origin_crawler(word)
        except TypeError:
            print("404 Not Found.")
            return None
        if origin.startswith("+"):       # when the word dont have a origin.
            print("Skipped",word)
            return None
        self.new_node(word,"tr")
        self.new_node(origin,destination)
        self.new_edge(origin,word)
        print("Added",word)