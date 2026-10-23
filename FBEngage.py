#!/usr/bin/env python3
# coding=utf-8
# Niassoh Taarmos[CyberCoder]
import os, sys, time, random, re, json, getpass, urllib.parse, threading, hashlib, requests, mechanize, subprocess as sp, shutil, tempfile, tarfile
from mechanize import Browser
from requests.exceptions import ConnectionError
from urllib.error import URLError

# =========================
# ANSI Color Codes
# =========================
white   = '\033[1;37m'
red     = '\033[1;31m'
yellow  = '\033[1;33m'
green   = '\033[1;32m'
purple  = '\033[1;35m'
black   = '\033[1;30m'
blue    = '\033[1;34m'
cyan    = '\033[1;36m'
reset   = '\033[0m'

whitelite   = '\033[0;37m'
redlite     = '\033[0;31m'
yellowlite  = '\033[0;33m'
greenlite   = '\033[0;32m'
purplelite  = '\033[0;35m'
blacklite   = '\033[0;30m'
bluelite    = '\033[0;34m'
cyanlite    = '\033[0;36m'

bluewhitemix    = '\033[0;37;44m'
purplewhitemix  = '\033[0;37;45m'
greenredmix     = '\033[1;32;41m'
bluemix         = '\033[1;37;44m'
ibluemix        = '\033[1;34;47m'
ipurplemix      = '\033[1;35;47m'

my_color = [white, red, yellow, green, purple, black, blue, cyan]
randmclor = random.choice(my_color)
randomcolor = random.choice(my_color)

# === ADD MISSING FUNCTIONS / VARIABLES ====
finished = reset     # means color reset
def clr():
    os.system('clear' if os.name == 'posix' else 'cls')
def running(text):
    print(text)
def jalan(text):
    print(text)
def run(text):
    print(text)
    
# ========== PART 2: Tarball Extraction and Banners ==========
def checkxvzf():
    # Find the exact folder where here is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Look for the tarball next to the script
    tarball = os.path.join(script_dir, "AGITFOLDER.tar.gz")
    
    if not os.path.isfile(tarball):
        return

    base_dir = script_dir
    extract_dir = os.path.join(base_dir, "AGITFOLDER")
    os.makedirs(extract_dir, exist_ok=True)

    try:
        tar = tarfile.open(tarball, "r:gz")
        try:
            tar.extractall(path=base_dir, filter='data')
        except TypeError:
            tar.extractall(path=base_dir)
        tar.close()
    except (tarfile.TarError, OSError, IOError) as e:
        # Silently fail or handle corrupt archive
        return

    inner = os.path.join(base_dir, "AGITFOLDER")
    if not os.path.isdir(inner):
        os.makedirs(extract_dir, exist_ok=True)
    else:
        nested = os.path.join(inner, "AGITFOLDER")
        if os.path.isdir(nested):
            for item in os.listdir(nested):
                shutil.move(os.path.join(nested, item), os.path.join(inner, item))
            shutil.rmtree(nested, ignore_errors=True)

    try:
        os.remove(tarball)
    except OSError:
        pass
    # Removed print and sleep so it extracts silently

# ========== LOGO ==========
logo = """
{cyan}┏━╸┏━┓┏━╸┏━╸┏┓ ┏━┓┏━┓╻┏ ┏━╸┏┓╻┏━╸┏━┓┏━╸┏━╸
┣╸ ┣━┫┃  ┣╸ ┣┻┓┃ ┃┃ ┃┣┻┓┣╸ ┃┗┫┃╺┓┣━┫┃╺┓┣╸ 
╹  ╹ ╹┗━╸┗━╸┗━┛┗━┛┗━┛╹ ╹┗━╸╹ ╹┗━┛╹ ╹┗━┛┗━╸{reset}
{0}  {yellow}            FACEBOOK BOT v2.0
{green}      Automated Interaction & Management
{0}--------------------------------------------------
{red}[{green}✓{red}] {0}Creator  {red}: {white}Niassoh Taarmos{redlite}[{yellowlite}CyberCoder{redlite}]
{red}[{green}✓{red}] {0}YouTube  {red}: {purple}HackerFake424
{red}[{green}✓{red}] {0}Support  {red}: {cyan}Personal CyberCoder
{red}[{green}✓{red}] {0}GitHub   {red}: {green}https://github.com/{yellowlite}Mr{whitelite}Ghost{greenlite}Official 
{0}--------------------------------------------------
{reset}""".format(white, yellow=yellow, green=green, red=red, redlite=redlite, cyan=cyan, yellowlite=yellowlite, greenlite=greenlite, reset=reset, white=white, purple=purple, whitelite=whitelite)

br = Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

# ========== UTILITY FUNCTIONS ==========
def lodhirt():
    lodhirt = [
     'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀', '      ', 'Notice Warnings👀\n']
    for o in lodhirt:
        print('\r\033[1;37m            \033[1;34m' + o, end='')
        sys.stdout.flush()
        time.sleep(0.01)
        
def exit_program():
    print(red + "[!] Exit" + reset)
    sys.exit()
    
def random_color(x):
    w = my_color
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w)-1)] + i
    return print_colored(d)
    
def print_colored(x):
    for i, col in enumerate(my_color):
        x = x.replace('!' + col, col)
    x += reset
    sys.stdout.write(x + '\n')
    
def slow_print(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0001)
        
def loading_animation():
    dots = ['.   ', '..  ', '... ']
    for o in dots:
        sys.stdout.write("\r" + red + "[●] " + green + "Loading " + white + o)
        sys.stdout.flush()
        time.sleep(1)
        
# ========== LOGIN SYSTEM ==========
def parse_cookie_string(cookie_str):
    cookies = {}
    parts = re.split(r'[;,]\s*', cookie_str)
    for part in parts:
        if '=' not in part:
            continue
        key, value = part.split('=', 1)
        key = key.strip()
        value = value.strip()
        value = urllib.parse.unquote(value)
        if key and value:
            cookies[key] = value
    return cookies
    
