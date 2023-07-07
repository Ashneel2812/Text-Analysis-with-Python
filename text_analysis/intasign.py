import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
import string
import re
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stpwrd = nltk.corpus.stopwords.words('english')

#nltk.download('punkt')

my_file1 = open("StopWords_Auditor.txt", "r")
data1 = my_file1.read()
data_into_list1 = data1.replace('\n', ' ').split(" ")
#print(data_into_list1)
my_file1.close()


#In the file StopWords_currencies.txt , remove the country name and only keep the currency . This can be done using MS Excel.
'''my_file2 = open("UpdatedStopWords_currencies.txt",mode="r")
data2 = my_file2.read()
data_into_list2 = data2.replace('\n', ' ').split(" ")
#print(data_into_list2)
my_file2.close()'''

my_file3 = open("StopWords_DatesandNumbers.txt", "r")
data3 = my_file3.read()
data_into_list3 = data3.replace('|',' ').replace('Denominations',' ').replace('Time',' ').replace('Calendar',' ').replace('Numbers',' ').replace('Roman',' ').replace('related',' ').replace('numerals',' ').replace('\n', ' ').split(" ")
#print(data_into_list3)
my_file3.close()

my_file4 = open("StopWords_Generic.txt", "r")
data4 = my_file4.read()
data_into_list4 = data4.replace('\n', ' ').split(" ")
#print(data_into_list4)
my_file4.close()

my_file5 = open("StopWords_GenericLong.txt", "r")
data5 = my_file5.read()
data_into_list5 = data5.replace('\n', ' ').split(" ")
#print(data_into_list5)
my_file5.close()

my_file6 = open("StopWords_Geographic.txt", "r")
data6 = my_file6.read()
data_into_list6 = data6.replace('\n', ' ').replace('Geographic', ' ').replace('Cities', ' ').replace('Countries', ' ').replace('States', ' ').replace('|', ' ').split(" ")
#print(data_into_list6)
my_file6.close()

my_file7 = open("StopWords_Names.txt", "r")
data7 = my_file7.read()
data_into_list7 = data7.replace('\n', ' ').replace('Surnames from 1990 census > .002%.  www.census.gov.genealogy/names/dist.all.last', ' ').replace("|",'').split(" ")
#print(data_into_list7)
my_file7.close()

poswords = open("positive-words.txt", mode="r",encoding="latin-1")
data8 = poswords.read()
data_into_list8 = data8.replace('\n', ' ').split(" ")
#print(data_into_list8)
#poswords.close()

negwords = open("negative-words.txt", mode="r",encoding="latin-1")
data9 = negwords.read()
data_into_list9 = data9.replace('\n', ' ').split(" ")
#print(data_into_list9)
#negwords.close()

lis=data_into_list1+data_into_list3+data_into_list4+data_into_list5+data_into_list6+data_into_list7
#print(lis)
stpwrd.extend(lis)



user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.``3945.88 Safari/537.37"
#The below URL can be changed accordingly and this change will work if the element tags in the code are also changed(line 81,82)
url = 'https://insights.blackcoffer.com/challenges-and-opportunities-of-big-data-in-healthcare/'
data = requests.get(url, headers={'User-Agent': user_agent})
soup = BeautifulSoup(data.text, 'lxml')
title=soup.find_all('div',class_='td-parallax-header')
article=soup.find_all('div',class_='td-post-content')



sum3=0
sum6=0
count = 0
count1=0
sum9=0
sum10=0
sum12=0
for headline in title:
  te=headline.find('h1')
  a=te.text


#If the contents of the article wants to be added into a file
  '''text_file = open("art_txt.txt", "w")
  text_file.write(a)'''

  res = sum(not chr.isspace() for chr in a)

  pronounRegex = re.findall(r'\b(I|we|my|ours|(?-i:us))\b',a)
  lenofpro=len(pronounRegex)
  sum12+=lenofpro

  es1=re.findall(r'\b(\w+es)\b',a)
  lenofes1=len(es1)
  #print(lenofes1)
  #print(es1)
  sum9+=lenofes1

  ed1=re.findall(r'\b(\w+ed)\b',a)
  lenofed1=len(ed1)
  #print(lenofed1)
  #print(ed1)
  sum10+=lenofed1

  sent1=nltk.sent_tokenize(a)
  lenofsen1=len(sent1)
  sum6+=lenofsen1
  #print(sum6)

  text_tokens = word_tokenize(a)
  lenoftitle=len(text_tokens)
  #print(text_tokens)

  


  removing_custom_words = [words for words in text_tokens if not words in stpwrd]
  removing_custom_words= [''.join(d for d in t if d not in string.punctuation) for t in removing_custom_words]
  removing_custom_words = [t for t in removing_custom_words if t]
  lenofti=len(removing_custom_words)
  sum3+=lenofti
  #print(a)
  data_into_list10 = a.replace('\n', ' ').split(" ")
  #print(data_into_list10))

  intersection = []
  for item in data_into_list8:
    if item in data_into_list10:
      intersection.append(item)
  lenoftit=len(intersection)
  #print(lenoftit)

  intersection1 = []
  for item in data_into_list9:
    if item in data_into_list10:
      intersection1.append(item)
      #print(intersection1)
  lenoftit1=len(intersection1)*-1
  #print(lenoftit)
  #print(data_into_list10)
  vowels = "aeoui"

  for word in data_into_list10:
    count = 0 
    for letter in word:
      if letter.lower() in vowels:
        count = count + 1
    if(count>2):
      count1+=1
  #print(count1)




