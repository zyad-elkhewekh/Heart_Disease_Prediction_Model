from pyngrok import ngrok

public_url = ngrok.connect(8501)
print("Your app is live at:", public_url)