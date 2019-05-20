from goose3 import Goose
import urllib.request
import lxml.html
import codecs
import os
from pymarkovchain import MarkovChain

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
    
def get_links(url, domain):
    """ Fetching urls """
 opener = AppURLopener()
 connection = opener.open(url)
 dom = lxml.html.fromstring(connection.read())
 for link in dom.xpath('//a/@href'):
 	if ( link.startswith("speech") and link.endswith("htm") ):
 		yield domain + link
        
        
def get_text(url):
 g = Goose() 
 article = g.extract(url=url)
 with codecs.open(article.link_hash + ".speech", "w", "utf-8-sig") as text_file:
 		text_file.write(article.cleaned_text)
if (__name__ == "__main__"):
 link = "http://www.americanrhetoric.com/barackobamaspeeches.htm"
 domain = "http://www.americanrhetoric.com/"
 for i in get_links(link, domain):
 	get_text(i)

for file in os.listdir("."):
 if file.endswith(".speech"):
 	os.system("cat "+ file + " >> all.speeches") # Saved all the texts from the sppeches to a file(all.sppeches)

with codecs.open("all.speeches", "r", "utf-8-sig") as text_file:
 r = text_file.read()
 tokenizer = RegexpTokenizer(r'\w+')
 _tokens = tokenizer.tokenize(r)
 tokens = [t for t in _tokens if t.lower() not in english_stopwords]

# Process lexical diversity
st = len(set(tokens))
lt = len(tokens)
y = [st*100/lt]
print(y)
fig = plt.figure()
ax = fig.add_subplot(111)
N = 1
ind = np.arange(N)
width = 0.7
rect = ax.bar(ind, y, width, color='black') 
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,100)
ax.set_ylabel('Score')
ax.set_title('Lexical Diversity')
xTickMarks = ['Lexical Diversity Meter']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)
ax.legend( (rect[0], ('') ))
plt.show()

# POS Tagging
tagged = nltk.pos_tag(tokens)

counts = Counter(tag for word,tag in tagged)
# counter data, counter is your counter object
keys = counts.keys()
y_pos = np.arange(len(keys))
# get the counts for each key
p = [counts[k] for k in keys]
error = np.random.rand(len(keys))

# Top 60 words
dist = nltk.FreqDist(tokens)
dist.plot(60, cumulative=False)

text = nltk.Text(_tokens)
collocation = text.collocations(num=60)

# Chuncking
nouns = [chunk for chunk in ne_chunk(tagged) if isinstance(chunk, Tree)]
persons = []
locations = []
organizations = []
dates = []
times = []
percents = []
facilities = []
gpes = []
for tree in nouns:
 if tree.label() == "PERSON": 
 	person = ' '.join(c[0] for c in tree.leaves())
 	persons.append(person)
 if tree.label() == "LOCATION": 
 	location = ' '.join(c[0] for c in tree.leaves())
 	locations.append(location)
 if tree.label() == "ORGANIZATION": 
 	organization = ' '.join(c[0] for c in tree.leaves())
 	organizations.append(organization)
 if tree.label() == "DATE": 
 	date = ' '.join(c[0] for c in tree.leaves())
 	dates.append(date)
 if tree.label() == "TIME": 
 	time = ' '.join(c[0] for c in tree.leaves())
 	timess.append(time)
 if tree.label() == "PERCENT": 
 	percent = ' '.join(c[0] for c in tree.leaves())
 	percents.append(percent)
 if tree.label() == "FACILITY": 
 	facility = ' '.join(c[0] for c in tree.leaves())
 	facilities.append(facility)
 if tree.label() == "GPE": 
 	gpe = ' '.join(c[0] for c in tree.leaves())
 	gpes.append(gpe)


 mc = MarkovChain()
 for i in range(1,20):
 	mc.generateDatabase(r)
 	g = mc.generateString()
 	print(g)
