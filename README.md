# Comon-Voice-Extraction-Data-Collection-South-African-Languages
Collection and extraction of data from South African languages


cv-sentence-extractor is a Rust library typically used in Artificial Intelligence, Natural Language Processing applications
Common Voice is Mozilla's initiative to help teach machines how real people speak. For this we need to collect sentences that people can read out aloud on the website. Individual sentences can be submitted through the Sentence Collector. This only can scale so far, so we also use automated tools to extract sentences from other sources.

Words and sentences were extracted from wikipedai related to the 11 official South African Languages. 
CText NCHLT Web Service is then used to indetify the given language.

# Setup

Clone this repo:
```bash
git clone https://github.com/Common-Voice/cv-sentence-extractor.git
```
Next, download the WikiExtractor:
```bash
git clone https://github.com/attardi/wikiextractor.git
```
# Extraction
Type the following in the terminal and change the XX to the language that it corresponds to. Ex: en for English, af for Afrikaans and ve for Tshivenḓa and so on.
```bash
wget https://dumps.wikimedia.org/XXwiki/latest/XXwiki-latest-pages-articles-multistream.xml.bz2

bzip2 -d XXwiki-latest-pages-articles-multistream.xml.bz2
```

Use WikiExtractor to extract the dump. In the parameters, we specify to use JSON as the output format instead of the default XML.
```bash
cd wikiextractor
git checkout e4abb4cbd019b0257824ee47c23dd163919b731b
python WikiExtractor.py --json ../XXwiki-latest-pages-articles-multistream.xml
```

# Rule Files

After extracting the dump, we need to setup a rules.otml file for the specific language that we are working with.


| Name   |      Description      |  Values | Default |
|--------|-----------------------|---------|---------|
| abbreviation_patterns |  Regex defining abbreviations | Rust Regex Array | all abbreviations allowed
| allowed_symbols_regex |  Regex of allowed symbols or letters. Each character gets matched against this pattern. | String Array | not used
| broken_whitespace |  Array of broken whitespaces. This could for example disallow two spaces following each other | String Array | all types of whitespaces allowed
| disallowed_symbols |  Use `allowed_symbols_regex` instead. Array of disallowed symbols or letters. Only used when allowed_symbols_regex is not set or is an empty String. | String Array | all symbols allowed
| disallowed_words |  Array of disallowed words. Prefer the blocklist approach when possible. | String Array | all words allowed
| even_symbols |  Symbols that always need an even count | Char Array | []
| matching_symbols |  Symbols that map to another | Array of matching configurations: each configuration is an Array of two values: `["match", "match"]`. See example below. | []
| max_word_count |  Maximum number of words in a sentence | integer | 14
| may_end_with_colon |  If a sentence can end with a : or not | boolean | false
| min_characters |  Minimum of character occurrences | integer | 0
| min_trimmed_length |  Minimum length of string after trimming | integer | 3
| min_word_count |  Minimum number of words in a sentence | integer | 1
| needs_letter_start |  If a sentence needs to start with a letter | boolean | true
| needs_punctuation_end |  If a sentence needs to end with a punctuation | boolean | false
| needs_uppercase_start |  If a sentence needs to start with an uppercase | boolean | false
| other_patterns |  Regex to disallow anything else | Rust Regex Array | all other patterns allowed
| quote_start_with_letter |  If a quote needs to start with a letter | boolean | true
| replacements |  Replaces abbreviations or other words according to configuration. This happens before any other rules are checked. | Array of replacement configurations: each configuration is an Array of two values: `["search", "replacement"]`. See example below. | nothing gets replaced
| segmenter |  Segmenter to use for this language. See below for more information. | "python" | using `rust-punkt` by default





Scrape the sentences into a new file from the WikiExtractor output directory:
Were XX, the language code that you are busy working with.

```bash
cd ../cv-sentence-extractor
pip3 install -r requirements.txt # can be skipped if your language doesn't use the Python segmenter
cargo run --release -- extract-wikisource -l XX -d ../wikiextractor/text/ >> wiki.XX.txt
```


Run the cv-sentence-extractor again, but this time, allow all extractions to take place
```bash
cd ../cv-sentence-extractor
cargo run --release -- extract -l XX -d ../wikiextractor/text/ --no_check >> wiki.XX.all.txt
```
Then you can use the cvtools scripts to generate a list of the word frequency:
```bash
cd  ..
git clone https://github.com/dabinat/cvtools/
cd cvtools
python3 ./word_usage.py -i ../cv-sentence-extractor/wiki.XX.all.txt >> word_usage.XX.txt
```

# Data Processing
After all the extractions has taken place, we need to upload the wiki.XX.txt file to CText NCHLT website.
```bash
https://hlt.nwu.ac.za/
```
Select the language that your are working with and the selected techonolgy should be "Language Identifier"

After uploadding and processing the wiki.XX.txt file, the website will give you a "wiki.XX-output.txt" output file.
Next, run the following with all the gathered data and files.

```bash
python3 FilterLanguage.py Language wiki.XX.txt wiki.XX-output.txt
```
Example:

```bash
python3 FilterLanguage.py Tshivenḓa wiki.ve.txt wiki.ve-output.txt
```
This will produce text files containing all the relevent results and Secondary languages indetified during the process.

# Results


