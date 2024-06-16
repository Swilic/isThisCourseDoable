import fitz

def getPdfText(pdf_path):
    pdf = fitz.open(pdf_path)
    text = ''
    for page in pdf:
        text += page.get_text("text")
    return text

def addMatAndNote(text):
    mat, note = [], []
    i = 0
    while i < len(text):
        if text[i].startswith('000'):
            mat.append(text[i])
            i+=1
            if text[i] not in ['ABS', 'ndp'] and text[i].replace('.', '', 1).isdigit() and float(text[i]) > 3:
                note.append(float(text[i]))
        i+=1
            
    return mat, note

def getParticipation(mat, note):
    return len(note) / len(mat) * 100

def getTauxReussite(note):
    return len([n for n in note if n >= 10]) / len(note) * 100

def getTop(note, n=5):
    sorted_note = sorted(note, reverse=True)
    return sorted_note[:5]

def printTop(top):
    for i, n in enumerate(top):
        print(f'Top {i+1}: {n}')

def main(path):
    pdf_text = getPdfText(path).split('\n')
    # print(pdf_text)

    mat, note = addMatAndNote(pdf_text)
    taux = getParticipation(mat, note)
    reussite = getTauxReussite(note)
    top = getTop(note, 5)

    print(f"Nombre d'étudiants: {len(mat)}")
    print(f'Taux de participation: {taux:.2f}% = {int(len(mat)*taux/100)} étudiants')
    print(f'Taux de réussite: {reussite:.2f}% = {int(len(note)*reussite/100)} étudiants')
    printTop(top)
    

if __name__ == '__main__':
    pdf_path = '/home/ahew/dora/Physique/202324_PHYS-F-103_SES1_anonymous.pdf'
    main(pdf_path)
 