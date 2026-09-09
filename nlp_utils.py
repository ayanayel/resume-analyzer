import io
import PyPDF2
import docx


def extract_text_from_file(file, filename):

    extension = filename.split(".")[-1].lower()

    data = file.read()

    if extension == "txt":

        return data.decode("utf-8", errors="ignore")


    elif extension == "pdf":

        pdf = PyPDF2.PdfReader(
            io.BytesIO(data)
        )

        text = ""

        for page in pdf.pages:
            text = text + (page.extract_text() or "")

        return text


    elif extension == "docx":

        document = docx.Document(
            io.BytesIO(data)
        )

        text = ""

        for paragraph in document.paragraphs:
            text = text + paragraph.text + "\n"

        return text


    return ""