from django.core.management.base import BaseCommand, CommandError
from web.models import Page,Event,SuccessStory,Job,Employer
from brightnetwork.settings_dev import ML_FILES
import pandas as pd
import io
import codecs
import unidecode
import unicodedata
import re
from gensim.models import Word2Vec


class Command(BaseCommand):
    help = 'Collect all contents in the website'
    path=ML_FILES+"stopwords"
    corpus_path=ML_FILES+"corpus.txt"
    model_path = ML_FILES + "model.bin"
    applications_path = ML_FILES + "job_applications.csv"

    def handle(self, *args, **options):
        all_data=self.collect(Page,Event,SuccessStory,Job,Employer)
        all_data = [i for i in all_data if len(i) > 4]
        documents = self.remove_stopwords(all_data, self.path)
        print("stopwords done")
        sentences = self.get_data_word2vec(documents)
        self.create_corpus_file(self.corpus_path, sentences)
        print("Corpus done")
        model=self.get_Word2vec_model(self.model_path, sentences)

    def get_Word2vec_model(self,model_path,sentences):
        model = Word2Vec(sentences, min_count=5, size=350,
                         window=5,
                         workers=10)
        model.train(sentences, total_examples=len(sentences), epochs=100)
        model.save(model_path)
        return model

    def remove_pages(self, content):
        res=True
        if len(content)<10:
            res=False
        return res

    def strip_accents(self,text):
        """
        Strip accents from input String.

        :param text: The input string.
        :type text: String.

        :returns: The processed String.
        :rtype: String.
        """
        try:
            text = unicode(text, 'utf-8')
        except (TypeError, NameError):  # unicode is a default on python 3
            pass
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)


    def clean_page(self, title, content):
        content=content.replace("&bull;","\r\n ").replace("bull;","\r\n ").replace("\r\r\n\t"," ").replace("\r\r\n"," ")
        content=content.replace(".","\r\n ").replace(":","").replace("&lsquo;","").replace("lsquo;","")
        content=content.replace("\r\r\n\r\r\n"," ").replace("..."," ").replace("&#39;s","").replace("#39;s","")
        content=content.replace("&nbsp;"," ").replace("nbsp;"," ").replace("&#39;","").replace("#39;","")
        content=content.replace("amp;","").replace("&middot;","").replace("middot;","")
        content=content.replace(",","").replace("?","\r\n ").replace("!","\r\n ").replace("  "," ")
        content=content.replace("&rsquo;"," ").replace("rsquo;"," ").replace("\t"," ")
        content=content.replace("\r\n\r\n","\r\n ").replace(" \r\n ","\r\n ").replace("\r\n \r\n","\r\n")
        content=content.replace("&ndash;"," ").replace("ndash;"," ").replace("&pound;","").replace("pound;","")
        content=content.replace("  ","").replace("   ","").replace("  ","").replace("   ","")
        content=content.replace("(","").replace(")","").replace(" - "," ").replace(" / "," ").replace("/"," ").replace("   ","")
        content=re.sub('<.*?>',"",content , flags=re.DOTALL)
        res=title.replace("?","").replace("!","").replace(".","")+"\r\n "+content
        res=res.replace("\r\n\r\n","").replace(" \r\n "," ").replace("&eacute;","e")
        res=res.replace("&ldquo;","").replace("ldquo;","").replace("&rdquo;","").replace("rdquo;","")
        res=''.join([i for i in res if not i.isdigit()])
        return res

    def clean_job(self, title, content):
        content=content.replace("&bull;","\r\n ").replace("bull;","\r\n ").replace("\r\r\n\t"," ").replace("\r\r\n"," ")
        content=content.replace(".","\r\n ").replace(":","").replace("&lsquo;","").replace("lsquo;","")
        content=content.replace("\r\r\n\r\r\n"," ").replace("..."," ").replace("&#39;s","").replace("#39;s","")
        content=content.replace("&nbsp;"," ").replace("nbsp;"," ").replace("&#39;","").replace("#39;","")
        content=content.replace("amp;","").replace("&middot;","").replace("middot;","")
        content=content.replace(",","").replace("?","\r\n ").replace("!","\r\n ").replace("  "," ")
        content=content.replace("&rsquo;"," ").replace("rsquo;"," ").replace("\t"," ")
        content=content.replace("\r\n\r\n","\r\n ").replace(" \r\n ","\r\n ").replace("\r\n \r\n","\r\n")
        content=content.replace("&ndash;"," ").replace("ndash;"," ").replace("&pound;","").replace("pound;","")
        content=content.replace("  ","").replace("   ","").replace("  ","").replace("   ","")
        content=content.replace("(","").replace(")","").replace(" - "," ").replace(" / "," ").replace("/"," ").replace("   ","")
        content=re.sub('<.*?>',"",content , flags=re.DOTALL)
        res=title.replace("?","").replace("!","").replace(".","")+"\r\n "+content
        res=res.replace("\r\n\r\n","").replace(" \r\n "," ").replace("&eacute;","e")
        res=res.replace("&ldquo;","").replace("ldquo;","").replace("&rdquo;","").replace("rdquo;","")
        res=''.join([i for i in res if not i.isdigit()])
        return res

    def clean_story(self, title, content):
        try:
            content=content.replace("&bull;","\r\n ").replace("bull;","\r\n ").replace("\r\r\n\t"," ").replace("\r\r\n"," ")
            content=content.replace(".","\r\n ").replace(":","").replace("&lsquo;","").replace("lsquo;","")
            content=content.replace("\r\r\n\r\r\n"," ").replace("..."," ").replace("&#39;s","").replace("#39;s","")
            content=content.replace("&nbsp;"," ").replace("nbsp;"," ").replace("&#39;","").replace("#39;","")
            content=content.replace("amp;","").replace("&middot;","").replace("middot;","")
            content=content.replace(",","").replace("?","\r\n ").replace("!","\r\n ").replace("  "," ")
            content=content.replace("&rsquo;"," ").replace("rsquo;"," ").replace("\t"," ")
            content=content.replace("\r\n\r\n","\r\n ").replace(" \r\n ","\r\n ").replace("\r\n \r\n","\r\n")
            content=content.replace("&ndash;"," ").replace("ndash;"," ").replace("&pound;","").replace("pound;","")
            content=content.replace("  ","").replace("   ","").replace("  ","").replace("   ","")
            content=content.replace("(","").replace(")","").replace(" - "," ").replace(" / "," ").replace("/"," ").replace("   ","")
            content=re.sub('<.*?>',"",content , flags=re.DOTALL)
            res=title.replace("?","").replace("!","").replace(".","")+"\r\n "+content
            res=res.replace("\r\n\r\n","").replace(" \r\n "," ").replace("&eacute;","e")
            res=res.replace("&ldquo;","").replace("ldquo;","").replace("&rdquo;","").replace("rdquo;","")
            res=''.join([i for i in res if not i.isdigit()])
        except:
            res=""
        return res

    def clean_event(self, title, content):
        try:
            content=content.replace("&bull;","\r\n ").replace("bull;","\r\n ").replace("\r\r\n\t"," ").replace("\r\r\n"," ")
            content=content.replace(".","\r\n ").replace(":","").replace("&lsquo;","").replace("lsquo;","")
            content=content.replace("\r\r\n\r\r\n"," ").replace("..."," ").replace("&#39;s","").replace("#39;s","")
            content=content.replace("&nbsp;"," ").replace("nbsp;"," ").replace("&#39;","").replace("#39;","")
            content=content.replace("amp;","").replace("&middot;","").replace("middot;","")
            content=content.replace(",","").replace("?","\r\n ").replace("!","\r\n ").replace("  "," ")
            content=content.replace("&rsquo;"," ").replace("rsquo;"," ").replace("\t"," ")
            content=content.replace("\r\n\r\n","\r\n ").replace(" \r\n ","\r\n ").replace("\r\n \r\n","\r\n")
            content=content.replace("&ndash;"," ").replace("ndash;"," ").replace("&pound;","").replace("pound;","")
            content=content.replace("  ","").replace("   ","").replace("  ","").replace("   ","")
            content=content.replace("(","").replace(")","").replace(" - "," ").replace(" / "," ").replace("/"," ").replace("   ","")
            content=re.sub('<.*?>',"",content , flags=re.DOTALL)
            res=title.replace("?","").replace("!","").replace(".","")+"\r\n "+content
            res=res.replace("\r\n\r\n","").replace(" \r\n "," ").replace("&eacute;","e")
            res=res.replace("&ldquo;","").replace("ldquo;","").replace("&rdquo;","").replace("rdquo;","")
            res=''.join([i for i in res if not i.isdigit()])
        except:
            res=""
        return res

    def clean_employer(self,title, content, sector):
        try:
            content = content.replace("&bull;", "\r\n ").replace("bull;", "\r\n ").replace("\r\r\n\t", " ").replace(
                "\r\r\n", " ")
            content = content.replace(".", "\r\n ").replace(":", "").replace("&lsquo;", "").replace("lsquo;", "")
            content = content.replace("\r\r\n\r\r\n", " ").replace("...", " ").replace("&#39;s", "").replace("#39;s",
                                                                                                             "")
            content = content.replace("&nbsp;", " ").replace("nbsp;", " ").replace("&#39;", "").replace("#39;", "")
            content = content.replace("amp;", "").replace("&middot;", "").replace("middot;", "")
            content = content.replace(",", "").replace("?", "\r\n ").replace("!", "\r\n ").replace("  ", " ")
            content = content.replace("&rsquo;", " ").replace("rsquo;", " ").replace("\t", " ")
            content = content.replace("\r\n\r\n", "\r\n ").replace(" \r\n ", "\r\n ").replace("\r\n \r\n", "\r\n")
            content = content.replace("&ndash;", " ").replace("ndash;", " ").replace("&pound;", "").replace("pound;",
                                                                                                            "")
            content = content.replace("  ", "").replace("   ", "").replace("  ", "").replace("   ", "")
            content = content.replace("(", "").replace(")", "").replace(" - ", " ").replace(" / ", " ").replace("/",
                                                                                                                " ").replace(
                "   ", "")
            content = re.sub('<.*?>', "", content, flags=re.DOTALL)
            res = title.replace("?", "").replace("!", "").replace(".", "") + "\r\n " + sector + "\r\n " + content
            res = res.replace("\r\n\r\n", "").replace(" \r\n ", " ").replace("&eacute;", "e")
            res = res.replace("&ldquo;", "").replace("ldquo;", "").replace("&rdquo;", "").replace("rdquo;", "")
            res = ''.join([i for i in res if not i.isdigit()])
        except:
            res = ""
        return res


    def collect(self,Page,Event,SuccessStory,Job,Employer):
        events = Event.objects.all()
        pages = Page.objects.all()
        stories=SuccessStory.objects.all()
        jobs=Job.objects.all()
        employers = Employer.objects.all()
        page_content=[]
        job_description=[]
        employer_description=[]
        stories_content=[]
        events_content=[]
        for page in pages:
            content=page.content
            page_title=page.title_part1+" "+page.title_part2
            page_content.append(self.clean_page(page_title, content))
        page_content = [i for i in page_content if self.remove_pages(i)]
        print("Page done")
        for job in jobs:
            title=job.title
            content=job.description
            job_description.append(self.clean_job(title,content))
        print("Job done")
        for employer in employers:
            title=employer.title
            content=employer.description
            employer_sectors = []
            for sector in employer.sectors.all():
                employer_sectors.append(sector.title)
            employer_sector_title = ""
            for i in employer_sectors:
                employer_sector_title += i + " "
            employer_description.append(self.clean_employer(title,content,employer_sector_title))
        print("Employer done")
        university_name, degree_subject_name=self.load_uni(self.applications_path)
        uni_data = [self.clean_uni(university_name[i], degree_subject_name[i]) for i in range(len(university_name))]
        uni_data = [i for i in uni_data if self.remove_pages(i)]
        uni_data = list(set(uni_data))
        print("Uni done")
        for story in stories:
            title=story.title_part2
            content=story.content
            stories_content.append(self.clean_story(title,content))
        print("Stories done")
        for event in events:
            title=event.title
            content=event.description
            events_content.append(self.clean_event(title, content))
        print("events done")
        all_data=page_content+job_description+stories_content+events_content+employer_description+uni_data
        return all_data

    def load_uni(self,path):
        d=pd.read_csv(path)
        university_name = d['university_name'].values
        degree_subject_name = d["degree_subject"].values
        return university_name,degree_subject_name

    def clean_uni(self,uni_name, degree_name):
        try:
            content = uni_name + " " + degree_name
        except:
            content = uni_name
        try:
            content = content.replace(".", "\r\n ").replace(":", "").replace("&lsquo;", "").replace("lsquo;", "")
            content = content.replace("\r\r\n\r\r\n", " ").replace("...", " ").replace("&#39;s", "").replace("#39;s",
                                                                                                             "")
            content = content.replace("&nbsp;", " ").replace("nbsp;", " ").replace("&#39;", "").replace("#39;", "")
            content = content.replace("amp;", "").replace("&middot;", "").replace("middot;", "")
            content = content.replace(",", "").replace("?", "\r\n ").replace("!", "\r\n ").replace("  ", " ")
            content = content.replace("&rsquo;", " ").replace("rsquo;", " ").replace("\t", " ")
            content = content.replace("\r\n\r\n", "\r\n ").replace(" \r\n ", "\r\n ").replace("\r\n \r\n", "\r\n")
            content = content.replace("&ndash;", " ").replace("ndash;", " ").replace("&pound;", "").replace("pound;",
                                                                                                            "")
            content = content.replace("  ", "").replace("   ", "").replace("  ", "").replace("   ", "")
            content = content.replace("(", "").replace(")", "").replace(" - ", " ").replace(" / ", " ").replace("/",
                                                                                                                " ").replace(
                "   ", "")
            res = content + "\r\n "
            res = ''.join([i for i in res if not i.isdigit()])
        except:
            res = ""
        return res

    def remove_stopwords(self, x,path):
        res=[]
        with open(path) as stopfile:
            stopwords = stopfile.read()
            stop = stopwords.split()
        for i,document in enumerate(x):
            sentences=document.split("\r\n")
            if len(sentences)>1:
                new_sentences=[]
                for sentence in sentences:
                    words=sentence.split(" ")
                    try:
                        lk=''
                        while True:
                            words.remove(lk)
                    except:
                        pass
                    if len(words)>1:
                        new_words=[]
                        for word in words:
                            word=word.lower()
                            if word not in stop:
                                new_words.append(word)
                        a=""
                        for l,k in enumerate(new_words):
                            if l<len(new_words):
                                a+=k+" "
                            else:
                                a+=k
                        a+="\r\n "
                        new_sentences.append(a)
            b=""
            for k in new_sentences:
                b+=k
            res.append(b)
        return res

    def get_data_word2vec(self,x):
        res=[]
        for document in x:
            sentences=document.split("\r\n")
            for sentence in sentences:
                if len(sentence)>1:
                    sentence=sentence.replace("&pound;","").replace("We;re","").replace(";"," ")
                    sentence=sentence.replace("We;ll","").replace(":"," ").replace("&quot;","")
                    sentence = ''.join([i for i in sentence if not i.isdigit()])
                    a=sentence.split(" ")
                    try:
                        lk=''
                        while True:
                            a.remove(lk)
                    except:
                        pass
                    res.append(a)
        return res

    def create_corpus_file(self,path, x):
        f = codecs.open(path, "w", "utf-8")
        #with io.open(path, mode='w', encoding='utf-8') as f:
        for item in x:
            a=""
            for i in item:
                a+=i+" "
            a+="\n"
            try:
                f.write(a)
            except:
                # remove accents
                unaccented_string = self.strip_accents(a)
                f.write(unaccented_string)
        f.close()

#model = Word2Vec.load("model.bin")
#model.wv.most_similar