def verify_facebook_token(token):
    try:
        resp = requests.get('https://graph.facebook.com/me?access_token=' + token, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if 'error' not in data:
                return data
    except Exception:
        pass
    return None
    
def is_cookie_session_valid(session):
    try:
        resp = session.get('https://m.facebook.com/me', timeout=15, allow_redirects=False)
        if resp.status_code == 302:
            location = resp.headers.get('Location', '')
            if 'login' in location or 'checkpoint' in location:
                return False
        if resp.status_code == 200:
            if 'login.php' in resp.url or 'checkpoint' in resp.url:
                return False
            if 'name="email"' in resp.text.lower() or 'name="pass"' in resp.text.lower():
                return False
        return True
    except Exception:
        return False
        
def extract_token_from_facebook_session(session):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    urls_to_try = [
        'https://m.facebook.com/',
        'https://m.facebook.com/me',
        'https://m.facebook.com/composer/',
        'https://m.facebook.com/ads/manager/',
        'https://m.facebook.com/feed'
    ]
    patterns = [
        r'"accessToken":"(EAA[^"]+)"',
        r'"access_token":"(EAA[^"]+)"',
        r'"accessToken":"(EAAG[^"]+)"',
        r'"access_token":"(EAAG[^"]+)"',
        r'"accessToken":"(EAAB[^"]+)"',
        r'"access_token":"(EAAB[^"]+)"',
        r'accessToken=([A-Za-z0-9]+)',
        r'access_token=([A-Za-z0-9]+)',
    ]
    for url in urls_to_try:
        try:
            resp = session.get(url, headers=headers, timeout=15, allow_redirects=True)
            if resp.status_code != 200:
                continue
            html = resp.text
            for pattern in patterns:
                matches = re.findall(pattern, html)
                for token in matches:
                    user_info = verify_facebook_token(token)
                    if user_info:
                        return token
            all_tokens = re.findall(r'(EAA[A-Za-z0-9]+)', html) + re.findall(r'(EAAG[A-Za-z0-9]+)', html) + re.findall(r'(EAAB[A-Za-z0-9]+)', html)
            for token in all_tokens:
                user_info = verify_facebook_token(token)
                if user_info:
                    return token
        except Exception:
            continue
    return None
    
def login():
    os.system('reset')
    try:
        open('login.txt', 'r')
        bot_menu()
    except (KeyError, IOError):
        os.system('reset')
        print(logo)
        print(cyan + "[☆] " + green + "FACEBOOK ACCOUNT LOGIN " + red + "[☆]" + reset)
        email = input(red + "[+] " + blue + "ID" + white + "|" + cyan + "Email" + white + " " + red + ":" + green + " ")
        password = getpass.getpass(purple + "[+] " + yellow + "Password " + yellow + ":" + purple + " ")
        loading_animation()
        try:
            br.open('https://m.facebook.com')
        except URLError:
            print("\n" + red + "[!] No connection" + reset)
            exit_program()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + email + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + password + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {"api_key": "882a8490361da98702bf97a021ddc14d", "credentials_type": "password", "email": email,
                        "format": "JSON", "generate_machine_id": "1", "generate_session_cookies": "1",
                        "locale": "en_US", "method": "auth.login", "password": password, "return_ssl_resources": "0",
                        "v": "1.0"}
                x = hashlib.new("md5")
                x.update(sig.encode('utf-8'))
                a = x.hexdigest()
                data.update({'sig': a})
                url = "https://api.facebook.com/restserver.php"
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                token_file = open("login.txt", 'w')
                token_file.write(z['access_token'])
                token_file.close()
                print('\n' + red + "[" + cyan + "✓" + red + "] " + green + "Login successful" + reset)
                bot_menu()
            except requests.exceptions.ConnectionError:
                print("\n" + red + "[!] No connection" + reset)
                exit_program()
        if 'checkpoint' in url:
            print("\n" + red + "[!] " + yellow + "Account Checkpoint" + reset)
            print("\n" + green + "[#] Please login again !" + reset)
            os.system('rm -rf login.txt')
            time.sleep(1)
            exit_program()
        else:
            print("\n" + red + "[!] Login Failed" + reset)
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
            
def login_with_cookie():
    os.system('reset')
    print(logo)
    cookie_input = input(red + "[?] " + green + "Enter cookie string (e.g., c_user=123; xs=abc; datr=xxx) or access token: " + white).strip()
    if not cookie_input:
        print(red + "[!] Input cannot be empty" + reset)
        exit_program()

    user_info = verify_facebook_token(cookie_input)
    if user_info:
        with open("login.txt", 'w') as f:
            f.write(cookie_input)
        print(red + "[" + cyan + "✓" + red + "] " + green + "Logged in as " + user_info.get('name', 'Unknown') + reset)
        bot_menu()
        return

    cookies = parse_cookie_string(cookie_input)
    if 'c_user' not in cookies or 'xs' not in cookies:
        print(red + "[!] Invalid cookie format. Missing c_user or xs." + reset)
        retry = input(red + "[?] " + green + "Try again? [y/n]: " + white)
        if retry.lower() == 'y':
            login_with_cookie()
        else:
            exit_program()
        return

    session = requests.Session()
    for key, value in cookies.items():
        session.cookies.set(key, value, domain='.facebook.com', path='/')
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    })

    print(red + "[✺] " + green + "Validating cookies and extracting access token..." + white)
    if not is_cookie_session_valid(session):
        print(red + "[!] Cookies are invalid or account is checkpointed." + reset)
        retry = input(red + "[?] " + green + "Try again? [y/n]: " + white)
        if retry.lower() == 'y':
            login_with_cookie()
        else:
            exit_program()
        return

    token = extract_token_from_facebook_session(session)
    if token:
        user_info = verify_facebook_token(token)
        if user_info:
            with open("login.txt", 'w') as f:
                f.write(token)
            print(red + "[" + cyan + "✓" + red + "] " + green + "Logged in as " + user_info.get('name', 'Unknown') + reset)
            bot_menu()
            return
    print(red + "[!] Could not extract access token automatically." + reset)
    retry = input(red + "[?] " + green + "Try again? [y/n]: " + white)
    if retry.lower() == 'y':
        login_with_cookie()
    else:
        exit_program()
        
