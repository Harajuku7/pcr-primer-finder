def fastaOpen(filename):
    file_object  = open(filename, "r")
    content = file_object.read()
    return content

def fastaConvert(fastaString):
    if fastaString[0] == ">":
        endLineIndex = fastaString.index('\n')
        title = fastaString[:endLineIndex]
        sequence = fastaString[endLineIndex+1:]
        sequence = sequence.replace("\n", "");
        sequence = sequence.replace("\r", "");
        return [title, sequence]
    else:
        fastaString = fastaString.replace("\n", "");
        fastaString = fastaString.replace("\r", "");
        return ["Untitled", fastaString]
