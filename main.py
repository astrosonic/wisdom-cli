import click
import getpass
import re
import sys
import time
import wikipedia


class wikiclss():
    def __init__(self, srchqery):
        self.srchqery = srchqery

    def obtntime(self):
        timestmp = time.localtime()
        timehour = str(timestmp.tm_hour)
        timemint = str(timestmp.tm_min)
        timesecs = str(timestmp.tm_sec)
        if int(timehour) < 10:  timehour = "0" + timehour
        if int(timemint) < 10:  timemint = "0" + timemint
        if int(timesecs) < 10:  timesecs = "0" + timesecs
        return timehour + ":" + timemint + ":" + timesecs

    def prsehead(self, purltext):
        while re.search("===== (.*) =====", purltext):
            purltext = purltext.replace("\n===== " + re.search("===== (.*) =====", purltext).group(1) + " =====", click.style(re.search("===== (.*) =====", purltext).group(1) + " > ", fg="green", bold=True))
        while re.search("==== (.*) ====", purltext):
            purltext = purltext.replace("\n==== " + re.search("==== (.*) ====", purltext).group(1) + " ====", click.style(re.search("==== (.*) ====", purltext).group(1) + " > ", fg="blue", bold=True))
        while re.search("=== (.*) ===", purltext):
            purltext = purltext.replace("\n=== " + re.search("=== (.*) ===", purltext).group(1) + " ===", click.style(re.search("=== (.*) ===", purltext).group(1) + " > ", fg="red", bold=True))
        while re.search("== (.*) ==", purltext):
            purltext = purltext.replace("\n== " + re.search("== (.*) ==", purltext).group(1) + " ==", click.style(re.search("== (.*) ==", purltext).group(1) + " > ", fg="magenta", bold=True))
        return purltext

    def getpgurl(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).url
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("URL > ", fg="blue", bold=True) + purltext)
                click.echo(click.style("RAISED > ", fg="green", bold=True) + "1 result in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def gettitle(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).title
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("TITLE > ", fg="blue", bold=True) + purltext)
                click.echo(click.style("RAISED > ", fg="green", bold=True) + "1 result in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def savehtml(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()

    def getlinks(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).links
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("LINKS > ", fg="blue", bold=True))
                for indx in range(len(purltext)):
                    click.echo(click.style("#" + str(indx+1), fg="magenta", bold=True) + " " + purltext[indx])
                click.echo(click.style("RAISED > ", fg="green", bold=True) + str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getshort(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).summary
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("SUMMARY > ", fg="blue", bold=True) + "\n" + purltext)
                click.echo(click.style("RAISED > ", fg="green", bold=True) + "1 result in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getcreds(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).references
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("REFERENCES > ", fg="blue", bold=True))
                for indx in range(len(purltext)):
                    click.echo(click.style("#" + str(indx+1), fg="magenta", bold=True) + " " + purltext[indx])
                click.echo(click.style("RAISED > ", fg="green", bold=True) + str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getimage(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).images
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("IMAGES > ", fg="blue", bold=True))
                for indx in range(len(purltext)):
                    click.echo(click.style("#" + str(indx+1), fg="magenta", bold=True) + " " + purltext[indx])
                click.echo(click.style("RAISED > ", fg="green", bold=True) + str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getpgeid(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).pageid
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("PAGEID > ", fg="blue", bold=True) + purltext)
                click.echo(click.style("RAISED > ", fg="green", bold=True) + "1 result in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getrevid(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).revision_id
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("REVISIONID > ", fg="blue", bold=True) + str(purltext))
                click.echo(click.style("RAISED > ", fg="green", bold=True) + "1 result in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getprtid(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).parent_id
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("PARENTID > ", fg="blue", bold=True) + str(purltext))
                click.echo(click.style("RAISED > ", fg="green", bold=True) + "1 result in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getdcont(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).content
                stoptime = time.monotonic()
                duration = stoptime - strttime
                purltext = self.prsehead(purltext)
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("CONTENT > ", fg="blue", bold=True) + "\n" + purltext)
                click.echo(click.style("RAISED > ", fg="green", bold=True) + "1 result in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getpgcat(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.page(self.srchqery).categories
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("CATEGORIES > ", fg="blue", bold=True))
                for indx in range(len(purltext)):
                    click.echo(click.style("#" + str(indx+1), fg="magenta", bold=True) + " " + purltext[indx])
                click.echo(click.style("RAISED > ", fg="green", bold=True) + str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def getitems(self):
        if self.srchqery is None:
            click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "You do not seem to have provided a search query")
            sys.exit()
        else:
            try:
                strttime = time.monotonic()
                purltext = wikipedia.search(self.srchqery)
                stoptime = time.monotonic()
                duration = stoptime - strttime
                click.echo(click.style("RESULT > ", fg="green", bold=True) + click.style("SEARCH > ", fg="blue", bold=True))
                for indx in range(len(purltext)):
                    click.echo(click.style("#" + str(indx+1), fg="magenta", bold=True) + " " + purltext[indx])
                click.echo(click.style("RAISED > ", fg="green", bold=True) + str(len(purltext)) + " result(s) in " + str(duration)[0:3] + " seconds [" + self.obtntime() + "]")
            except wikipedia.exceptions.HTTPTimeoutError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Timeout occured while processing the query.")
            except wikipedia.exceptions.RedirectError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Page title unexpectedly resolved to a redirect.")
            except wikipedia.exceptions.PageError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Couldn't find the Wikipedia page for the query.")
            except wikipedia.exceptions.DisambiguationError:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "The query resolves to a Disambiguation page.")
            except Exception:
                click.echo(click.style("CAVEAT > ", fg="red", bold=True) + "Exception occurred due to which results could not be displayed")

    def wkdonate(self):
        click.echo(click.style("THANKS > ", fg="magenta", bold=True) + "for considering donating to the initiative")
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
    click.echo(click.style("WISDOM > ", fg="green", bold=True) + "Welcome " + getpass.getuser() + ", please wait while the results are obtained.")
    wikiobjc = wikiclss(srchqery)
    if wkaction == "getpgurl":      wikiobjc.getpgurl()
    elif wkaction == "gettitle":    wikiobjc.gettitle()
    elif wkaction == "savehtml":    wikiobjc.savehtml()
    elif wkaction == "getlinks":    wikiobjc.getlinks()
    elif wkaction == "getshort":    wikiobjc.getshort()
    elif wkaction == "getcreds":    wikiobjc.getcreds()
    elif wkaction == "getimage":    wikiobjc.getimage()
    elif wkaction == "getpgeid":    wikiobjc.getpgeid()
    elif wkaction == "getrevid":    wikiobjc.getrevid()
    elif wkaction == "getprtid":    wikiobjc.getprtid()
    elif wkaction == "getdcont":    wikiobjc.getdcont()
    elif wkaction == "getpgcat":    wikiobjc.getpgcat()
    elif wkaction == "getitems":    wikiobjc.getitems()
    elif wkaction == "wkdonate":    wikiobjc.wkdonate()


if __name__ == "__main__":
    mainfunc()