# ========== BOT MENU ==========
def bot_menu():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login_screen()
    try:
        req = requests.get('https://graph.facebook.com/me?access_token=' + token)
        data = json.loads(req.text)
        name = data['name']
        user_id = data['id']
    except KeyError:
        print(red + "[!] Account Checkpoint" + reset)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login_screen()
    except requests.exceptions.ConnectionError:
        print(red + "[!] No connection" + reset)
        exit_program()

    os.system("reset")
    print(logo)
    print(red + "["+ green +"+"+ red +"]"+ green +" Name "+ red +": " + white + name)
    print(red + "["+ green +"+"+ red +"]"+ green +" ID   "+ red +": " + white + user_id)
    print(black + "-" * 50)
    print(red + "["+ green +"1"+ red +"] " + white + "Bot Reactions Target Post")
    print(red + "["+ green +"2"+ red +"] " + white + "Bot Reactions Group Post")
    print(red + "["+ green +"3"+ red +"] " + white + "Bot Comments Target Post")
    print(red + "["+ green +"4"+ red +"] " + white + "Bot Comments Group Post")
    print(red + "["+ green +"5"+ red +"] " + white + "Mass Delete My Posts")
    print(red + "["+ green +"6"+ red +"] " + white + "Mass Accept Friend Requests")
    print(red + "["+ green +"7"+ red +"] " + white + "Mass Delete All Friends")
    print(red + "["+ green +"8"+ red +"] " + white + "Create Post")
    print(red + "["+ green +"9"+ red +"] " + white + "Logout")
    print(red + "["+ green +"0"+ red +"] " + white + "Exit program")
    print(black + "-" * 50)
    bot_choice()
    
def bot_choice():
    choice = input(red + "["+ green +"ッ"+ red +"]"+ yellow +" Enter"+ white +"Choose"+ black +"]"+ red +"> " + green)
    if choice == "":
        print(red + "[!] Wrong input" + reset)
        bot_choice()
    elif choice == "1":
        react_target()
    elif choice == "2":
        react_group()
    elif choice == "3":
        comment_target()
    elif choice == "4":
        comment_group()
    elif choice == "5":
        delete_my_posts()
    elif choice == "6":
        accept_friend_requests()
    elif choice == "7":
        delete_all_friends()
    elif choice == "8":
        create_post()
    elif choice == "9":
        os.system('rm -rf login.txt')
        print(red + "[!] Logged out" + reset)
        time.sleep(1)
        login_screen()
    elif choice == "0":
        exit_program()
    else:
        print(red + "[!] Wrong input" + reset)
        bot_choice()
        
# ---------- Reaction Types ----------
def get_reaction_type():
    print(cyan + "-" * 40)
    print(yellow + "[1] Like")
    print(yellow + "[2] Love")
    print(yellow + "[3] Wow")
    print(yellow + "[4] Haha")
    print(yellow + "[5] Sad")
    print(yellow + "[6] Angry")
    print(cyan + "-" * 40)
    choice = input(red + "["+ green +"ッ"+ red +"]"+ yellow +" Enter"+ white +"Choose"+ black +"]"+ red +"> " + green)
    types = {"1": "LIKE", "2": "LOVE", "3": "WOW", "4": "HAHA", "5": "SAD", "6": "ANGRY"}
    return types.get(choice, "LIKE")
    
def react_target():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    target_id = input(red + "[+] " + green + "Target ID: " + white)
    limit = input(red + "[!] " + green + "Limit (number of posts): " + white)
    reaction = get_reaction_type()
    try:
        url = "https://graph.facebook.com/" + target_id + "?fields=feed.limit(" + limit + ")&access_token=" + token
        resp = requests.get(url)
        data = json.loads(resp.text)
        slow_print(red + "[✺] " + green + "Reacting... " + white)
        print(42 * "-")
        count = 0
        for post in data['feed']['data']:
            post_id = post['id']
            react_url = "https://graph.facebook.com/" + post_id + "/reactions?type=" + reaction + "&access_token=" + token
            requests.post(react_url)
            print(green + "[" + white + post_id[:10] + "... " + green + "] " + reaction)
            count += 1
        print(42 * "-")
        print(red + "[+] " + green + "Done " + white + str(count) + " reactions")
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
    except KeyError:
        print(red + "[!] Target not found or no posts" + reset)
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
        
