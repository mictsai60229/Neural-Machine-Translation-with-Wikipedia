## Neural Machine Translation with Wikipedia

### Preprare parallel data

In this work, I used:

* [UM corpus](http://nlp2ct.cis.umac.mo/um-corpus/)
* [News commentary](http://data.statmt.org/news-commentary/v15)

### Tokenize parallel data

Tokenize English sentence and Chinese sentecne
```
cd preprocess/tokenize
```

For English, I used SpaCy.
```
python enzh_tokenize.py [infile] [outfile] spacy
```

For Chinnes, I tokenized sentence into characters.
```
python enzh_tokenize.py [infile] [outfile] zh
```

### Align English and Chinses sentence
I use [fast_align](https://github.com/clab/fast_align) to generate alignment.
Please install fast_align before you continue on the next step.
After installing fast_align, you need to cocat English sentence and Chinsese sentence.
```
a strict lock ##down in the australian city of melbourne has been extended by two weeks , with officials saying new co ##vid - 19 cases had not dropped enough . ||| 澳 大 利 亞 墨 爾 本 的 嚴 格 封 鎖 已 延 長 了 兩 週 ， 官 員 稱 新 的 co ##vid - 19 病 例 還 沒 有 足 夠 減 少 。
```
Run this command to cocat the sentences.
```
TAB=$'\t'
SEPERATOR=$' ||| '
paste [en_file] [zh_file] | sed "s/${TAB}/${SEPERATOR}/g" > [en-zh_file]
```


After generating training data, run the following command to generate alignment
```
cd preprocess/fast_align
./fast_align -i [en-zh_file] -d -o -v > forward.align
```

fast_align produces outputs in the widely-used `i-j` "Pharaoh format," where a pair `i-j` indicates that the ith word (zero-indexed) of the left language (by convention, the source language) is aligned to the jth word of the right sentence (by convention, the target language)
```
0-0 1-1 2-4 3-2 4-3 5-5 6-6
```

## Entity Linking System

I use [End-to-End Neural Entity Linking](https://github.com/dalab/end2end_neural_el) to link entities to Wikipedia.
The entity linking system is created as submodule in `services/entity_linking`

To run the entity linking system
```
cd services/entity_linking/code
python -m gerbil.server --training_name=base_att_global --experiment_name=paper_models   \
           --persons_coreference_merge=True --all_spans_training=True --entity_extension=extension_entities
```







