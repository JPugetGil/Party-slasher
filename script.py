import sys
import os
import json
import random
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader, select_autoescape

def assert_exists(file_path):
    if not os.path.exists(file_path):
        print(f'{file_path} could not be found.')
        exit(1)

# read config json from file path
def read_config(file_path):
    assert_exists(file_path)
    with open(file_path, 'r', encoding="utf8") as f:
        return json.load(f)
    
def has_one_matched_with_himself(victims, killers):
    for i in range(len(victims)):
        if (victims[i] == killers[i]):
            return True
    return False
    
# shuffle all the elements inside an array and match them with another one
def shuffle(victims):
    killers = victims.copy()
    random.shuffle(killers)
    while has_one_matched_with_himself(victims, killers):
        print("Bad shuffle: a person cannot be matched with himself. Shuffling again.")
        random.shuffle(killers)
    print("Ended shuffle.")
    return killers, victims

# assign a symbol to each killer
def assign_symbol(killers, victims, symbols):
    random.shuffle(symbols)
    story = []
    for i in range(len(killers)):
        # print(f'{killers[i]} kills {victims[i]} with {symbols[i]}')
        story.append({
            "killer": killers[i],
            "victim": victims[i],
            "weapon": symbols[i]
        })
    return story

def send_email(to, subj, body):
    """Sends an email."""
    config = read_config("./config-email.json")
    smtp_address = config["smtp_address"]
    smtp_port = config["smtp_port"]
    email_address = config["email_address"]
    email_password = config["email_password"]

    # Send the mail
    message = MIMEMultipart('alternative')
    message['Subject'] = subj
    message['From'] = email_address
    message['To'] = to
    html_part = MIMEText(body, 'html', 'utf-8')
    message.attach(html_part)

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=ssl.create_default_context()) as server:
        # connexion au compte
        server.login(email_address, email_password)
        # envoi du mail
        server.sendmail(email_address, to, message.as_string())

def send_template_email(template, to, subj, **kwargs):
    """Sends an email using a template."""
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template(template)
    send_email(to, subj, template.render(**kwargs))

def tell_the_story(story, lieu):
    """Sends an email to each killer and victim."""
    for i in range(len(story)):
        send_template_email(
            template='criminal.html',
            to=story[i]['killer']['email'],
            subj='Mission de haute importance',
            criminel=story[i]['killer']['name'],
            victime=story[i]['victim']['name'],
            arme=story[i]['weapon'],
            lieu=lieu
        )
        # print(f"Sending email to {story[i]['killer']['name']} ({story[i]['killer']['email']}) : you will kill {story[i]['victim']['name']} with {story[i]['weapon']}")

        send_template_email(
            template='victim.html',
            to=story[i]['victim']['email'],
            subj='Attention à vous !',
            victime=story[i]['victim']['name'],
            arme=story[i]['weapon']
        )
        # print(f"Sending email to {story[i]['victim']['name']} ({story[i]['victim']['email']}) : the sign {story[i]['weapon']} will kill you")

def main():
    # read config
    config = read_config("./config.json")
    killers, victims = shuffle(config["users"])
    story = assign_symbol(killers, victims, config["symbols"])
    tell_the_story(story, config["lieu"])

if __name__ == "__main__":
    main()