def react_group():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    group_id = input(red + "[+] " + green + "Group ID: " + white)
    limit = input(red + "[!] " + green + "Limit (number of posts): " + white)
    reaction = get_reaction_type()
    try:
        url = "https://graph.facebook.com/v3.0/" + group_id + "?fields=feed.limit(" + limit + ")&access_token=" + token
        resp = requests.get(url)
        data = json.loads(resp.text)
        slow_print(red + "[✺] " + green + "Reacting... " + white)
        print(42 * "-")
        count = 0
        for post in data['feed']['data']:
            post_id = post['id']
            react_url = "https://graph.facebook.com/" + post_id + "/reactions?type=" + reaction + "&access_token=" + token
            requests.post(react_url)
            print(green + "[" + white + post_id[:10] + "... " + green + "] " + reaction)
            count += 1
        print(42 * "-")
        print(red + "[+] " + green + "Done " + white + str(count) + " reactions")
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
    except KeyError:
        print(red + "[!] Group not found or no posts" + reset)
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
        
def comment_target():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    print(red + "[!] " + green + "Use " + white + "'<>' " + green + "for new lines")
    target_id = input(red + "[+] " + green + "Target ID: " + white)
    comment = input(red + "[+] " + green + "Comment: " + white)
    limit = input(red + "[!] " + green + "Limit (number of posts): " + white)
    comment = comment.replace('<>', '\n')
    try:
        url = "https://graph.facebook.com/" + target_id + "?fields=feed.limit(" + limit + ")&access_token=" + token
        resp = requests.get(url)
        data = json.loads(resp.text)
        slow_print(red + "[✺] " + green + "Commenting... " + white)
        print(42 * "-")
        count = 0
        for post in data['feed']['data']:
            post_id = post['id']
            comment_url = "https://graph.facebook.com/" + post_id + "/comments?message=" + comment + "&access_token=" + token
            requests.post(comment_url)
            print(green + "[" + white + comment[:10].replace('\n', ' ') + "... " + green + "]")
            count += 1
        print(42 * "-")
        print(red + "[+] " + green + "Done " + white + str(count) + " comments")
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
    except KeyError:
        print(red + "[!] Target not found or no posts" + reset)
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
        
def comment_group():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    print(red + "[!] " + green + "Use " + white + "'<>' " + green + "for new lines")
    group_id = input(red + "[+] " + green + "Group ID: " + white)
    comment = input(red + "[+] " + green + "Comment: " + white)
    limit = input(red + "[!] " + green + "Limit (number of posts): " + white)
    comment = comment.replace('<>', '\n')
    try:
        url = "https://graph.facebook.com/v3.0/" + group_id + "?fields=feed.limit(" + limit + ")&access_token=" + token
        resp = requests.get(url)
        data = json.loads(resp.text)
        slow_print(red + "[✺] " + green + "Commenting... " + white)
        print(42 * "-")
        count = 0
        for post in data['feed']['data']:
            post_id = post['id']
            comment_url = "https://graph.facebook.com/" + post_id + "/comments?message=" + comment + "&access_token=" + token
            requests.post(comment_url)
            print(green + "[" + white + comment[:10].replace('\n', ' ') + "... " + green + "]")
            count += 1
        print(42 * "-")
        print(red + "[+] " + green + "Done " + white + str(count) + " comments")
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
    except KeyError:
        print(red + "[!] Group not found or no posts" + reset)
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
        
def delete_my_posts():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
        req = requests.get('https://graph.facebook.com/me?access_token=' + token)
        data = json.loads(req.text)
        name = data['name']
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    print(green + "[+] Account: " + white + name)
    slow_print(red + "[+] " + green + "Deleting posts..." + white)
    print(42 * "-")
    feed = requests.get('https://graph.facebook.com/me/feed?access_token=' + token)
    posts = json.loads(feed.text)
    deleted = 0
    for p in posts['data']:
        pid = p['id']
        try:
            resp = requests.delete('https://graph.facebook.com/' + pid + '?access_token=' + token)
            if resp.status_code == 200:
                print(green + "[" + white + pid[:10] + "..." + green + "] Deleted")
                deleted += 1
            else:
                print(red + "[" + white + pid[:10] + "..." + red + "] Failed")
        except Exception:
            print(red + "[" + white + pid[:10] + "..." + red + "] Error")
    print(42 * "-")
    print(red + "[+] " + green + "Deleted " + white + str(deleted) + " posts")
    input("\n" + red + "[ " + white + "Back " + red + "]")
    bot_menu()
    
