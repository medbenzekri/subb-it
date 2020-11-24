import pysubs2
from googletrans import Translator
def translatorf(uploaded_file):
	translator = Translator(to_lang='ar')
	subs= pysubs2.load(uploaded_file, encoding="utf-8")
	for line in subs :
		if line.text.find("{") == -1   :
			if line.text.find(r"\N")== -1 :
			    line.text = translator.translate(line.text,src='',dest='ar').text
			else:
				pos= line.text.find(r"\N")
				line.text = translator.translate(line.text[:pos-1],src='',dest='ar').text + r"\N"+ translator.translate(line.text[pos+1:],src='',dest='ar').text
		else :
		    pos = line.text.find("}")
		    line.text = translator.translate(line.text[pos+1:],src='',dest='ar').text
    
	# translator = Translator()
	# subs= pysubs2.load(uploaded_file, encoding="utf-8")
	# for line in subs :
	# 	if line.text.find("{") == -1   :
	# 		if line.text.find(r"\N")== -1 :
	# 		    line.text = translator.translate(line.text,dest='ar').text
	# 		else:
	# 			pos= line.text.find(r"\N")
	# 			line.text = translator.translate(line.text[:pos-1],dest='ar').text + r"\N"+ translator.translate(line.text[pos+1:],dest='ar').text
	# 	else :
	# 	    pos = line.text.find("}")
	# 	    line.text = translator.translate(line.text[pos+1:],dest='ar').text
    

	return subs.save(uploaded_file)




