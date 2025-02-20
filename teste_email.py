import smtplib
from email.message import EmailMessage
from datetime import datetime

# Configurações
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587
EMAIL_ORIGEM = 'ggunstavo-019@hotmail.com'
EMAIL_DESTINATARIOS = ['ggunstavo-019@hotmail.com']
SENHA_APP = '5307 4832'  # Use a senha gerada

# Conteúdo do e-mail
msg = EmailMessage()
msg['Subject'] = f"🚀 Relatório de Kafka - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
msg['From'] = EMAIL_ORIGEM
msg['To'] = ', '.join(EMAIL_DESTINATARIOS)
msg.set_content("Este é um teste de envio de e-mail usando a senha de aplicativo.")

# Enviar e-mail
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ORIGEM, SENHA_APP)
        server.send_message(msg)
    print("📧 E-mail enviado com sucesso!")
except Exception as e:
    print(f"❌ Falha ao enviar o e-mail: {e}")
