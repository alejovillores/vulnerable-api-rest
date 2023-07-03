import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class EmailService:

    def __init__(self):
        self.sender_email = 'fiuba.seguridad.grupo2@gmail.com'
        self.password = "fisfdpqyjwylkand"
        self.host = 'sandbox.smtp.mailtrap.io'
        self.port = 2525
    
    def send_email(self ):
        sender = "fiuba.seguridad.grupo2@gmail.com"
        receiver = "fiuba.seguridad.grupo2@gmail.com"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Aviso: Su cuenta pasará a ser paga"
        message["From"] = sender
        message["To"] = receiver

        text = """\
                Estimado/a ,
                Te escribo para informarte sobre cambios importantes que impactarán tu cuenta en nuestra plataforma.
                Para consultas adicionales, estamos aquí para ayudarte.
                Atentamente, seguridad fiuba"""

        html = """\
                <html>
                <body>
                    <p>Estimado usuario, <br>
                    Queremos informarte sobre un <b>cambio en el plan de pago de tu cuenta </b>.</p> 
                    <p>A partir de ahora, se requiere que elijas una opción adecuada en la plataforma para evitar la transición a una suscripción de pago.
                    Mantén tu plan gratuito actual seleccionando la opción correspondiente antes del las siguientes 48hrs.
                    Puedas realizarlo directamente <a href="http://localhost:5000/password/reset?new_password=pass"> ingresando en tu cuenta </a>
                    </p>
                    <br>
                    <p>Disculpe las molestias, attentamente grupo 2 - FIUBA SEGURIDAD</p>
                </body>
                </html>
                """
        mime_text = MIMEText(text, "text")
        mime_html = MIMEText(html, "html")
        message.attach(mime_text)
        message.attach(mime_html)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver, message.as_string())
        
