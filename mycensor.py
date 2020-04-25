# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_one(word, text):
  cen_word=""
  for i in word:
    if i==" ":
      cen_word+=" "
    else:
      cen_word+='*'
  return text.replace(word,cen_word)
#print(censor_one("learning algorithms",email_one))

def censor_two(lst,text):
  for i in lst:
    cen_word=""
    for j in i:
      if j==" ":
        cen_word+=" "
      else:
        cen_word+='*'
    text=text.replace(i,cen_word)
  return text
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#print(censor_two(proprietary_terms,email_two))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
def censor_three(n_lst,text):
  text=censor_two(proprietary_terms,text)
  text1=text.split()
  ctr=0
  for i in range(len(text1)):
    if (text1[i] in n_lst)==True:
      new_text=text1[i]
      ctr+=1
      if ctr>2:
        cen_word=""
        for j in new_text:
          cen_word+='*'
        text1[i]=text1[i].replace(new_text,cen_word)
  return " ".join(text1)
#print(censor_three(negative_words, email_three))
punct = [",", "!", "?", ".", "%", "/", "(", ")"]

def cen(word):
  cen_word=""
  for j in word:
    cen_word+="*"
  return cen_word
new_lst=proprietary_terms+negative_words
def censor_four(n_lst,text):
  text2=text.split()
  for i in range(len(text2)):
    for j in punct:
      text2[i]=text2[i].strip(j)
    if text2[i].lower() in n_lst:
      bf=text2[i-1]
      af=text2[i+1]
      word=text2[i]
      bf_cen=cen(text2[i-1])
      text2[i-1]=text2[i-1].replace(bf,bf_cen)
      af_cen=cen(text2[i+1])
      text2[i+1]=text2[i+1].replace(af,af_cen)
      cen_word=cen(text2[i])
      text2[i]=text2[i].replace(word,cen_word)
  return " ".join(text2)
print(censor_four(new_lst, email_four))