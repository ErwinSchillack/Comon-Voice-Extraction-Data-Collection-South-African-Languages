# Comon-Voice-Extraction-Data-Collection-South-African-Languages
Collection and extraction of data from South African languages


cv-sentence-extractor is a Rust library typically used in Artificial Intelligence, Natural Language Processing applications
Common Voice is Mozilla's initiative to help teach machines how real people speak. For this we need to collect sentences that people can read out aloud on the website. Individual sentences can be submitted through the Sentence Collector. This only can scale so far, so we also use automated tools to extract sentences from other sources.

Words and sentences were extracted from wikipedai related to the 11 official South African Languages. 
CText NCHLT Web Service is then used to indetify the given language.

# Setup

Clone this repo:

git clone https://github.com/Common-Voice/cv-sentence-extractor.git

Next, download the WikiExtractor:

git clone https://github.com/attardi/wikiextractor.git

# Extraction
Type the following in the terminal and change the XX to the language that it corresponds to. Ex: en for English, af for Afrikaans and ve for Tshivenḓa and so on.

wget https://dumps.wikimedia.org/XXwiki/latest/XXwiki-latest-pages-articles-multistream.xml.bz2

bzip2 -d XXwiki-latest-pages-articles-multistream.xml.bz2


Use WikiExtractor to extract the dump. In the parameters, we specify to use JSON as the output format instead of the default XML.

cd wikiextractor
git checkout e4abb4cbd019b0257824ee47c23dd163919b731b
python WikiExtractor.py --json ../XXwiki-latest-pages-articles-multistream.xml

After extracting the dump, we need to setup a rules.otml file for the specific language tht we are working with.


# Results


| Artical Pages| Sentence Count| Word Count |Word Count |Word Count |Word Count |Word Count |Word Count |Word Count |Word Count |Word Count |
| ---------- | ----------- | -------- | -------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |
| SeSwati |  |  |  |
| Xitsonga |  | 203 | 1610  |
| Afrikaans |  |  |  |
| English |  |  |  |
| Sesotho | |  |  |
| isiZulu |  |  |  |
| isiXhosa |  |  |  |
| isiNdebele |  |  |  |
| Sesotho sa Leboa |  |  |  |
| Setswana|  |  |  |
| Tshivenḓa|  |  |  |


| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |
