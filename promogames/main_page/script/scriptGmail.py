import smtplib
import email.message

def send_email(user_email, user_name, image_url):
    corpo_email = f"""
    <!DOCTYPE html>
    <html>
        <body style="font-family: Arial, sans-serif; font-size: 16px; line-height: 1.5; color: #333;">
            <h1 style="font-size: 24px; margin-top: 0;">Olá {user_name},</h1>
            <p style="margin-bottom: 1em;">Estamos animados em oferecer a você uma oportunidade incrível de economizar em seus jogos favoritos. Aproveite agora nossas promoções.</p>

            <p style="margin-bottom: 1em;">Não perca esta oportunidade e compre agora! A oferta é por tempo limitado.</p>

            <a href="" style="display: inline-block; padding: 1em; background-color: #00cc66; color: white; text-decoration: none; border-radius: 4px; font-weight: bold;">Compre agora</a>

            <p style="margin-top: 1em;">Atenciosamente,<br>Equipe PromoGames</p>
        </body>
    </html>

    """

    msg = email.message.Message()
    msg['Subject'] = "Economize agora em seus jogos favoritos!"
    msg['From'] = 'promogamesweb@gmail.com'
    msg['To'] = user_email
    password = 'cqdrjcfynmmlavtn' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))