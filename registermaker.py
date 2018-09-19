import PyPDF2
import re

register = {
    "Theater": {
        "tokens": ["theater"],
        "paginanummers": set()
    },
    "Spin": {
        "tokens": ["SPIN"],
        "paginanummers": set()
    }
}

pdfFileObj = open('test.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text = pageObj.extractText().replace("\n", "").replace("\r", "")
    for sleutelwoord in register:
        for token in register[sleutelwoord]["tokens"]:
            regex = re.compile(token, re.IGNORECASE)
            if regex.findall(text):
                register[sleutelwoord]["paginanummers"].add(count)

print(register)

pdfFileObj.close()
