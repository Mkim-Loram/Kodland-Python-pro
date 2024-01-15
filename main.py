import time
meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "Leggera disapprovazione",
            "CREEPY": "Spaventoso, inquietante",
            "PARA": "Preoccuparsi per qualcosa, paranoiarsi",
            "BTW": "By The Way (Ad ogni modo, comunque)",
            "FR": "For Real (Per davvero, vero)",
            "RIZZ": "Accorciamento di caRISma (caRIZZma)",
            "LMAO": "Laughing My Anxiety/Arms/Apples Off (intensa risata)",
            "ROTFL": "Rolling On The Floor Laughing (intensa risata)",
            
            }
            
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
if parola in meme_dict.keys():
    print(meme_dict.get(parola))
else:
    print("Parola non trovata!")
    
