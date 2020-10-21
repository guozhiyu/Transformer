import sys, re

a=sys.argv

f_s = open("/home/s1810409/HAN_NMT/zh-en/train.tags.zh-en.en")
f_t = open("/home/s1810409/HAN_NMT/zh-en/train.tags.zh-en.zh")
# f_s_o = open("/home/s1810409/HAN_NMT/zh-en/corpus.en", "w")
# f_t_o = open("/home/s1810409/HAN_NMT/zh-en/corpus.zh", "w")
# f_doc = open("/home/s1810409/HAN_NMT/zh-en/corpus.doc", "w")
# f_s_doc = open("/home/s1810409/HAN_NMT/zh-en/corpus.doc.en", "w")
# f_t_doc = open("/home/s1810409/HAN_NMT/zh-en/corpus.doc.zh", "w")
f_s_o = open("/home/s1810409/HAN_NMT/zh-en/cxt_corpus.en", "w")
f_t_o = open("/home/s1810409/HAN_NMT/zh-en/cxt_corpus.zh", "w")

count = 0
prev=""
for ls, lt in zip(f_s, f_t):
    if ls.startswith("<title>"):
        if not lt.startswith("<title>"): 
            print "error "+str(count)
            break
#         prev=""
        ls = re.sub("(^\<title\>)(.*)(\</title\>)","\g<2>", ls).strip()
        lt = re.sub("(^\<title\>)(.*)(\</title\>)","\g<2>", lt).strip()

        f_s_o.write(ls + "\n")
        f_t_o.write(lt + "\n")
        prev=ls

    elif ls.startswith("<description>"):
        if not lt.startswith("<description>"): 
            print "error "+str(count)
            break
        ls = re.sub("(^\<description\>)(.*)(\</description\>)","\g<2>", ls).strip()
        lt = re.sub("(^\<description\>)(.*)(\</description\>)","\g<2>", lt).strip()
        f_s_o.write("[CLS]"+prev+"[SEP]"+ls +"[SEP]"+ "\n")
        f_t_o.write(lt + "\n")
        prev=ls

    elif not ls.startswith("<"):
        if ls.strip()!= "" and lt.strip()!= "":
            f_s_o.write("[CLS]"+prev+"[SEP]"+ls.strip()+"[SEP]"+ "\n")
            f_t_o.write(lt.strip() + "\n")
            count +=1
            prev=ls.strip()

f_s.close()
f_t.close()
f_s_o.close()
f_t_o.close()
# f_doc.close()
# f_s_doc.close()
# f_t_doc.close()

# prefix='/home/s1810409/HAN_NMT/zh-en/'
# for test in ["dev2010", "tst2010", "tst2011", "tst2012", "tst2013"]:
# 	f_s = open(prefix+"IWSLT15.TED." + test +".zh-en.en.xml")
# 	f_t = open(prefix+"IWSLT15.TED." + test +".zh-en.zh.xml")

# 	count = 0

# 	f_s_o = open(prefix+"IWSLT15.TED." + test +".zh-en.en", "w")
# 	f_t_o = open(prefix+"IWSLT15.TED." + test +".zh-en.zh", "w")
# 	f_doc = open(prefix+"IWSLT15.TED." + test +".zh-en.doc", "w")
# 	f_s_doc = open(prefix+"IWSLT15.TED." + test +".zh-en.doc.en", "w")
# 	f_t_doc = open(prefix+"IWSLT15.TED." + test +".zh-en.doc.zh", "w")

# 	for ls, lt in zip(f_s, f_t):
# 		if ls.startswith("<talkid>"):
# 			if not lt.startswith("<talkid>"): 
# 				print "error "+str(count)
# 				break
# 			s = re.sub("(^\<talkid\>)(.*)(\</talkid\>)","\g<2>", ls).strip()
# 			t = re.sub("(^\<talkid\>)(.*)(\</talkid\>)","\g<2>", lt).strip()

# 			if s!=t:
# 				print "error "+str(count)+" "+test
# 				break

# 			f_s_doc.write(ls.strip() + "\n")
# 			f_t_doc.write(lt.strip() + "\n")
# 			f_doc.write(str(count) + "\n")
			

# 		elif ls.startswith("<seg"): 
# 			if not lt.startswith("<seg"): 
# 				print "error "+str(count)+" "+test
# 				break

# 			ls = re.sub("(^\<seg.*\>)(.*)(\</seg\>)","\g<2>", ls).strip()
# 			lt = re.sub("(^\<seg.*\>)(.*)(\</seg\>)","\g<2>", lt).strip()

# 			if ls.strip()!= "" and lt.strip()!= "":
# 				f_s_o.write(ls + "\n")
# 				f_t_o.write(lt + "\n")
# 				count += 1
# 		else:

# 			f_s_doc.write(ls.strip() + "\n")
# 			f_t_doc.write(lt.strip() + "\n")

# 	f_s.close()
# 	f_t.close()
# 	f_s_o.close()
# 	f_t_o.close()
# 	f_doc.close()
# 	f_s_doc.close()
# 	f_t_doc.close()




		
					
					
