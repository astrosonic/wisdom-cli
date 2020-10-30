import click
import getpass
import re
import sys
import time
import wikipedia


def printMessage(styled="CAVEAT > ",color="red",message=""):
    click.echo(click.style(styled,fg=color,bold=True)+message)

def obtntime():
    timestmp = time.localtime()
    timehour = str(timestmp.tm_hour)
    timemint = str(timestmp.tm_min)
    timesecs = str(timestmp.tm_sec)
    if int(timehour) < 10:  timehour = "0" + timehour
    if int(timemint) < 10:  timemint = "0" + timemint
    if int(timesecs) < 10:  timesecs = "0" + timesecs
    return timehour + ":" + timemint + ":" + timesecs

def prsehead(srchqery, purltext):
    while re.search("===== (.*) =====", purltext):
        purltext = purltext.replace("\n===== " + re.search("===== (.*) =====", purltext).group(1) + " =====", click.style(re.search("===== (.*) =====", purltext).group(1) + " > ", fg="green", bold=True))
    while re.search("==== (.*) ====", purltext):
        purltext = purltext.replace("\n==== " + re.search("==== (.*) ====", purltext).group(1) + " ====", click.style(re.search("==== (.*) ====", purltext).group(1) + " > ", fg="blue", bold=True))
    while re.search("=== (.*) ===", purltext):
        purltext = purltext.replace("\n=== " + re.search("=== (.*) ===", purltext).group(1) + " ===", click.style(re.search("=== (.*) ===", purltext).group(1) + " > ", fg="red", bold=True))
    while re.search("== (.*) ==", purltext):
        purltext = purltext.replace("\n== " + re.search("== (.*) ==", purltext).group(1) + " ==", click.style(re.search("== (.*) ==", purltext).group(1) + " > ", fg="magenta", bold=True))
    return purltext


def getpgurl(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).url
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("URL > ", fg="blue", bold=True) + purltext)
    printMessage("RAISED > ","green","1 result in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def gettitle(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).title
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("TITLE > ", fg="blue", bold=True) + purltext)
    printMessage("RAISED > ","green","1 result in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")

def savehtml(srchqery):
    pass