def accept_friend_requests():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    limit = input(red + "[!] " + green + "Limit (number of requests): " + white)
    url = 'https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + token
    r = requests.get(url)
    requests_data = json.loads(r.text)
    if not requests_data['data']:
        print(red + "[!] No friend requests" + reset)
        input("\n" + red + "[ " + white + "Back " + red + "]")
        bot_menu()
    slow_print(red + "[✺] " + green + "Accepting... " + white)
    print(42 * "-")
    accepted = 0
    for req in requests_data['data']:
        from_id = req['from']['id']
        name = req['from']['name']
        accept_url = 'https://graph.facebook.com/me/friends/' + from_id + '?access_token=' + token
        resp = requests.post(accept_url)
        if 'error' in resp.text:
            print(white + "[ " + red + "Failed" + white + " ] " + name)
        else:
            print(white + "[ " + green + "Accepted" + white + " ] " + name)
            accepted += 1
    print(42 * "-")
    print(red + "[+] " + green + "Accepted " + white + str(accepted) + " requests")
    input("\n" + red + "[ " + white + "Back " + red + "]")
    bot_menu()
    
def delete_all_friends():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    slow_print(red + "[✺] " + green + "Deleting friends... " + white)
    print(red + "[!] Press Ctrl+C to stop" + white)
    print(42 * "-")
    try:
        friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        data = json.loads(friends.text)
        deleted = 0
        for friend in data['data']:
            name = friend['name']
            uid = friend['id']
            del_url = "https://graph.facebook.com/me/friends?uid=" + uid + "&access_token=" + token
            requests.delete(del_url)
            print(white + "[" + green + "Deleted" + white + "] " + name)
            deleted += 1
        print(42 * "-")
        print(red + "[+] " + green + "Deleted " + white + str(deleted) + " friends")
    except KeyboardInterrupt:
        print("\n" + red + "[!] Stopped" + reset)
    input("\n" + red + "[ " + white + "Back " + red + "]")
    bot_menu()
    
def create_post():
    os.system('reset')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(red + "[!] Token not found" + reset)
        bot_menu()
    print(logo)
    msg = input(red + "[+] " + green + "Status message: " + white)
    if msg == "":
        print(red + "[!] Message cannot be empty" + reset)
    else:
        url = "https://graph.facebook.com/me/feed?method=POST&message=" + msg + "&access_token=" + token
        res = requests.get(url)
        op = json.loads(res.text)
        slow_print(red + "[✺] " + green + "Creating post... " + white)
        print(42 * "-")
        print(red + "[+] " + green + "Post ID: " + white + op['id'])
    input("\n" + red + "[ " + white + "Back " + red + "]")
    bot_menu()

# ========== NEW FEATURE FUNCTIONS (repo_update, telegram, backmenu, exit) ==========
REPO_URL = "https://github.com/MrGhostOfficial/FbEngage.git"
TARGET = os.path.expanduser("~/FbEngage")

def repo_update():
    clr()
    os.system("bash -c \"source <(echo 'dHRlIC0tZnJhbWUtcmF0ZSA2NjYgLWkgJFBSRUZJWC9zaGFyZS9pZ2hvc3QvZ2l0LnVwZGF0ZSAtLXJhbmRvbS1lZmZlY3QgLS1leGNsdWRlLWVmZmVjdHMgbWF0cml4' | base64 -d)\"")
    print("{}Target contents folder kept removed inside{}:{} {} {}".format(blue, redlite, red, TARGET, finished))
    if not os.path.exists(TARGET):
        os.makedirs(TARGET)
    for item in os.listdir(TARGET):
        item_path = os.path.join(TARGET, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path, ignore_errors=True)
        else:
            os.unlink(item_path)
    print("{}Cloning fresh repository{}...{}".format(greenlite, redlite, finished))
    temp_dir = tempfile.mkdtemp()
    try:
        sp.check_call(["git", "clone", REPO_URL, temp_dir])
    except sp.CalledProcessError as e:
        print("Git clone failed: {}".format(e))
        shutil.rmtree(temp_dir, ignore_errors=True)
        return
    for item in os.listdir(temp_dir):
        src = os.path.join(temp_dir, item)
        dst = os.path.join(TARGET, item)
        shutil.move(src, dst)
    shutil.rmtree(temp_dir, ignore_errors=True)
    print("{}✓ Success{}! {}Files are now inside {} {}({}folder preserved{}){}\n".format(greenlite, red, cyan, TARGET, redlite, yellowlite, redlite, finished))
    sp.call(["ls", TARGET])
    code_file = os.path.join(TARGET, "FbEngage.py")
    if os.path.exists(code_file):
        sp.call(["chmod", "+x", code_file])
    else:
        print("FbEngage not found")
        sp.call(["ls", TARGET])
        time.sleep(2)
        sys.exit()
        
def telegram():
    clr()
    os.system("bash -c \"source <(echo 'dHRlIC0tZnJhbWUtcmF0ZSA2NjYgLWkgJFBSRUZJWC9zaGFyZS9pZ2hvc3QvdGVsZWdyYW0gLS1yYW5kb20tZWZmZWN0IC0tZXhjbHVkZS1lZmZlY3RzIG1hdHJpeA' | base64 -d)\"")
    jalan('{}[{}INFO{}] {}Hello User{}, {}if you facing any issues about my projects{}, {}Then give me your issues screenshot and write about your issues in telegram group, if You have also github account then dont forget to Follow/Stars Me on GitHub{}, {}Thanks for with us ENJOY{}.{}(👀){}'.format(red,green,red,cyan,redlite,cyan,redlite,cyan,redlite,cyan,whitelite,redlite,finished))
    time.sleep(3)
    running('{}Url↪️{}: {}https://t.me/NetCyberCoder{}'.format(cyan,redlite,yellowlite,finished))
    os.system('xdg-open https://t.me/NetCyberCoder')
    backmenu()
    
def backmenu():
    running(('\n{}if you dont understand how to Use it then follow \nme telegram group or my youtube channel.{}').format(purplelite, finished))
    running(('  {}+----------{}[{}Secondary~Menu{}]{}----------------+{}').format(black, red, whitelite, red, black, finished))
    running(('   {}| {}[{}1{}] {}Main-menu                          {}|{}').format(black, red, green, red, yellow, black, finished))
    running(('   {}| {}[{}e{}] {}Exit                               {}|{}').format(black, red, white, red, yellow, black, finished))
    running(('   {}+----------------------------------------+{}').format(black, finished))
    try:
        inp = input(('{}[{}ッ{}]{} EnterChoose{}]{}> {}').format(red, white, red, yellow, black, red, finished))
    except (KeyboardInterrupt, EOFError):
        run('Non-Active!!')
    if inp == '1' or inp == '01':
        login_screen()
    elif inp == 'e' or inp == 'E':
        exit_program()
    else:
        running(('{}Wrong input!{}').format(red, finished))
        time.sleep(2)
        backmenu()
        
def exit():
    clr()
    os.system("bash -c \"source <(echo 'dHRlIC0tZnJhbWUtcmF0ZSA2NjYgLWkgJFBSRUZJWC9zaGFyZS9pZ2hvc3QvbG9nb3V0IC0tcmFuZG9tLWVmZmVjdCAtLWV4Y2x1ZGUtZWZmZWN0cyBtYXRyaXg' | base64 -d)\"")
    running(('{}   +----------------------------------------+{}').format(black, finished))
    running(('{}   |    {}Join telegram group Account.        {}|{}').format(black, green, black, finished))
    running(('{}   |       {}@NetCyberCoder                   {}|{}').format(black, yellow, black, finished))
    running(('{}   |----------------------------------------|{}').format(black, finished))
    running(('{}   |          {}Bye Bye {}( {}^{}_{}^ {}){}/              {}|{}').format(black, cyan, white, red, cyan, red, white, whitelite, black, finished))
    running(('{}   +----------------------------------------+{}').format(black, finished))
    running(('{}       Friends keep supporting me and{}').format(purplelite, finished))
    running(('{}       Motivating me for making projects{}').format(yellowlite, finished))
    running(('{}       FOR YOU ENJOY..🌿👀{}').format(greenlite, finished))
    run('       See you at next time bye!')
    print("\n")
    time.sleep(1)
    sys.exit()
    
