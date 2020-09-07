# usage
# python tokenize.py inf outf type
# en: spacy, bert
# zh: character, jieba
import sys
import re

import spacy
from pytorch_pretrained_bert import BertTokenizer
import jieba


nlp = spacy.load("en", disable=['entity'])
BERT_TOKENIZIER = BertTokenizer.from_pretrained('bert-base-multilingual-uncased', do_lower_case=True)
EN_ZH_REGEX = "|".join([r"\w+", r'[\u4e00-\ufaff]', r'[^\s]'])
TOKENIZIER = re.compile(EN_ZH_REGEX, flags=re.ASCII)

def spacy_tokenizier(sent):
    sent = re.sub("\s+", " ", sent.strip())
    doc = nlp(sent)
    
    return " ".join(token.text for token in doc)

def bert_tokenizier(sent):
    return " ".join(BERT_TOKENIZIER.tokenize(sent))


def jieba_toknezier(sent):
    return " ".join(jieba.cut(sent))


def zh_character_tokenzier(sent, subwords=True):
    tokens = []
    if subwords:
        for text in TOKENIZIER.findall(sent):
            if text.isalpha():
                tokens.extend(BERT_TOKENIZIER.tokenize(text))
            else:
                tokens.append(text)
    else:
        for text in TOKENIZIER.findall(sent):
            tokens.append(text)

    return " ".join(tokens)

if __name__ == "__main__":

    tools = {'spacy': spacy_tokenizier, 'bert': bert_tokenizier, 'jieba': jieba_toknezier, 'zh': zh_character_tokenzier}

    infile = sys.argv[1]
    outfile = sys.argv[2]
    token_tool = tools[sys.argv[3]]
    

    with open(infile) as inf, open(outfile, "w") as outf:
        for line in inf:
            print(token_tool(line), file=outf)
            

            
    
    
    


