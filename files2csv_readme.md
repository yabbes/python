## Automatized file export with Python

I wrote a script with Python to create a catalogue of all files in a given directory in the csv format.

### Automated parsing of doc / docx files
Other than just list the file contents, I wanted the script also to automatically give me a brief idea of what the contained Word documents were about. To achieve this I used the **python-docx** module.

So whenever I would find a file with a Word file extension, I would handle it like so:
```python
def getDocxSummary(file):
    try:
        doc = docx.Document(file)
        ftext = ''
        for p in doc.paragraphs:
            for run in p.runs:
                ftext += run.text
        if len(ftext) > 200:
            return ftext[0:200]
        else:
            return ftext
    except:
        return ''

```

Because I had to handle mainly docx files for the task I wrote this script for, this already helped me a great deal further classifying the filecontents lateron when editing the csv and making an Excel spreadsheet.

Obviously the script could be enhanced to handle text files the same way or maybe PDF there are solutions as well. I didn't do it here, but obviously parsing text files would have been even easier;)

### Creating the csv
Creating a new output.csv file is simple in Python

```python
with open(sys.argv[2],'w', encoding='utf-8', newline='') as f:        
    w = csv.writer(f, delimiter=",")
    w.writerow(['file', 'complete path', 'file extension', 'file size', 'content-summary', 'last modified'])

```
And then I would collect the necessary information and put it in a new row like so:
```python
try:
	w.writerow([filename, os.path.join(path, filename), fext, fsize, content_summary, ftimestamp])
	print(path + '/' + filename)
except UnicodeEncodeError:
	print('UnicodeEncodeError')
```
#### Wait, what's this try / except for?
Well, I was a bit lazy to try and decode and encode the filename + path accordingly, as this error only occured for one file during my usage. The error arises from the fact that filenames on Unix systems and for Python as well are just bytes. They don't have to follow utf-8 encoding *per se*. So sometimes when re-encoding the filenames to put them as utf-8 strings into a csv you get an error like that.

On top of that the csv module of Python has historically (in Python2) had issues with unicode. [It did not really support it.](https://docs.python.org/2/library/csv.html) Now in Python3 it should be supported, but the original encoding of the files did not have to be utf-8 like I said above, so I just got lazy and skipped this one file by catching the error.

### Filtering file extensions
Because the folder I wanted to catalogize had a huge number of irrelevant files, I used this simple filter inside the loop through ```paths, dirs, files``` of the  ```os.walk()``` method

```python
wanted = ['.docx', '.doc', '.pdf', '.DOC', '.PDF', '.DOCX', '.txt', '.TXT', '.pub', '.xls', '.xlsx']

# fext = file extension

if fext not in wanted:
    continue

```

