import streamlit as st
import random


st.title("Zahlenratespiel mit Streamlit")
#st.header("Zahlenratespiel")

#Sielerklärung
st.write('Bei diesem Spiel "denkt" sich der Computer eine ganze Zahl zwischen 1 und 100!')
st.write('Deine Aufgabe besteht darin, die Zahl zu erraten.\nEs geht los:')

#Anzahl Rateversuche
maxVersuche=int(7)
#st.write("Du hast maximal",maxVersuche,"Rateversuche!")

#Zufallszahl
# Geheime Zahl nur einmal pro Session erzeugen und dann in Ruhe lassen
if "zahlgeheim" not in st.session_state:
    st.session_state.zahlgeheim = random.randint(1, 100)
st.write("Der Computer hat sich eine Zahl gemerkt ...")

# Variable anzahlversuche nur einmal pro Session mit 0 belegen
if "anzahlversuche" not in st.session_state:
    st.session_state.anzahlversuche = int(0)

# Optional: Debug-Ausgabe
st.write("DEBUG, geheime Zahl:", st.session_state.zahlgeheim)



# Ein Formular für die Auswertung:
with st.form(key='mein_formular'):
	#st.write("### Zahl wählen")
	rateversuch=st.number_input("Bitte eine Zahl wählen oder eingeben:  ",min_value=1,max_value=100,step=1)
	
	# Der Submit-Button MUSS innerhalb des Formulars sein
	submit_button = st.form_submit_button(label='Absenden')
	
	if submit_button:
		if st.session_state.anzahlversuche==maxVersuche-1 and st.session_state.zahlgeheim != rateversuch:
			st.error("Das war der siebte und letzte Rateversuch!")
			st.write("Die gesuchte Zahl lautet:",st.session_state.zahlgeheim)
			
		elif st.session_state.zahlgeheim == rateversuch:
			st.success("Juchuuuu: Du hast die Zahl erraten!")
			st.session_state.anzahlversuche=st.session_state.anzahlversuche+1
			st.write("Du hast es im",st.session_state.anzahlversuche,". Rateversuch geschafft, die Geheimzahl zu erraten! :sunglasses:")
		elif st.session_state.zahlgeheim < rateversuch:
			st.warning("Diese Zahl ist zu groß!")
			st.session_state.anzahlversuche=st.session_state.anzahlversuche+1
			st.write("Das war der",st.session_state.anzahlversuche,". Rateversuch!")
		elif st.session_state.zahlgeheim > rateversuch:
			st.warning("Diese Zahl ist zu klein!")
			st.session_state.anzahlversuche=st.session_state.anzahlversuche+1
			st.write("Das war der",st.session_state.anzahlversuche,". Rateversuch!")