| Languages| Total Pages| Total Artical Pages| Sentence Count| Word Count | Character Count (Spaces not included) |
| ---------- | ----------- | -------- | -------- |-------- |-------- |
| SiSwati | 1131 | 587 | 123 | 762 | 6778 |
| Xitsonga |1992| 740 | 203 | 1610  | 8968 |
| Afrikaans |  |  |  |
| English |  |  |  |
| Sesotho | 2882 | 1002 | 177 | 1332 | 7136 |
| isiZulu |  |  |  |
| isiXhosa |  |  |  |
| isiNdebele |  |  |  |
| Sesotho sa Leboa |  |  |  |
| Setswana|  |  |  |
| Tshivenḓa| 1061 | 716 | 79 | 431 | 2553 |







# OPUS

The table below show the amount of sentences that were extracted from each corpra for the different languages that were available within OPUS, after all filtering and applying the 10% copyright rule.

| Languages| CCAligned v1| GNOME v1| XLEnt v1.1| tico-19 v2020-10-28| Tatoeba v2022-03-03| CCMatrix v1| memat v1|KDE4 v2|XhosaNavy v1|QED v2.0a|SPC v1|TED2020 v1| ELRC_2922 v1|OpenSubtitles v2018|
| ---------- | ----------- | -------- | -------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |
| SiSwati | 1131 | 587 | 123 | 762 | 6778 |
| Xitsonga | 2254 |  | 1612 |   | 8968 |
| Afrikaans | 7885 |  |  |
| English |  |  |  |
| Sesotho | 2882 | 1002 | 177 | 1332 | 7136 |
| isiZulu | 3222 |  |  |
| isiXhosa | 2323 | 535 |  | 1610 |  |  | 4585 | 1139 | 2430 |  |
| isiNdebele |  |  |  |
| Sesotho sa Leboa |  |  |  |
| Setswana| 802 |  | 120 |  | 2 |
| Tshivenḓa| 203 | 716 | 79 | 431 | 2553 |


The table below shows the amount of sentences that were extracted from each corpra for the different languages that were available within OPUS, before the 10% copyright rule.


| Languages| CCAligned v1| GNOME v1| XLEnt v1.1| tico-19 v2020-10-28| Tatoeba v2022-03-03| CCMatrix v1| memat v1|KDE4 v2|XhosaNavy v1|QED v2.0a|SPC v1|TED2020 v1| ELRC_2922 v1|OpenSubtitles v2018|
| ---------- | ----------- | -------- | -------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |
| SiSwati | 1131 | 587 | 123 | 762 | 6778 |
| Xitsonga |  |  | 1612 | 1610  | 8968 |
| Afrikaans |  |  |  |
| English |  |  |  |
| Sesotho | 2882 | 1002 | 177 | 1332 | 7136 |
| isiZulu |  |  |  |
| isiXhosa | 24449 | 55628 |  | 16970 |  |  | 48266 | 11991 |  | 25580 |
| isiNdebele |  |  |  |
| Sesotho sa Leboa |  |  |  |
| Setswana| 802 |  | 120 |  | 2 |
| Tshivenḓa| 1061 | 716 | 79 | 431 | 2553 |



# Percentage Overlap Between Different Corpra for each language:

# SiSwati
Corpra | CCAligned v1| GNOME v1|
| ---------- | ----------- | -------- |
| CCAligned v1 |  | 2.3% |
| GNOME v1 | 2.3% |  |


# Xitsonga
Corpra | CCAligned v1 | GNOME v1| QED v2.0a | Tatoeba v2022-03-03 |
| ---------- | ----------- | -------- | -------- | -------- |
| CCAligned v1 |  | 0.94% | 0% | 0% |
| GNOME v1 | 0.94% |  | 0.5% | 0% |
| QED v2.0a | 0% | 0.5% |  | 0% |
| Tatoeba v2022-03-03 | 0% | 0% | 0% |  |


# Afrikaans
Corpra | CCAligned v1 | GNOME v1| QED v2.0a | Tatoeba v2022-03-03 | XLEnt v1.1 | TED2020 v1 | KDE4 v2 | SPC v1 | OpenSubtitles v2018 | ELRC_2922 v1 |
| ---------- | ----------- | -------- | -------- | -------- |-------- |-------- |-------- |-------- ||-------- ||-------- |
| CCAligned v1 |  | 0.4% | 0% | 0% | 2.2% | 0% | 0.8% | 0.2% | 0% | 0% |
| GNOME v1 | 0.4% |  | 0.3% | 0% | 0.9% | 0% | 0.8% | 0.1% | 0% | 0% | 0% | 
| QED v2.0a | 0% | 0.3% |  | 0% | 1% | 0% | 0.7% | 0% | 0% | 0% |
| Tatoeba v2022-03-03 |  0% | 0.9% | 0% |  |  0% | 0% | 0% | 0% | 0% | 0% |
| XLEnt v1.1 | 2.2% | 0% | 1% | 0% | 0%  |  |  |
| TED2020 v1 | 0% | 0.8% | 0% | 0% |
| KDE4 v2 | 0.8% | 0.1% | 0.7% | 0% |
| SPC v1 | 0.2% | 0% | 0% | 0% |
| OpenSubtitles v2018 |  0% | 0% | 0% | 0% |
| ELRC_2922 v1 | 0% | 0% | 0% | 0% |



Corpra | CCAligned v1| GNOME v1| XLEnt v1.1| tico-19 v2020-10-28| Tatoeba v2022-03-03| CCMatrix v1| memat v1|KDE4 v2|XhosaNavy v1|QED v2.0a|SPC v1|TED2020 v1| ELRC_2922 v1|OpenSubtitles v2018|
| ---------- | ----------- | -------- | -------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |-------- |
| CCAligned v1 |
| GNOME v1 |
| XLEnt v1.1 |
| tico-19 v2020-10-28 |
| Tatoeba v2022-03-03 |
| CCMatrix v1 |