# ========== LOGIN SCREEN (MODIFIED) ==========
def login_screen():
    checkxvzf()
    clr()
    os.system('reset')
    print(logo)
    lodhirt()
    print(ipurplemix + " Don't Use Your Real Account:"+ reset)
    print(ibluemix + " Use this app and collect Access Token:"+ reset)
    print(bluelite + " Url↪️"+ red +": "+ yellowlite + "https://bit.ly/4fB7AhS"+ reset)
    print(ibluemix + " Kiwi Browser.apk ExtensionsCRX:"+ reset)
    print(bluelite + " Url↪️"+ red +": "+ yellowlite + "https://bit.ly/4v4ON3b"+ reset)
    print(ibluemix + " Use 2FA.CN Code.apk enable 2FA on your account:"+ reset)
    print(bluelite + " Url↪️"+ red +": "+ yellowlite + "https://bit.ly/42Ojmhu"+ reset)
    print(ibluemix + " If app not installed, enable Shizuku & USB/Wireless Debugging in Developer Options."+ reset)
    print(black + "-" * 50)
    print(reset + "              " + bluewhitemix + "First Use This⤵️" + reset)
    print(red + "           ["+ green +"i"+ red +"] " + green + "TermuxElevated\n")
    print(red + "["+ green +"1"+ red +"] " + white + "Login with Email"+ black +"/"+ white +"Password\n")
    print(red + "["+ green +"2"+ red +"] " + white + "Login with Cookie"+ black +"/"+ white +"Access Token\n")
    print(red + "["+ green +"3"+ red +"] " + white + "Facebook"+ black +"/"+ white +"Cracking Old\n")
    print(red + "["+ green +"u"+ red +"] " + white + "Latest Update" + red + " ["+ green +"t"+ red +"] " + white + "Telegram Us" + red + " ["+ green +"e"+ red +"] " + white + "Exit tool")
    print(black + "-" * 50)
    choice = input(red + "["+ green +"ッ"+ red +"]"+ yellow +" Enter"+ white +"Choose"+ black +"]"+ red +"> " + green)
    if choice == "":
        print(red + "[!] Invalid input" + reset)
        exit_program()
    elif choice == "i":
        clr()
        os.system("bash -c \"source <(echo 'dHRlIC0tZnJhbWUtcmF0ZSA2NjYgLWkgJFBSRUZJWC9zaGFyZS9pZ2hvc3QvcGVybWlzc2lvbiAtLXJhbmRvbS1lZmZlY3QgLS1leGNsdWRlLWVmZmVjdHMgbWF0cml4' | base64 -d)\"")
        running('{}[{}?{}] {}If you already using my {}TermuxElevated{}, {}then\n    dont need again{}, {}you can use this tool{}, \n{}   just update use{}: {}pkg ighost-install{}'.format(red, white, red, cyan, purple, redlite, cyan, redlite, cyan, redlite, cyan, redlite, greenlite, finished))
        running('{}Url↪️{}: {}https://github.com/MrGhostOfficial/TermuxElevated{}'.format(cyan, redlite, yellowlite, finished))
        time.sleep(5)
        os.system('xdg-open https://github.com/MrGhostOfficial/TermuxElevated')
        backmenu()
    elif choice == "1":
        login()
    elif choice == "2":
        login_with_cookie()
    elif choice.lower() == "3":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        crack_path = os.path.join(script_dir, "AGITFOLDER", "FbCrack.py")
        os.system(f'python "{crack_path}"')
    elif choice.lower() == "u":
        repo_update()
    elif choice.lower() == "t":
        telegram()
    elif choice == "e":
        exit()
    else:
        print(red + "[!] Wrong input" + reset)
        exit_program()
        
if __name__ == "__main__":
    login_screen()