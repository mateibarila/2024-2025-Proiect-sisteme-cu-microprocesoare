Titlu proiect: Sistem de avertizare la apropiere, controlat prin rețea

Motivația alegerii temei: Am ales această temă deoarece îmbină mai multe concepte esențiale din domeniul sistemelor embedded și al Internetului Lucrurilor (IoT), oferind o aplicație practică de monitorizare și semnalizare automată a distanței.
Totodată, tema are aplicabilitate directă în sisteme reale, cum ar fi:
•	sisteme de parcare asistată;
•	detectarea prezenței într-o zonă;
•	semnalizarea riscurilor în spații restrânse;

Rezumat:
Proiectul propune implementarea unui subsistem embedded destinat detecției și semnalizării proximității, utilizând un senzor ultrasonic HC-SR04 pentru măsurarea cu un interval de eșantionare de aproximativ o secundă a distanței față de un obstacol. În funcție de pragurile configurabile din interfața web, sistemul declanșează mecanisme de feedback acustic (buzzer activ) și vizual (LED-uri RGB), corespunzător nivelurilor de avertizare. De asemenea, sistemul oferă un mod manual de control, accesibil prin interfața web, care permite utilizatorului să activeze sau să dezactiveze semnalizarea acustică și vizuală independent de valorile măsurate.

Importanța/Utilitatea  în domeniul Embedded System-SM:
Proiectul se înscrie în sfera subsistemelor de tip embedded cu rol de detecție și semnalizare automata a proximității, având o valoare practică ridicată și demonstrând mai multe concepte cheie ale ingineriei embedded.
 
Utilitatea sa se regăsește în multiple industrii:
•	Sisteme de parcare asistată și evitarea coliziunilor (auto și robotică)
•	Controlul accesului și siguranța prin monitorizarea obiectelor sau persoanelor în medii sensibile

Scalabilitate și adaptabilitate:
Sistemul poate fi extins cu ușurință pentru a 
•	include mai mulți senzori;
•	pentru a trimite notificări prin internet; 
•	pentru a controla alte echipamente;

Analiză - design - implementare:
•	Analiză
În etapa de analiză, s-a urmărit identificarea nevoii unui sistem embedded capabil să detecteze distanța față de un obiect și să semnalizeze vizual și acustic pe baza unor praguri definite de utilizator utilizând un senzor ultrasonic HC-SR04  și afișarea unei interfețe web pentru configurarea parametrilor de funcționare.

•	Design-ul arhitecturii sistemului
Proiectul este structurat modular, cu următoarele componente principale hardware:
•	Senzor ultrasonic (HC-SR04) – pentru detectarea distanței;
•	Microcontroler Raspberry Pi Pico 2W – care procesează datele, controlează ieșirile și găzduiește interfața web;
•	Ieșiri de semnalizare (LED roșu, LED galben, buzzer activ) – acționate în funcție de distanțele detectate și pragurile stabilite; 
Pe partea de software, designul implică
•	Interfață web – permite introducerea valorilor prag pentru LED-uri cât și comutarea în mod manual, unde utilizatorul poate aprinde/stinge LED-ul roșu și buzzerul printr-un simplu acces la o resursă web.
 
•	Implementare
Implementarea a fost realizată în limbajul MicroPython, utilizând funcționalitățile bibliotecilor integrate pentru:
•	Controlul pinilor digitali (intrări/ieșiri);
•	Gestionarea conexiunii Wi-Fi în mod Access Point (AP);
•	Inițializarea unui server HTTP local;
•	Procesarea cererilor POST pentru a prelua pragurile introduse de utilizator;
Funcțiile au fost separate în module logice:
•	citeste_distanta() – citește datele de la senzor și returnează valoarea în cm;
•	mod_automat() – declanșează acțiunile de semnalizare pe baza distanței;
•	mod_manual(cerere) – funcție care controlează semnalizarea acustică și vizuală în mod direct, pe baza cererilor primite de la utilizator
•	Serverul HTTP – gestionează conexiunea și interfața cu utilizatorul.

Ce se învață dacă se replica proiectul:
1.	Citirea senzorilor cu precizie: Această noțiune presupune interpretarea corectă a semnalelor digitale provenite de la senzori externi. Astfel, se dobândește o înțelegere practică a modului în care se obține și se interpretează o valoare fizică (distanța) într-un sistem digital.
2.	Crearea unui server web pe un microcontroler: Prin utilizarea funcționalităților de rețea ale microcontrolerului Pico W, se creează un server HTTP local care răspunde la cereri din partea unui browser. Acest server generează o interfață HTML simplă, care permite trimiterea de date către dispozitiv (prin metode POST), simulând astfel un control IoT de tip client-server.
3.	Gestionarea feedbackului vizual și sonor în funcție de condiții variabile: În acest proiect, LED-urile și buzzer-ul sunt activate sau dezactivate în funcție de valorile măsurate și de pragurile setate de utilizator. Se exersează astfel noțiuni de control digital (ON/OFF) și temporizare.
4.	Control direct al echipamentelor prin web – Se dobândește experiență practică în dezvoltarea unei interfețe web care permite activarea/dezactivarea ieșirilor digitale prin comenzi directe, fără procesare logică intermediară.

Prezentare:
![image](https://github.com/user-attachments/assets/d3ad5601-ec6b-454e-8aa2-a4c249e7a33d)
![image](https://github.com/user-attachments/assets/31bfdb0f-f439-4c35-8787-1e071fc8ca0c)

Interfața web:
![image](https://github.com/user-attachments/assets/3074abb7-ab63-49b7-b2e4-8f58790cf764)

Bibliografie:
https://randomnerdtutorials.com/raspberry-pi-pico-w-wi-fi-micropython/
https://forums.raspberrypi.com/viewtopic.php?t=336901
https://www.freva.com/hc-sr04-ultrasonic-sensor-on-raspberry-pi/?srsltid=AfmBOoprdY3Fo2DVFMkK6o1aXRXy2K7N8Fzc7d3kcD9QkZx42j1YpMCW