def getlinks(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).links
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("LINKS > ", fg="blue", bold=True))
    max_width = len(str(len(purltext)))+1
    for indx,val in enumerate(purltext,1):
        printMessage(f"#{indx}".rjust(max_width),"magenta"," " + val)
    printMessage("RAISED > ","green",str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getshort(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).summary
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("SUMMARY > ", fg="blue", bold=True) + "\n" + purltext)
    printMessage("RAISED > ","green","1 result in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getcreds(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).references
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("REFERENCES > ", fg="blue", bold=True))
    max_width=len(str(len(purltext)))+1
    for indx,val in enumerate(purltext,1):
        printMessage(f"#{indx}".rjust(max_width),"magenta"," " + val)
    printMessage("RAISED > ","green",str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getimage(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).images
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("IMAGES > ", fg="blue", bold=True))
    max_width = len(str(len(purltext)))+1
    for indx,val in enumerate(purltext,1):
        printMessage(f"#{indx}".rjust(max_width),"magenta"," " + val)
    printMessage("RAISED > ","green",str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getpgeid(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).pageid
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("PAGEID > ", fg="blue", bold=True) + purltext)
    printMessage("RAISED > ","green","1 result in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getrevid(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).revision_id
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("REVISIONID > ", fg="blue", bold=True) + str(purltext))
    printMessage("RAISED > ","green","1 result in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getprtid(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).parent_id
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("PARENTID > ", fg="blue", bold=True) + str(purltext))
    printMessage("RAISED > ","green","1 result in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getdcont(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).content
    stoptime = time.monotonic()
    duration = stoptime - strttime
    purltext = prsehead(purltext)
    printMessage("RESULT > ","green",click.style("CONTENT > ", fg="blue", bold=True) + "\n" + purltext)
    printMessage("RAISED > ","green","1 result in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getpgcat(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.page(srchqery).categories
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("CATEGORIES > ", fg="blue", bold=True))
    max_width = len(str(len(purltext)))+1
    for indx,val in enumerate(purltext,1):
        printMessage(f"#{indx}".rjust(max_width),"magenta"," " + val)
    printMessage("RAISED > ","green",str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")


def getitems(srchqery):
    strttime = time.monotonic()
    purltext = wikipedia.search(srchqery)
    stoptime = time.monotonic()
    duration = stoptime - strttime
    printMessage("RESULT > ","green",click.style("SEARCH > ", fg="blue", bold=True))
    max_width = len(str(len(purltext)))+1
    for indx,val in enumerate(purltext,1):
        printMessage(f"#{indx}".rjust(max_width),"magenta"," " + val)
    printMessage("RAISED > ","green",str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + obtntime() + "]")

def wkdonate():
    printMessage("THANKS > ","magenta","for considering donating to the initiative")
    wikipedia.donate()


@click.command()
@click.option("-u", "--getpgurl", "wkaction", flag_value="getpgurl", help="Get page URL if such page exists", required=True)
@click.option("-t", "--gettitle", "wkaction", flag_value="gettitle", help="Get page title if such page exists", required=True)
@click.option("-h", "--savehtml", "wkaction", flag_value="savehtml", help="Save page HTML to a file", required=True)
@click.option("-l", "--getlinks", "wkaction", flag_value="getlinks", help="Get the list of links available", required=True)
@click.option("-s", "--getshort", "wkaction", flag_value="getshort", help="Get page summary if such page exists", required=True)
@click.option("-r", "--getcreds", "wkaction", flag_value="getcreds", help="Get the list of references available", required=True)
@click.option("-i", "--getimage", "wkaction", flag_value="getimage", help="Get the list of images available", required=True)
@click.option("-d", "--getpgeid", "wkaction", flag_value="getpgeid", help="Get page identity if such page exists", required=True)
@click.option("-v", "--getrevid", "wkaction", flag_value="getrevid", help="Get revision identity if such page exists", required=True)
@click.option("-p", "--getprtid", "wkaction", flag_value="getprtid", help="Get parent identity if such page exists", required=True)
@click.option("-c", "--getdcont", "wkaction", flag_value="getdcont", help="Get page content if such page exists", required=True)
@click.option("-g", "--getpgcat", "wkaction", flag_value="getpgcat", help="Get page category if such page exists", required=True)
@click.option("-e", "--getitems", "wkaction", flag_value="getitems", help="Get list of search results", required=True)
@click.option("-o", "--wkdonate", "wkaction", flag_value="wkdonate", help="Donate to the Wikimedia project", required=True)
@click.option("-q", "--srchqery", "srchqery", help="Enter the query you wish to search for")
@click.version_option(version="09102020", prog_name="Wisdom CLI by t0xic0der")
def mainfunc(srchqery, wkaction):
    printMessage("WISDOM > ","green","Welcome " + getpass.getuser() + ", please wait while the results are obtained.")
    if wkaction == "wkdonate":
        wkdonate()
    else:
        try:
            eval(wkaction)(srchqery)
        except wikipedia.exceptions.DisambiguationError:
            printMessage(message="The query resolves to a Disambiguation page.")
        except wikipedia.exceptions.HTTPTimeoutError:
            printMessage(message="Timeout occured while processing the query.")
        except wikipedia.exceptions.RedirectError:
            printMessage(message="Page title unexpectedly resolved to a redirect.")
        except wikipedia.exceptions.PageError:
            printMessage(message="Couldn't find the Wikipedia page for the query.")
        except wikipedia.exceptions.WikipediaException:
            printMessage(message="Base Wikipedia exception class.")
        except Exception:
            printMessage(message="Exception occurred due to which results could not be displayed")


if __name__ == "__main__":
    mainfunc()