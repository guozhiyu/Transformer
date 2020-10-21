#!/bin/bash
moses_scripts=/home/s1810409/Context-Aware/runs/iwslt14/de-en/mosesdecoder/scripts
BPEROOT=/home/s1810409/Context-Aware/runs/iwslt14/de-en/subword-nmt/subword_nmt
# zh_segment_home=/idiap/home/lmiculicich/.cache/pip/wheels/ce/32/de/c2be1db5f30804bc7f146ff698c52963f8aa11ba5049811b0d
#kpu_preproc_dir=/fs/zisa0/bhaddow/code/preprocess/build/bin

max_len=200

# export PYTHONPATH=$zh_segment_home

src=zh
tgt=en
prep=prep
tmp=tmp
pair=$src-$tgt
BPE_TOKENS=30000

# Tokenise the English part
# cat corpus.$tgt | \
# $moses_scripts/tokenizer/normalize-punctuation.perl -l $tgt | \
# $moses_scripts/tokenizer/tokenizer.perl -a -l $tgt  \
# > corpus.tok.$tgt

# #Segment the Chinese part
# # python -m jieba -d ' ' < corpus.$src > corpus.tok.$src 

# #
# ###
# #### Clean
# #$moses_scripts/training/clean-corpus-n.perl corpus.tok $src $tgt corpus.clean 1 $max_len corpus.retained
# ###
# #

# #### Train truecaser and truecase
# $moses_scripts/recaser/train-truecaser.perl -model truecase-model.$tgt -corpus corpus.tok.$tgt
# $moses_scripts/recaser/truecase.perl < corpus.tok.$tgt > corpus.tc.$tgt -model truecase-model.$tgt

# ln -s corpus.tok.$src  corpus.tc.$src
#
#  
# dev sets
# for devset in valid test; do
#   for lang  in $src $tgt; do
#     if [ $lang = $tgt ]; then
#       side="src"
#       $moses_scripts/tokenizer/normalize-punctuation.perl -l $lang < $devset.$lang | \
#       $moses_scripts/tokenizer/tokenizer.perl -a -l $lang |  \
#       $moses_scripts/recaser/truecase.perl -model truecase-model.$lang \
#       > $devset.tc.$lang
    
#     fi
    
#   done

# done

TRAIN=$tmp/train.en-de
BPE_CODE=$prep/code
# rm -f $TRAIN
# for l in $src $tgt; do
#     cat $tmp/train.$l >> $TRAIN
# done

echo "learn_bpe.py on ${TRAIN}..."
python $BPEROOT/learn_bpe.py -s $BPE_TOKENS < $tmp/train.en > $prep/code.en
python $BPEROOT/learn_bpe.py -s $BPE_TOKENS < $tmp/train.zh > $prep/code.de

for L in $src $tgt; do
    for f in train.$L valid.$L test.$L; do
        echo "apply_bpe.py to ${f}..."
        python $BPEROOT/apply_bpe.py -c $prep/code.$L < $tmp/$f > $prep/$f
    done
done