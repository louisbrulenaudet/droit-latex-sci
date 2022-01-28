# -*- coding: utf-8 -*-
import os
import uuid
import time
import platform

if platform.system() == "Darwin":
    os.system("clear")

elif platform.system() == "Windows":
    os.system("cls")


def laTex_templating(filename, extension, folder, data):
    """
    latex_templating : Str * Str * Dict[Str:Str] -> None
    latex_templating(data) Templating engine for LaTex documents. Return None.
    """
    with open(folder + filename + extension, "r") as file:
        textcontent = file.read()

        for key, value in data.items():
            try:
                textcontent = textcontent.replace("\{{"+ key + "}\}", value)
            except:
                continue

        rfc4122 = uuid.uuid4().hex
        with open(rfc4122 + extension, "w") as output:
            output.write(textcontent)

    return rfc4122


def pdfLaTex(rfc4122, extension):
    """
    pdfLaTex : Str * Str -> None
    pdfLaTex(rfc4122, extension) Runs commmand in console and compile LaTeX source code. Return None.
    """
    instruction = "xelatex " + rfc4122 + extension + " >/dev/null 2>&1" # LaTex Compilation using XeLaTeX.

    if platform.system() == "Darwin":
        try:
            os.system(instruction)

        except:
            try:
                os.system("brew help")

            except:
                os.system("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")

            os.system("brew install basictex  >/dev/null 2>&1")
            os.system(instruction)

    elif platform.system() == "Linux":
        try:
            os.system(instruction)

        except:
            os.system("sudo apt install texlive")
            os.system(instruction)

    return None


def clean_setup(filename, rfc4122):
    """
    clean_setup : Str * Str -> None
    clean_setup(filename, rfc4122) Removes log and aux files created by the compilation process and rename the pdf file. Return None.
    """
    os.remove(rfc4122 + ".aux")
    os.remove(rfc4122 + ".log")

    os.rename(rfc4122 + ".pdf", filename + ".pdf")
    os.rename(rfc4122 + ".tex", filename + ".tex")

    os.remove(filename + ".tex")

    return None


def display_pdf(filepath):
    """
    display_pdf : Str -> None
    display_pdf(filepath) Shows pdf files that was created. Return None.
    """
    if platform.system() == "Darwin":
        while os.path.isfile(filepath + ".pdf") == False:
            time.sleep(0.1)

        if os.path.isfile(filepath + ".pdf"):
            os.system("open " + filepath + ".pdf")
        else:
            raise ValueError("%s isn't a file!" % filepath + ".pdf")

    return None


def main():
    """
    Fonction Principale.
    """
    objects = {
        "Attestation sur l'honneur de filiation et de non condamnation" : {
            "folder" : "Templates/",
            "template" : "Attestation sur l'honneur de filiation et de non condamnation - Template",
            "extension" : ".tex"
        },
        "Attestation de domiciliation et d'autorisation de siège social" : {
            "folder" : "Templates/",
            "template" : "Attestation de domiciliation et d'autorisation de siège social - Template",
            "extension" : ".tex"
        },
        "Délégation de pouvoir en vue de l'accomplissement des actes de constitution" : {
            "folder" : "Templates/",
            "template" : "Délégation de pouvoir en vue de l'accomplissement des actes de constitution - Template",
            "extension" : ".tex"
        },
        "Avis de constitution de société" : {
            "folder" : "Templates/",
            "template" : "Avis de constitution de société - Template",
            "extension" : ".tex"
        },
    }

    data = {
        "prénom": "XXXX",
        "nom": "XXXX",
        "date de naissance": "6 septembre 2000",
        "ville de naissance": "XXXX",
        "numéro de voie": "XXXX",
        "libellé de la voie": "XXXX",
        "code postal": "XXXX",
        "ville": "XXXX",
        "prénom du père": "XXXX",
        "nom du père": "XXXX",
        "prénom de la mère": "XXXX",
        "nom de la mère": "XXXX",
        "raison sociale": "XXXX",
        "forme juridique": "S.C.I.",
        "capital": "XXXX",
        "objet social": "XXXX",
        "durée d'exercice": "XXXX",
        "qualité des apports": "XXXX",
        "modalités d'agrément": "XXXX",
        "localisation du RCS": "XXXX",
        "civilité du mandataire": "XXXX",
        "prénom du mandataire": "XXXX",
        "nom du mandataire": "XXXX",
        "société du mandataire": "XXXX",
        "date de naissance du mandataire": "XXXX",
        "ville de naissance du mandataire": "XXXX",
        "numéro de voie du mandataire": "XXXX",
        "libellé de la voie du mandataire": "XXXX",
        "code postal du mandataire": "XXXX",
        "ville du mandataire": "XXXX"
    }

    for key, value in objects.items():
        rfc4122 = laTex_templating(value["template"], value["extension"], value["folder"], data)
        pdfLaTex(rfc4122, value["extension"])
        display_pdf(rfc4122)
        clean_setup(key, rfc4122)

main()