sum13=0
sum1=0
sum2=0
sum4=0
sum5=0
count3=0
sum7=0
sum8=0
sum11=0
sum14=0
for d in article:
  for dt in d.find_all('p'):
    b=dt.text
    #If the contents of the article wants to be added into a file
    #text_file.write(b)

    res1 = sum(not chr.isspace() for chr in b)
    sum14+=res1

    pronounRegex1 = re.findall(r'\b(I|we|my|ours|(?-i:us))\b',b)
    lenofpro1=len(pronounRegex1)
    sum11+=lenofpro1

    es=re.findall(r'\b(\w+es)\b',b)
    lenofes=len(es)
    #print(lenofes)
    #print(es)
    sum7+=lenofes

    ed=re.findall(r'\b(\w+ed)\b',b)
    lenofed=len(ed)
    #print(lenofed)
    #print(ed)
    sum8+=lenofed
    

    sent2=nltk.sent_tokenize(b)
    lenofsen2=len(sent2)
    sum5+=lenofsen2
    #print(sum5)

    text_tokens1 = word_tokenize(b)
    lenoftok1=len(text_tokens1)
    sum4+=lenoftok1
    #print(text_tokens1)#No of words

    removing_custom_words1 = [words for words in text_tokens1 if not words in stpwrd]
    #removing_custom_words1.remove(',')

    removing_custom_words1 = [''.join(c for c in s if c not in string.punctuation) for s in removing_custom_words1]
    removing_custom_words1 = [s for s in removing_custom_words1 if s]
    lenoftex=len(removing_custom_words1)
    sum2+=lenoftex
    #print(b)
    c=b.split()
    #print(intersection_list(c, data_into_list8))
    abcde=set(data_into_list8).intersection(c)
    #print(abcde)
    acd=len(abcde)
    #print(acd)
    sum13+=acd

    abcde1=set(data_into_list9).intersection(c)
    #print(abcde1)
    acd1=len(abcde1)*-1
    #print(acd1)
    sum1+=acd1
    vowels1 = "aeoui"
    for word in c:
      count2 = 0 
      for letter in word:
        if letter.lower() in vowels:
          count2 = count2 + 1
      if(count2>2):
        count3+=1
    #print(count3)
  #print(sum7)
  #print(sum8)
  #print(sum11)
  #print(sum14)
'''for word1 in a:
      count4 = 0 
      for letter1 in word1:
        if letter1.lower() in vowels1:
          count4 = count4 + 1
        
      if(coun2>2):
        count3+=1
  print(count3)'''
  
lenofchrinwords=res+sum14
lenofcxwor=count3+count2
nosylwor=lenofcxwor-(sum7+sum8+sum9+sum10)
len=lenoftitle+sum4#no of words
noofsent=sum6+sum5
noofcharac=sum2+sum3
poswords1=sum13+lenoftit
perspro=sum11+sum12
avgwrdlen=lenofchrinwords/len
print("Positive words are : ",poswords1)
negwords1=(sum1+lenoftit1)*-1
print("Negative words are : ",negwords1)
polscore=(poswords1-negwords1)/((poswords1+negwords1)+0.000001)
print("Polarity Score is : ",polscore)
subjsore=(poswords1+negwords1)/(noofcharac+0.000001)
print("The subjective score is : ",subjsore)
avgsenlen=len/noofsent
print("Average Sentence length is : ",avgsenlen)
ptofcxw=lenofcxwor/len
print("Percentage of complex words is : ",ptofcxw)
fogind=0.4*(avgsenlen+ptofcxw)
print("The fod index is : ",fogind)
print("The average number of words per sentence is : ",avgsenlen)
print("The number of complex words are : ",lenofcxwor)
print("Word count is : ",noofcharac)
print("Syllable words is :",nosylwor)
print("Number of Personal pronouns is :",perspro)
print("Average word length is :",avgwrdlen)