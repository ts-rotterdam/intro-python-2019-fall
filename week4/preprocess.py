from os import listdir
from os.path import isfile, join
from lxml import etree
import lzma
import pickle

# First we need to get the list of articles
# To do that we need oai-harvest
# https://github.com/bloomonkey/oai-harvest
# After installing run this command in the terminal on the folder you want to
# save the dataset, and change the path below
# The action below takes a few hours at least, if this is interrupted, you can
# limit the start date so you don't fetch everything again
# oai-harvest --set "cs" http://export.arxiv.org/oai2

input_path = "/the/path/where/the/files/are"
summaries_path = "data/arxiv_cs_summaries.pickle.xz"
descriptions_path = "data/arxiv_cs_descriptions.pickle.xz"

# Generate a list of files to be used later generate the dataset
files = [f for f in listdir(input_path) if isfile(join(input_path, f))]
with open("files.pickle", "wb") as f:
    pickle.dump(files, f)

# Load the list of files
files = pickle.load(open("files.pickle", "rb"))

summaries = []
descriptions = []

ss = [
    "Computer Science - Artificial Intelligence",
    "Computer Science - Computer Vision and Pattern Recognition",
    "Computer Science - Machine Learning",
]

for f in files:
    el = etree.parse(join(input_path, f))

    if not [s for s in el.xpath("//*[name()='dc:subject']/text()") if s in ss]:
        continue

    title = el.xpath("//*[name()='dc:title']/text()")[0].replace("\n", "")
    authors = el.xpath("//*[name()='dc:creator']/text()")
    year = int(el.xpath("substring(//*[name()='dc:date'][last()]/text(), 0, 5)"))
    ref = [
        r
        for r in el.xpath("//*[name()='dc:identifier']/text()")
        if r.startswith("http://arxiv.org")
    ][0]
    summaries.append((title, authors, year, ref))
    descriptions.append(
        el.xpath("//*[name()='dc:description']/text()")[0].replace("\n", " ").strip()
    )


with lzma.open(summaries_path, "wb") as f:
    pickle.dump(summaries, f)

with lzma.open(descriptions_path, "wb") as f:
    pickle.dump(descriptions, f)
