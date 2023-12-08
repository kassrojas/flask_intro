# import pyjokes
# joke = pyjokes.get_joke('en', 'neutral')
# print(joke)

###### FILE I / O input/output
# input from outside world and output into outside world
# wouldn't it be nice if we could input an image and then output a compressed image? With python, we can
# reading and writing files allows this to happen

# python has built in functions to open and write to files
# myTxtFile = open('test.txt') #can only read the file once
# print(myTxtFile)#<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

# print(myTxtFile.read()) #will only read the file once, works like a single line cursor
# print(myTxtFile.read()) #will output nothing

# myTxtFile.seek(0) # resets the cursor at the beginning of the file so it can read it again
# print(myTxtFile.read()) #will read file again-- once


# myTxtFile.seek(0)
# print(myTxtFile.readlines()) # [every, line, written, split, by, \n]

# #standard practice
# myTxtFile.close()


######## BETTER WAY OF DOING FILE I / O
# mode default is r, r+ means read and write to file
with open('test.txt', mode='r+') as myTxtFile: #'with' opens and closes for us
  newText = myTxtFile.write('hey, it\'s me!!!! Test.py over here!!!')
  print(myTxtFile.readlines())

# #a = append mode, adds to end of file vs starting cursor at [0]
# with open('test.txt', mode='a') as myTxtFile: 
#   newText = myTxtFile.write(':))))))')
#   print(newText)

# # w overwrites existing file with new file and new text, creates a new file if the one specified doesnt exist
# with open('file_that_dne_yet.txt', mode='w+') as willExistNow:
#   text = willExistNow.write('If you are seeing this then you did this correctly!\n This is another line')
#   willExistNow.seek(0)
#   # print(willExistNow.readlines())
#   for lines in willExistNow.readlines():
#     print(lines.strip())

####### most common modes are 'a', 'r', 'w'


try:
  with open('test.txt', mode='w') as myFile:
    print(myFile.read())
except FileNotFoundError as err:
  print('file does not exist')
  raise err
except IOError as err:
  print('IO error occurred')
  raise err


#### translator practice exercise
# pip install translate

from translate import Translator

try:
  with open('test.txt', mode='r') as testFile:
    translator = Translator(to_lang="es")
    translation = translator.translate(testFile.read())
    print(translation)
    with open('./test-es.txt', mode ='w') as spanishFile:
      spanishFile.write(translation)
except FileNotFoundError as err:
  print(f'File not found. \n{err}')
  