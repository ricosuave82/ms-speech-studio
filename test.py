'''
  For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk 
'''

import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
speech_key = "af345a47df294d35a762eec805cf2c90"
service_region = "uksouth"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.endpoint_id = "67c079f8-d810-4389-a980-e88c7c3a0270"
speech_config.speech_synthesis_voice_name = "Caroline clone 1Neural"

text_full = '''
Hallo allemaal, wat leuk dat ik deze keer de blog mag verzorgen. 
Binnen generieke software services, ontwikkelen we en beheren we veel applicaties die door heel het bedrijf worden gebruikt.
En dat is ook meteen het bijzondere en interessante van wat we doen. 
We hebben te maken met alle labels en lagen van ons mooie bedrijf, en We moeten zoveel mogelijk voldoen aan alle wensen en eisen, terwijl de kwaliteit en de Generiekheid van onze IT gewaarborgd blijft. 
Om alle componenten zo generiek mogelijk te houden, wordt dan ook veel aan innovatie gedaan. 
Een goed voorbeeld daarvan is conversational AI.
'''

text_full = '''
Onder conversational AI wordt technologie bedoeld, waarmee we AI direct met Mensen Laten communiceren, zoals Chatbots en Voice Bots. 
AI stelt ons in staat om de applicatie verzekerings taal te leren door een taalmodel te trainen. 
En door die training is AI ook in staat om de werkelijke bedoeling van de vraagsteller vast te stellen, oftewel de intent te herkennen. 
Een op zichzelf staande zin kan leiden tot een heel ander antwoord dan Als je deze In de context van een gesprek bekijkt. 
Conversational AI is in staat om die context dynamisch mee te nemen bij het formuleren van een antwoord. 
Dus bijvoorbeeld een vraag: is mijn auto tegen inbraak schade verzekerd? 
Leidt zeer waarschijnlijk tot een ander antwoord dan: gisteren heb ik mijn auto met de deuren open In het midden van de stad achtergelaten. Is mijn auto tegen inbraak schade verzekerd? 
Conversational AI helpt ons dan ook om het juiste antwoord te geven, met inachtneming van alle context. 
'''

text_full = '''
En wel zo, dat de bot zich aanpast naar de manier waarop de klanten informatie geeft, ook wel non lineair genoemd. 
Dat betekent dat de bot stap voor stap alle benodigde informatie af vinkt, die nodig is om een antwoord te formuleren en je niet onnodig in een keurslijf dwingt. 
Als je in één zin al de helft van de benodigde informatie geeft, gaat de bot daar niet meer om vragen. 
In de traditionele bots moet dit nog wel worden gedaan. 
Verzekeraars moeten daar zijn waar hun klanten zijn, en klanten zijn steeds vaker te vinden op allerlei digitale kanalen. 
Met behulp van conversational ai, kan achmea 24 7 bereikbaar zijn voor onze klanten, en deze techniek is ook erg makkelijk schaalbaar voor bijvoorbeeld eindejaars campagnes, of andere momenten waarop pieken in communicatie ontstaan, 
zoals bijvoorbeeld herfststormen.
''' 

text_full = '''
Tegelijkertijd draagt de bot zorg voor consistente informatievoorziening naar de klant, en is de wachttijd drastisch lager. 
Binnen Achmea is conversational AI momenteel in gebruik bij centraal beheer, de AI chatbot CB, Interpolis, de AI Chatbot Interpolis virtueel assistent, en zilveren Kruis met zoey. 
Ontwikkelingen gaan snel op AI gebied. Alle grote tech leveranciers zijn hiermee bezig. 
Een Microsoft CEO zei onlangs, Bots zijn de nieuwe applicaties, en digitale assistenten zijn de nieuwe browsers. 
De belangrijkste themas waar we nu aan werken zijn: automatische klant identificatie, zodat we toegespitst op de individuele klant conversaties kunnen voeren, en het uitbreiden van de ai bot naar het voice kanaal, en het aansluiten van de bot op whatsapp en appchat. 
'''

text_full = '''
Ons doel is om uiteindelijk de bot in staat te stellen om een volledig en volwassen gesprek te Laten voeren met de klant, inclusief het verwerken van transacties in andere applicaties. 
Denk hierbij aan het registreren van een claim, het helpen maken van een afspraak bij een schadeherstelbedrijf, of het verrichten van een betaling. 
En daarbij blijven we uiteraard ook voldoen aan alle wet en regelgeving. 
En Dit is maar een van de voorbeelden binnen de IT keten generieke software services. 
Er zijn nog veel meer technieken waar we je over kunnen vertellen, en Als je daar meer van wil weten of je hebt andere vragen, dan nemen we graag de tijd om met je hierover in gesprek te gaan!  
'''

text_full = '''
En nu voor een kleine plotwending: deze video is volledig gegenereerd met behulp van AI. Ik heb er niets van gezegd, het is een kunstmatige stem die door ons team is gemaakt. 
De video wordt gesynchroniseerd met deze stem met behulp van een lipsynchronisatietechnologie. Heb je iets verdachts opgemerkt toen je dit zag? Binnenkort meer nieuws over dit onderwerp!”
'''

# text_full = '''
# Ik denk dat we meer met why Digital moeten doen. 
# Deze jongens zijn gewoon briljant en we zullen heel ver komen met hun steun. 
# Geef ze alsjeblieft al het geld dat ze nodig hebben.
# '''

text_full = "en zilveren Kruis met Zoë"

file_name = "zoe2.wav"

# using the default speaker as audio output.
file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)

result = speech_synthesizer.speak_text_async(text_full).get()
# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(text_full, file_name))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))