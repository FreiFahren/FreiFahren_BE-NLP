test_cases = [
    (
        'heinrich-heine zwei blauwesten',

        'Heinrich-Heine-Straße',

        None,
        None
    ),
    (
        'U6 Schumacher-Platz 2 Controller merhingdam',

        'Mehringdamm',

        'U6',

        None,
    ),
    (
        '2x Hellblau U8 Hermannplatz Richtung Wittenau am Bahnsteig',

        'Hermannplatz',

        'U8',

        'Wittenau',

    ),
    (
        'U8 pankstrasse 2 Blau veste',

        'Pankstraße',

        'U8',

        None
    ),
    (
        '2 Kontrolleure U9 Richtung Osloer Straße',

        None,
        'U9',

        'Osloerstraße'
    ),
    (
        'Und zwei Cops oben am Bahnsteig der SBahn',

        None,
        None,
        None
    ),
    (
        'U 8 Heinrich Heine str',

        'Heinrich-Heine-Straße',

        'U8',

        None
    ),
    (
        'Friedrichstrasse bei der u6 waren gerade zwei mit bos westen',

        'Friedrichstraße',

        'U6',

        None,
    ),
    (
        '2personen dunkel blaue weste',

        None,
        None,
        None
    ),
    (
        'U2 Ernst Reuter Platz',

        'Ernst-Reuter-Platz',

        'U2',

        None
    ),
    (
        'U9 4 (oder mehr) blauwesten auf Gleis Spichernstraße',

        'Spichernstraße',

        'U9',

        None,
    ),
    (
        'Zwei Stück Richtung Osloer',

        None,
        None,
        'Osloerstraße'
    ),
    (
        'Jetzt Zoo in der Bahn richtung Steglitz!',

        'Zoologischer Garten',

        None,
        'Rathaus Steglitz',

    ),
    (
        '''U6 Mehringdamm -> hallesches Tor gerade ausgestiegen. 2 Kontrolleure
        in schwarz,glaube ich. :''',

        'Hallesches Tor',

        None,
        None,
    ),
    (
        '''S Alexanderplatz west direction at least one ticket checker with
        a white puffer jacket on the platform''',

        'Alexanderplatz',

        None,
        None,
    ),
    (
        'u6 leopoldplatz towards alt mariendorf 2 people with 2 cops',

        'Leopoldplatz',

        'U6',

        'Alt-Mariendorf',

    ),
    (
        'u6 paradestraße ausgestiegen.',

        'Paradestraße',

        None,
        None
    ),
    (
        'M10 towards turmstr. two guys with no uniform',

        None,
        'M10',

        'Turmstraße',

    ),
    (
        'U boddinstrasse. 5 securitys / 3 cops',

        'Boddinstraße',

        None,
        None
    ),
    (
        'Gerade S Tiergarten Richtung zoo',

        'Tiergarten',

        None,
        'Zoologischer Garten',

    ),
    (
        'Walther Schreiber Platz U9 Richtung Rathaus Steglitz Kontrolletis',

        'Walther-Schreiber-Platz',

        'U9',

        'Rathaus Steglitz',

    ),
    (
        '2 in schwarz S tempelhof',

        'Tempelhof',

        None,
        None
    ),
    (
        'Grad ausgestiegen s41',

        None,
        None,
        None
    ),
    (
        '''S7,2 männlich gelesene in zivil grad Friedrichstraße
        mit jemandem ausgestiegen''',

        'Friedrichstraße',

        None,
        None,
    ),
    (
        'Ring zwischen S Tempelhof und S Hermannstraße',

        'Tempelhof',

        None,
        None
    ),
    (
        'U2 Märkisches Museum richtung ruhleben 3 Männer mit B.O.S Jacken',

        'Märkisches Museum',

        'U2',

        'Ruhleben',

    ),
    (
        'Ring Bahn Hohenzollerndamm vor 2 Minuten eine Person alleine',

        'Hohenzollerndamm',

        None,
        None,
    ),
    (
        '''S1 Richtung Spindersfeld,männlich gelesen gerade
        bei hermannstraße geht durch die Bahn''',

        'Hermannstraße',

        'S1',

        'Spindlersfeld',

    ),
    (
        'S1 nach spindlersfelde war ein am hermannplatz oder vorher',

        'Hermannplatz',

        'S1',

        'Spindlersfeld',

    ),
    (
        'U8 Wittenau sind U Jannowitzbrücke raus',

        'Jannowitzbrücke',

        None,
        None,
    ),
    (
        'messe nord grad raus',

        'Messe Nord/ICC',

        None,
        None
    ),
    (
        '3x weiblich jetzt westkreuz ina s41',

        'Westkreuz',

        'S41',

        None
    ),
    (
        'Kontrolle in s42 jetzt Treptower Park',

        'Treptower Park',

        'S42',

        None
    ),
    (
        'Kontrolle auf der Strecke u9',

        None,
        'U9',

        None
    ),
    (
        'BOS Alex u8 on the platform',

        'Alexanderplatz',

        'U8',

        None
    ),
    (
        'A lot of bvg and cops,outside,at Hermanplatz',

        'Hermannplatz',

        None,
        None,
    ),
    (
        '''3x m gelesen 1x w gelesen am hermannplatz Gleis u8 Richtung
        hermannstraße blaue bos jacken''',

        'Hermannplatz',

        'U8',

        'Hermannstraße',

    ),
    (
        'S42 greiswalder strasse2 Männer 1 frau',

        'Greifswalderstraße',

        'S42',

        None,
    ),
    (
        '''Ring zwischen Hohenzollerndamm und Halensee. 3x weiblich gelesen,
        davon 1x weiße Jacke,1x schwarz glänzende Jacke''',

        'Hohenzollerndamm',

        None,
        None,
    ),
    (
        '''2 Kontrolleure read male black outfits black beards in S8
        to Ostkreuz,now Storkower Str got off at Storkower Straße''',

        'Storkowerstraße',

        None,
        None,
    ),
    (
        '''S41 gleich Tempelhof. Ein Typ,eine Frau. Beide schwarze Kapuzenjacke.
        Er mit North Face Mütze schwarz,Sie mit langen blonden Haaren''',

        'Tempelhof',

        'S41',

        None,
    ),
    (
        '''U6 steigen gerade Wedding ein Richtung alt mariendorf
        im hinteren Teil der Bahn 3m blaue Jacken''',

        'Wedding',

        'U6',

        'Alt-Mariendorf',

    ),
    (
        '''Kontrolleur m gelesen S2 Frohnau jetzt Halensee In zivil,schwarze
        Jacke,schwarze Haare,braune Ledertasche''',

        'Halensee',

        'S2',

        'Frohnau',

    ),
    (
        'Jannowitzbrücke U8',

        'Jannowitzbrücke',

        'U8',

        None
    ),
    (
        'S42 Tempelhof ein Mann und eine Frau mit langen blonden Haaren.',

        'Tempelhof',

        'S42',

        None,
    ),
    (
        'S41 tempelhof',

        'Tempelhof',

        'S41',

        None
    ),
    (
        '''U6 Friedrichstrasse direction north,K.Schumacher platz,
        3 mannlich gelesen mit B.O.B. jackets''',

        'Friedrichstraße',

        'U6',

        'Kurt-Schumacher-Platz',

    ),
    (
        '2 männer S42 Treptower park',

        'Treptower Park',

        'S42',

        None
    ),
    (
        'S41 in Storkowerstr Richtung Ostkreuz',

        'Storkowerstraße',

        'S41',

        'Ostkreuz',

    ),
    (
        '2 civil controllis in s 41 to landsberger',

        None,
        'S41',

        'Landsberger Allee',

    ),
    (
        'Three female kontrolettis in the S42 soon to be Bundesplatz',

        'Bundesplatz',

        'S42',

        None,
    ),
    (
        'S45 Flughafen BER',

        'Flughafen BER',

        'S45',

        None
    ),
    (
        '''Sind jetzt jungfeenheide. 1 x mal männlich und 1x mal weiblich
        gelesen komplett in schwarz''',

        'Jungfernheide',

        None,
        None,
    ),
    (
        'S8 Ostkreuz',

        'Ostkreuz',

        'S8',

        None
    ),
    (
        '''Controller in S7 Richtung Alexanderplatz
        Was just checked in jannowitzbrucke''',

        'Jannowitzbrücke',

        'S7',

        'Potsdam Hauptbahnhof',

    ),
    (
        '''S42 Landsberger Alle,2m,schwarze Jacke,schwarze Mütze. 2 m mit
        Gelber Weste begleiten.''',

        'Landsberger Allee',

        'S42',

        None,
    ),
    (
        '3 Kontrolleure s Greifswalder',

        'Greifswalderstraße',

        None,
        None
    ),
    (
        'S8 Greifswalder Straße',

        'Greifswalderstraße',

        'S8',

        None
    ),
    (
        'S41 Ringbahn Landsberger allee big group of kontrolettis',

        'Landsberger Allee',

        'S41',

        None,
    ),
    (
        '''Ring 41-> Landsberger Allee,glaube mehrere
        männer die auch Minderjährige hochnehmen''',

        'Landsberger Allee',

        'S41',

        None,
    ),
    (
        'S42,3x agressiv männlich,gerade Schönhauser ausgestiegen',

        'Schönhauser Allee',

        None,
        None,
    ),
    (
        'Ring s42  approaching geundbrunnen civil control',

        'Gesundbrunnen',

        'S42',

        None,
    ),
    (
        '5 Kontrolleure S8 to Birkenwerder',

        None,
        'S8',

        'Birkenwerder'
    ),
    (
        'U8 heinrrich heinest blue vest at platform',

        'Heinrich-Heine-Straße',

        'U8',

        None,
    ),
    (
        'Friedrichstraße',

        'Friedrichstraße',

        None,
        None
    ),
    (
        '''Spichernstraße U3 am Bahnsteig eine Person männl gelesen,komplett
        schwarz angezogen mit braunem undercut,ca 30 Jahre.. wirkt aber sehr
        nett weil er grad jemand erklärt wie er das Ticket einer anderen Person
        nachreichen kann''',

        'Spichernstraße',

        'U3',

        None,
    ),
    (
        '2x Blauwesten u8 Heinrich Heine straße Richtung Hermannstraße',

        'Heinrich-Heine-Straße',

        'U8',

        'Hermannstraße',

    ),
    (
        '''Bitte hier keine Fragen,ob diese oder jene Linie gerade frei ist,
        sondern stattdessen die Suchfunktion (das Lupensymbol) nutzen. Danke!
        Nachricht gelöscht.''',

        None,
        None,
        None,
    ),
    (
        '''Two men wearing normal clothes in M5,checking tickets,just
        got off at alexanderplatz''',

        'Alexanderplatz',

        None,
        None,
    ),
    (
        '''U1 at hallesches tor towards warschauer str.
        2 maybe 3 blue wests giving fines''',

        'Hallesches Tor',

        'U1',

        'Warschauer Straße',

    ),
    (
        '''Wenn mein Infopost über die Demo am Sonntag Nachmittag gegen Rechts
        als Spam gewertet wird (über die ja auch im Bild der Gruppe informiert
        wird) würde ich mir eine kurze Rückmeldung von euch darüber wünschen''',

        None,
        None,
        None,
    ),
    (
        '''No basically this is the decision of the admins who run this group
        because we share certain values and leftist politics. If you happen to
        dislike actions against fascists,its you who might not belong in this
        group. Like Spam.''',

        None,
        None,
        None,
    ),
    (
        'S41 Treptower Park,2 Männer',

        'Treptower Park',

        'S41',

        None
    ),
    (
        'U1 hallesches tor in der bahn richtung westen',

        'Hallesches Tor',

        'U1',

        'Uhlandstraße',

    ),
    (
        '''s7 nach Ahrensfelde 3 Männer schwarze jacken
        hackescher markt ausgestiegen''',

        'Hackescher Markt',

        None,
        None,
    ),
    (
        'Ring S41 Sonnenallee Richtung Neukölln',

        'Sonnenallee',

        'S41',

        None
    ),
    (
        'U6 friedrichstr',

        'Friedrichstraße',

        'U6',

        None
    ),
    (
        'S42 two guys at frankfurterallee',

        'Frankfurter Allee',

        'S42',

        None
    ),
    (
        'Alexanderplatz an Gleis der u8 hellblaue westen',

        'Alexanderplatz',

        'U8',

        None,
    ),
    (
        '4x männlich gelesen S42 aktuell Landsbegwr immer noch im Zug',

        'Landsberger Allee',

        'S42',

        None,
    ),
    (
        'Alexanderplatz sbahn platform',

        'Alexanderplatz',

        None,
        None
    ),
    (
        '41 wedding. Grun mantel',

        'Wedding',

        'S41',

        None
    ),
    (
        '''Ostbahnhof 8 Bundesbullen stehen an der Bahnsteigkante.
        Alle mit gelben Westen. Keine Ahnung ob die eingestiegen sind.''',

        'Ostbahnhof',

        None,
        None,
    ),
    (
        'Ostkreuz 6 Polizisten kontrollieren Ausweise willkürlich',

        'Ostkreuz',

        None,
        None,
    ),
    (
        'U6 Unter den Linden',

        'Unter den Linden',

        'U6',

        None
    ),
    (
        '''unter den Linden,U6,Richtung Tegel,
        eine m gelesene Person mit blauer wrtse''',

        'Unter den Linden',

        'U6',

        'Tegel',

    ),
    (
        '''U6 Richtung alt Mariendorf Stadtmitte eingestiegen
        2 blauwesten m gelesen''',

        'Stadtmitte',

        'U6',

        'Alt-Mariendorf',

    ),
    (
        'U8 Hermannstr,just saw police + BVG going downstairs from the street',

        'Hermannstraße',

        'U8',

        None,
    ),
    (
        'U8 Hermannstraße',

        'Hermannstraße',

        'U8',

        None
    ),
    (
        'S42 Hermanstraße ,2x schwarze Jacken',

        'Hermannstraße',

        'S42',

        None
    ),
    (
        'S25 S Hennigsdorf a least 2Pers.',

        'Hennigsdorf',

        'S25',

        None
    ),
    (
        '3 Blauwesten Ubhf Heinrich Heine Str',

        'Heinrich-Heine-Straße',

        None,
        None,
    ),
    (
        '''U3 freie Universität stehen blau Westen. Sie werden wohl die nächste
        Bahn in die Innenstadt nehmen''',

        'Freie Universität (Thielplatz)',

        'U3',

        None,
    ),
    (
        'U8 rosenthaler Richtung hermanstr',

        'Rosenthaler Platz',

        'U8',

        'Hermannstraße',

    ),
    (
        'M27 Pankstr Richtung Jungfernheide',

        'Pankstraße',

        'M27',

        'Jungfernheide',

    ),
    (
        'U2 From Alex to Ruhleben now bunch of them in a wagon',

        'Alexanderplatz',

        'U2',

        'Ruhleben',

    ),
    (
        '''3 mänlich gelesene 2 mit gelben westen 1 mit blauer bos weste alex
        u8 richtung wittenau''',

        'Alexanderplatz',

        'U8',

        'Wittenau',

    ),
    (
        'About to get off s8 Prenzlauer Allee',

        'Prenzlauer Allee',

        None,
        None
    ),
    (
        'M29 two men,to Halensee',

        None,
        'M29',

        'Halensee'
    ),
    (
        's47 nach spindlerfeld s tempelhof eingestiegen 2 in zivil',

        'Tempelhof',

        'S47',

        'Spindlersfeld',

    ),
    (
     's-bahn kontrolleure friedrichstrasse 2mal weiblich eine kräftig und blonde haare lang andere dünner grüne jacke',
     'friedrichstrasse',
     None, None) ,
    (
     '4 Kontrolleur*innen S85 nach Buch',
     None, 'S85',
     'Buch') ,
    (
     'Sind nicht zu übersehen 😅',
     None, None, None) ,
    (
     'U5 nach Hönow',
     None, 'U5',
     'Hönow') ,
    (
        'Blaue veste',
        None, None, None) ,
    (
     'S42 grade landsbergeralee los',
     'landsbergeralee',
     'S42',
     None) ,
    (
     'froilein rattenmeier sie/shehey kurze frage: der kontroletti hat meinen namen falsch geschrieben, adresse stimmt aber. kann das ...Wenn deine Ausweisnummer stimmt finden die dich überall in der EU außer in Rumänien 😬',
     None, None, None) ,
    (
     'FlinnUnd wenn er den Namen hat aber nicht die Adresse?Die Ausweisnummer bzw das Personaldokument worüber sie dich aufgenommen haben ist entscheidend',
     None, None, None) ,
    (
     'zwei bos westen mit gelbem nacken sind gerade schönleinstr u8 richtung hermannstr eingestiegen',
     'schönleinstr',
     'u8',
     'hermannstr') ,
    (
     '3 bos u8 richtung wittenau, weinmeisterstr ausgestiegen',
     'weinmeisterstr',
     'u8',
     'wittenau') ,
    (
     'Große Kontrolle beim aussteigen an der U-Alt-Tempelhof U6',
     'U-Alt-Tempelhof',
     'U6',
     None) ,
    (
     'Ring, tempelhof, richtung sudkreuz',
     'tempelhof',
     'Ring',
     'sudkreuz') ,
    (
     'u8 Voltastr.',
     'Voltastr',
     'u8',
     None) ,
    (
     'mind. 2 blaue westen am leopoldplatz, polizei ist auch da, am u9 gleis',
     'leopoldplatz',
     'u9',
     None) ,
    (
     'Neukölln  sbahn 2 männlich gelesene',
     'Neukölln',
     None, None) ,
    (
     'Lazi ♀️Neukölln  sbahn 2 männlich geleseneBeide glatze',
     '♀️Neukölln',
     None, None) ,
    (
     'Jetzt noch zusätzlich zwei weitere steigen von s41 aus in Tempelhof',
     'Tempelhof',
     's41',
     None) ,
    (
     '2 Männer mit blauen Westen stiegen in die U8 Richtung Witteneu @ Henrich-Heine-Straße ein',
     'Henrich-Heine-Straße',
     'U8',
     'Witteneu') ,
    (
     'S7 Richtung potsdam Hbf, 3 w gelesen, gleich griebnitzsee',
     'griebnitzsee',
     'S7',
     'potsdam Hbf') ,
    (
     'u5 straußberger Richtung hönow',
     'straußberger',
     'u5',
     'hönow') ,
    (
     'u7 Richtung spandau. Drei Mal in BVG Uniform. Gerade hermannplatz',
     'hermannplatz',
     'u7',
     'spandau.') ,
    (
     'S85 Plänterwald Richtung Grünau',
     'Plänterwald',
     'S85',
     'Grünau') ,
    (
     '4x in Zivil, schwarze Jacken',
     None, None, None) ,
    (
     'gibts ein updare zur u7?',
     None, None, None) ,
    (
     '⁃ Bitte keine Fragen ob eine Linie bzw. ein Ort frei ist. Alle gesichteten Kontrollen sollten hier stehen.',
     None, None, None) ,
    (
     'Mehr Infos sind in der angehefteten Nachricht.',
     None, None, None) ,
    (
     'Für Fragen gibt es die @Diskussionsgruppe.TelegramA in Freifahren_BE🚂 \u206d Initiative gegen Ticketpflicht im ÖPNV 🚂',
     None, None, None) ,
    (
     '(english version below)',
     None, None, None) ,
    (
     'Bitte helft mit und schreibt kurz, wenn ihr Kontrollen seht oder erlebt, Fehlve...VIEW MESSAGE',
     None, None, None) ,
    (
     'U6, Alt-Tempelhof, gemischt in Zivil und mit BVG-Jacke.',
     'Alt-Tempelhof',
     'U6',
     None) ,
    (
     'U6, Paradestraße Richtung Kurt-Schumacher-Platz, BVG zusammen mit Polizei. Mind. zu sechst.',
     'Paradestraße',
     'U6',
     'Kurt-Schumacher-Platz') ,
    (
     'M29er Richtung hermannplatz, wurde bereits mehrmals kontrolliert während der Fahrt. Sind erkennbar an prüferjacken',
     None, 'M29er',
     'hermannplatz') ,
    (
     'Jetzt U9 Hansaplatz Richtung Osloer',
     'Hansaplatz',
     'U9',
     'Osloer') ,
    (
     'S41 Hermannstr eingestiegen, 3 Männer 2 in schwarzer 1 in brauner Jacke',
     'Hermannstr',
     'S41',
     None) ,
    (
     '1x Braun lilane North face Jacke, kurze schwarze haare, männlich gelesen',
     None, None, None) ,
    (
     '1x schwarze Jacke, schwarze kurze haare, bisschen Bart',
     None, None, None) ,
    (
     '',
     None, None, None) ,
    (
     'Kommen grade mit s41 von hermannstraße nach Tempelhof an',
     'Tempelhof',
     's41',
     None) ,
    (
     'Nicolas Sidiropulos1x Braun lilane North face Jacke, kurze schwarze haare, männlich gelesen',
     None, None, None) ,
    (
     '1x schwarze Jacke, schwarze...Waren 3',
     None, None, None) ,
    (
     'Einer hat nen kleinen Dutt und ne brille',
     None, None, None) ,
    (
     'U8 Rosenthaler Platz',
     'Rosenthaler Platz',
     'U8',
     None) ,
    (
     'M4 alexanderplatz',
     'alexanderplatz',
     'M4',
     None) ,
    (
     'Richtung hackeischet markt',
     None, None, 'hackeischet markt') ,
    (
     '2 blaue Westen U9 Richtung Steglitz ',
     None, 'U9',
     'Steglitz') ,
    (
     'am u amruner str ausgestiegen',
     'amruner str',
     None, None) ,
    (
     '3 Männer  U6 - Alt-Tempelhof',
     'Alt-Tempelhof',
     'U6',
     None) ,
    (
     'Stehen Richtung Zoo',
     None, None, 'Zoo') ,
    (
     'U7 rudow direction, richard wagner platz, 2 blue vests',
     'rudow',
     'U7',
     'richard wagner platz') ,
    (
     'Three in civil at invalidenpark entering m10 direction warschauer',
     'invalidenpark',
     'm10',
     'warschauer') ,
    (
     'U2 nollendorfplatz richtung ruhleben',
     'nollendorfplatz',
     'U2',
     'ruhleben') ,
    (
     'Polizei boddinstrasse',
     'boddinstrasse',
     None, None) ,
    (
     'U5 Alexanderplatz am Gleis richtung HBF 2 Blauwesten',
     'Alexanderplatz',
     'U5',
     'HBF') ,
    (
     'U6 Seetr. Richtung Alt. Mariendorf :  Bullen und BVG Security stressen Obdachlose',
     None, 'U6',
     'Alt. Mariendorf') ,
    (
     'Ring Neukölln, two man with yellow shirt. S41 right now',
     'Neukölln',
     'S41',
     None) ,
    (
     'Osloer Str U9',
     'Osloer Str',
     'U9',
     None) ,
    (
     'nuxU5 Alexanderplatz am Gleis richtung HBF 2 BlauwestenUff-Basse !',
     'Alexanderplatz',
     'nuxU5',
     'HBF') ,
    (
     'U7 Wilmersdorfer str richtung Rudow',
     'Wilmersdorfer',
     'U7',
     'Rudow') ,
    (
     '2männer in blau',
     None, None, None) ,
    (
     'Ringbahn S41 jetzt gleich Tempelhof',
     'Tempelhof',
     'S41',
     None) ,
    (
     'U8 Richtung hermannstraße',
     None, 'U8',
     'hermannstraße') ,
    (
     'Just got out there standing on the platform Bernauer Straße',
     'Bernauer Straße',
     None, None) ,
    (
     'Sind ausgestiegen Bernauer Straße',
     'Bernauer Straße',
     None, None) ,
    (
     'U7 Wilmersdorfer str richtung rudow standing on the platform, 4 men wearing blue vests',
     'Wilmersdorfer str',
     'U7',
     'rudow') ,
    (
     'Stephen MarcalanRingbahn S41 jetzt gleich TempelhofWie sehen die aus?',
     'TempelhofWie',
     'S41',
     None) ,
    (
     'U8 Bernauerstr richtung Hermannstr, 3 Blauevesten',
     'Bernauerstr',
     'U8',
     'Hermannstr') ,
    (
     'Drei am Bahnhof Zoo, U9 Richtung Rathaus Steglitz',
     'Zoo',
     'U9',
     'Rathaus Steglitz') ,
    (
     'Riesen Gruppe mit bos Jacken mitten auf Bahnsteig rosenthalerplatz',
     'rosenthalerplatz',
     None, None) ,
    (
     '2bos mehringdamm am gleis u7/u6',
     'mehringdamm',
     'u7/u6',
     None) ,
    (
     'Diese Leute am Moritzplatz. nicht Kontrolleur(?)',
     'Moritzplatz.',
     None, None) ,
    (
     'Mehringdamm jetzt viele',
     'Mehringdamm',
     None, None) ,
    (
     'dumbass óskPhoto, Diese Leute am Moritzplatz. nicht Kontrolleur(?)Manchmal ja manchmal nein',
     'Moritzplatz.',
     None, None) ,
    (
     'U7 direction Rudow Gneisenaustrasse',
     'Gneisenaustrasse',
     'U7',
     'Rudow') ,
    (
     'JaumeU7 direction Rudow GneisenaustrasseSind auf dem Gleis dort',
     None, 'GneisenaustrasseSind',
     'Rudow') ,
    (
     'U7 Gneisenaustr, jetzt Richtung Rudow',
     'Gneisenaustr',
     'U7',
     'Rudow') ,
    (
     'NikoU7 Gneisenaustr, jetzt Richtung RudowSind Südstern immernoch Richtung Rudow draußen',
     None, None, None) ,
    (
     'Gelbe Westen S5 Bellevue. Gerade ausgestiegen',
     'Bellevue.',
     'S5',
     None) ,
    (
     'Tram station bersarinplatz/weidenweg 21 stehen ein paar oa und Polizei...keine Ahnung.einfach Augen auf',
     None, None, None) ,
    (
     'ZoraDie sehen eher nach Security aus und nicht nach Kontrolle?grüne weste ist kontrolleur bei der s-bahn steht auch hinten drauf',
     None, None, None) ,
    (
     'u7, adenauer platz, berlin Ab-ticket, noch ne Stunde gültig. Inne Maschine gelassen',
     'adenauer platz',
     'u7',
     None) ,
    (
     'Die haben mich eben kontrolliert die haben diese neuen Geräte Handys bei der BVG jetzt auch auf der M 10  jetzt gerade Kaffeepause',
     None, None, None) ,
    (
     'Ali ModoPhoto, Die haben mich eben kontrolliert die haben diese neuen Geräte Handys bei der BVG jetzt auch auf der ...Ja, ihr müsst jetzt richtig drauf achten man erkennt die nicht mehr so schnell die haben schon letzte Woche auf dem Bus kontrolliert mit diese neue Geräte !!!!!!!!!!',
     None, None, None) ,
    (
     'U9 richtig osloerstr.',
     None, 'U9',
     'osloerstr') ,
    (
     '2 blauwesten w. gelesen. ',
     None, None, None) ,
    (
     'Grade amruner str. ausgestiegen',
     'amruner str.',
     None, None) ,
    (
     'U5 - Brandenburg Tor',
     'Brandenburg Tor',
     'U5',
     None) ,
    (
     'U9 in Osloerstr. ausgestiegen',
     'Osloerstr.',
     'U9',
     None) ,
    (
     'zwei Blauwesten-Muttis U9, steigen gerade Leo aus. Eine (groß, lange schwarze Haare) hat die Weste nicht an, sondern trägtvsie über dem Arm',
     None, 'U9',
     None) ,
    (
     '4 bos westen märkisches museum, kontrollieren auf dem Bahnhof gerade, richtung pankow',
     'märkisches museum',
     None, 'pankow') ,
    (
     'Blauwesten u5 Alexanderplatz richtung hönow',
     'Alexanderplatz',
     'u5',
     'hönow') ,
    (
     '2 blauwesten u9 Birkenstr',
     'Birkenstr',
     'u9',
     None) ,
    (
     'U9 osloer Richtung Steglitz am Gleis',
     'osloer',
     'U9',
     'Steglitz') ,
    (
     'Steigen ein',
     None, None, None) ,
    (
     'Schöneberg KerstinJa, ihr müsst jetzt richtig drauf achten man erkennt die nicht mehr so schnell die haben schon letzt...Sind das irgendwelche besonderen Geräte ?',
     None, None, None) ,
    (
     '3 Blauwesten Frankfurter Allee U5 Richtung Hbf.',
     'Frankfurter Allee',
     'U5',
     'Hbf.') ,
    (
     '2 weitere Personen warten noch bei Frankfurter Allee U5',
     'Frankfurter Allee',
     'U5',
     None) ,
    (
     '2 Blauwesten u5 Richtung Alexanderplatz gleich Frankfurter Tor',
     'Frankfurter Tor',
     'u5',
     'Alexanderplatz') ,
    (
     'Waren 3 und sind Frankfurter Tor ausgestiegen.',
     'Frankfurter Tor',
     None, None) ,
    (
     '2 Blaue jetzt im Zug, Weberwiese raus',
     'Weberwiese',
     None, None) ,
    (
     'U5',
     None, 'U5',
     None) ,
    (
     'ca 10 leute mit bos westen, wittenbergplatz auf dem Gleis, warten für u2 nach pankow glaube ich',
     'wittenbergplatz',
     'u2',
     'pankow') ,
    (
     'kontrolle u8 richtung hermannplatz grade jannowitz zwei männlich gelesen, eine weiblich gelesene person alles mit b.o.s. uniform bzw westen. ziemlich weit hinten von der bahn',
     'jannowitz',
     'u8',
     'hermannplatz') ,
    (
     'U8 Jannowits',
     'Jannowits',
     'U8',
     None) ,
    (
     'Blaue Jacke Turmstraße u 9 Richtung Osloer 1 weiblich gelesene Mensch',
     'Turmstraße',
     'u 9',
     'Osloer') ,
    (
     '3 Gelbwesten hermannplatz gerade eingestiegen in die u7 richtung rathaus spandau',
     'hermannplatz',
     'u7',
     'rathaus spandau') ,
    (
     'U7, Neukölln, in Uniform',
     'Neukölln',
     'U7',
     None) ,
    (
     '4 balue Westen in U8 jannowitzbruecke',
     'jannowitzbruecke',
     'U8',
     None) ,
    (
     'Mo4 balue Westen in U8 jannowitzbrueckeSind insgesamt zehn in verschiedenen Wagen. Jetzt Heinrich Heine Richtung Hermannstraße.',
     'Heinrich Heine',
     'U8',
     'Hermannstraße.') ,
    (
     'U9 amrumer Richtung zoo',
     'amrumer',
     'U9',
     'zoo') ,
    (
     'U9 Westhafen stehen Blauwesten, konnte beim Rausgehen aber nicht erkennen, was sie genau machen...',
     'Westhafen',
     'U9',
     None) ,
    (
     'U6 Paradestraße',
     'Paradestraße',
     'U6',
     None) ,
    (
     'U8 Hermanplatz',
     'Hermanplatz',
     'U8',
     None) ,
    (
     '2 m gelesene Kontrolletis in M46 Richtung Britz.',
     None, None, None) ,
    (
     'Gerade Haltestelle Reichartstraße',
     'Reichartstraße',
     None, None) ,
    (
     'U9 Richtung Rathaus Steglitz jetzt Amrumer Str',
     'Amrumer Str',
     'U9',
     'Rathaus Steglitz') ,
    (
     'Westhafen ausgestiegen',
     'Westhafen',
     None, None) ,
    (
     'U9 amrumer str, Blauwesten am Bahnsteig',
     'amrumer str',
     'U9',
     None) ,
    (
     'U8 Richtung Wittenau 2 männlich gelesen 1 weiblich gelesen steigen jetzt in Schönleinstr aus',
     'Schönleinstr',
     'U8',
     'Wittenau') ,
    (
     'U5 weberwiese 2 Blau veste +1 more in normal clothes',
     'weberwiese',
     'U5',
     None) ,
    (
     '',
     None, None, None) ,
    (
     'NeelU5 weberwiese 2 Blau veste +1 more in normal clothesrichtung?',
     None, 'NeelU5',
     None) ,
    (
     'hauptbahnhof',
     'hauptbahnhof',
     None, None) ,
    (
     'soniarichtung?.',
     None, None, None) ,
    (
     'U6 Richtung alt mariendorf, grade ulsteinstr. 2 männlich, schwarze jacke',
     'ulsteinstr.',
     'U6',
     'alt mariendorf') ,
    (
     'U2 Kloster Str 5 Personen Ticket Kontrolle',
     'Kloster Str',
     'U2',
     None) ,
    (
     'U2 Klosterstraße 5 Personen Ticket Kontrolle',
     'Klosterstraße',
     'U2',
     None) ,
    (
     'PuroxuIch dachte DB streikt, oder nicht? ',
     None, None, None) ,
    (
     'Also wieso an der Sbhn Kontrollen haben?Notfallfahrplan ;) die Regios die fuhren wurden auch alle Kontrolliert. Zugbegleiter und Kontrollpersonal sind halt nicht in der GDL.',
     None, None, None) ,
    (
     'Kontrolle in der u8 richtung wittensu bei der janowitzbrücke',
     'janowitzbrücke',
     'u8',
     'wittensu') ,
    (
     'Sind teilweise ausgestiegen.',
     None, None, None) ,
    (
     'Sbahn fährt wieder normal wird garnicht kontrolliert ?',
     None, None, None) ,
    (
     'U6 naturkundemuseum Richtung Kurt Schumacher',
     'naturkundemuseum',
     'U6',
     'Kurt Schumacher') ,
    (
     'Blauwesten',
     None, None, None) ,
    (
     'Sind gerade raus',
     None, None, None) ,
    (
     '2x',
     None, None, None) ,
    (
     'Keine Kontis auf em sbahn oder? Es scheint nicht 🤔',
     None, None, None) ,
    (
     'U7 Wilmersdorf ausgestiegen',
     'Wilmersdorf',
     'U7',
     None) ,
    (
     'Leopoldplatz -> Alt Tegel blauvesten',
     'Alt Tegel',
     None, None) ,
    (
     'U2 Gleisdreieck platform direction Pankow',
     'Gleisdreieck',
     'U2',
     'Pankow') ,
    (
     'U2 Alex - 2 x Blauwesten',
     'Alex',
     'U2',
     None) ,
    (
     '3 guys with yellow jacket U5 Museuminsel Hönow',
     'Museuminsel',
     'U5',
     'Hönow') ,
    (
     '2 guys with yellow jackets in U8 Hermannstr',
     'Hermannstr',
     'U8',
     None) ,
    (
     'PhilKeine Kontis auf em sbahn oder? Es scheint nicht 🤔Faehrt auch noch keine wegen streik',
     None, None, None) ,
    (
     'U6 Schumacher-Platz merhingdam',
     'merhingdam',
     'U6',
     'Schumacher-Platz') ,
    (
     'U8 alex richtung wittenau',
     'alex',
     'U8',
     'wittenau') ,
    (
     '',
     None, None, None) ,
    (
     'U8 Alexanderplatz Richtung Wittenau',
     'Alexanderplatz',
     'U8',
     'Wittenau') ,
    (
     '',
     None, None, None) ,
    ("Miguel GalindoPhotothey're at heinrich heine now", 'heinrich heine',
     None, None) ,
    (
     'U6 tempelhof ',
     'tempelhof',
     'U6',
     None) ,
    (
     '4 with yellow vests at platform',
     None, None, None) ,
    (
     'U9 Richtung Osloer Straße, 4 people auf Bahnsteig.',
     None, 'U9',
     'Osloer Straße') ,
    (
     '/line U1, U3 Kontrolle die sind 3 Männer mit schwarze Jacke',
     None, 'U3',
     None) ,
    (
     'U1/U3 schlesisches Tor in 3 Kontrolletis in Security Westen',
     'schlesisches Tor',
     'U1/U3',
     None) ,
    (
     'Richtung Uhlnd Straße',
     None, None, 'Uhlnd') ,
    (
     '4 BOS U9 Zoo on the platform',
     'Zoo',
     'U9',
     None) ,
    (
     'stehn u7 berliner Straße/Richtung Rathaus Spandau, circa 3-4 Leute mit Bos Westen',
     'berliner Straße/Richtung',
     'u7',
     'Rathaus Spandau') ,
    (
     'u1 nach warschauer gerade görli eingestiegen',
     'görli',
     'u1',
     'warschauer') ,
    (
     'U8 Pankstraße nach Wittenau blaue Westen',
     'Pankstraße',
     'U8',
     'Wittenau') ,
    (
     'U8 Pankstraße nach Hermannstraße auch blau Westen',
     'Pankstraße',
     'U8',
     'Hermannstraße') ,
    (
     'Sind in die U Bahn gestiegen',
     None, None, None) ,
    (
     'Blue vest at weinmesterstr. U8',
     'weinmesterstr.',
     'U8',
     None) ,
    (
     '5 blauwesten weinmeister straße',
     'weinmeister straße',
     None, None) ,
    (
     'U8',
     None, 'U8',
     None) ,
    (
     '2 blaue Westen U8 Richtung hermannstrasse',
     None, 'U8',
     'hermannstrasse') ,
    (
     '3 Personen u- Pankow Right Ruhl.',
     'Pankow',
     None, 'Ruhl.') ,
    (
     '1weibl gel. 2männl. Gel. In BVG Uniform',
     None, None, None) ,
    (
     '*richt Theodor Heuss Platz nicht Ruhleben, sorry',
     None, None, 'Ruhleben') ,
    (
     'U7 megringdamm Richtung Rathaus spandau, 2 gelbe Westen',
     'megringdamm',
     'U7',
     'Rathaus spandau') ,
    (
     'U2 klosterstraße 2 in blau 1mal männlich,ein mal weiblich',
     'klosterstraße',
     'U2',
     None) ,
    (
     'u7 richtung rathaus spanda, ca 5 mit bos westen und 2 mit bvg sicherheit sind mierendorff raus. männl gelesen.',
     'mierendorff',
     'u7',
     'rathaus spanda') ,
    (
     'U3 Richtung krumme lanke Wittenbergplatz',
     'Wittenbergplatz',
     'U3',
     'krumme lanke') ,
    (
     'U2 mohrenstr. Rictung ruhleben',
     'mohrenstr.',
     'U2',
     'ruhleben') ,
    (
     'Kontrolleur*innen warten am Ausgang S-Mahlsdorf',
     'S-Mahlsdorf',
     None, None) ,
    (
     'U2 Bülowstraße platform direction Ruhleben',
     'Bülowstraße',
     'U2',
     'Ruhleben') ,
    (
     '3 manner  in U bismarkstr  Bos Westen',
     'bismarkstr',
     None, None) ,
    (
     'MarisaPhoto, Kontrolleur*innen warten am Ausgang S-MahlsdorfDie sehen eher nach Security aus und nicht nach Kontrolle?',
     None, None, None) ,
    (
     'ZoraDie sehen eher nach Security aus und nicht nach Kontrolle?Auf deren Westen steht doch Prüfpersonal ich kenne die, die kontrollieren in der S-Bahn',
     None, None, None) ,
    (
     'Ich dachte DB streikt, oder nicht? ',
     None, None, None) ,
    (
     'Also wieso an der Sbhn Kontrollen haben?',
     None, None, None) ,
    (
     'Hat jemand Lust meine Theaterkarten HEUTE um 17 Uhr in der Schaubühne zu nutzen? Bin verhindert und kann nicht hin. Verschenke sie!',
     None, None, None) ,
    (
     'Di NorrHat jemand Lust meine Theaterkarten HEUTE um 17 Uhr in der Schaubühne zu nutzen? Bin verhindert und ...2x',
     None, None, None) ,
    (
     'Di NorrHat jemand Lust meine Theaterkarten HEUTE um 17 Uhr in der Schaubühne zu nutzen? Bin verhindert und ...https://t.me/+SfbQrVVRAOpyQhcH ',
     None, None, None) ,
    (
     'Sharing is caring Gruppe ',
     None, None, None) ,
    (
     '',
     None, None, None) ,
    (
     'https://t.me/Veranstaltungen_BLN',
     None, None, None) ,
    (
     'Veranstaltungen',
     None, None, None) ,
    (
     '',
     None, None, None) ,
    (
     'Vielleicht wirst du die hier los :)',
     None, None, None) ,
    (
     'U9 Kontrolle 2x bos',
     None, 'U9',
     None) ,
    (
     'Ri Steglitz',
     None, None, 'Steglitz') ,
    (
     'Wo gesichtet?',
     None, None, None) ,
    (
     '',
     None, None, None) ,
    (
     'U-Bahn Hof zoologischer',
     'zoologischer',
     None, None) ,
    (
     'Beide sind ausgestiegen haben eine junge Frau rausgezogen',
     None, None, None) ,
    (
     'U6 kochstrase',
     'kochstrase',
     'U6',
     None) ,
    (
     'Sorry it was a wolt false alarm XD',
     None, None, None) ,
    (
     'U7 berliner str. Min. 10 Kontis gesehen. Ri. Rudow',
     'berliner str.',
     'U7',
     'Rudow') ,
    (
     'U6 Tempelhof am Gleis Richtung Alt Tegel',
     'Tempelhof',
     'U6',
     'Alt Tegel') ,
    (
     'ZoraDie sehen eher nach Security aus und nicht nach Kontrolle?Das ist "Prüfpersonal" - die kontrollieren. Hab ich dann auch noch mitbekommen.',
     None, None, None) ,
    (
     'u6 mehringdamm',
     'mehringdamm',
     'u6',
     None) ,
    (
     'blaue kötter Westen',
     None, None, None) ,
    (
     'fünf Personen',
     None, None, None) ,
    (
     'U2 Pankow. Zoologischer Garden',
     'Zoologischer Garden',
     'U2',
     'Pankow.') ,
    (
     '3 männlich gelesene stehen am Gleis nollendorfplatz Richtung krumme lanke',
     'nollendorfplatz',
     None, 'krumme lanke') ,
    (
     'U8 richtung hermanplatz',
     None, 'U8',
     'hermanplatz') ,
    (
     'rosa luxemburg platz u2 pankow direction',
     'rosa luxemburg platz',
     'u2',
     'pankow') ,
    (
     'MarsPhoto, U8 richtung hermanplatzHaben die kontrolliert? Ne, oder?',
     None, 'U8',
     'hermanplatzHaben') ,
    (
     'U8 kotti polizei kontrol..',
     'kotti',
     'U8',
     None) ,
    (
     'Ich dachte security kontrollieren nicht.',
     None, None, None) ,
    (
     '4 bluevest alex u8 wittenau',
     'alex',
     'u8',
     'wittenau') ,
    (
     'U2 Zoo 2 polizei 2 bvg Sicherheit stehen auf dem Gleis Richtung ruhleben',
     'Zoo',
     'U2',
     'ruhleben') ,
    (
     '2 Blauwesten gerade in der U8, sind Voltastr. drin geblieben. Richtung Wittenau.',
     'Voltastr.',
     'U8',
     'Wittenau') ,
    (
     'Mon2 Blauwesten gerade in der U8, sind Voltastr. drin geblieben. Richtung Wittenau.Jetzt noch 2 andere ohne Westen an der U8 Pankstr.',
     'Pankstr',
     'U8',
     'Richtung Wittenau.Jetzt') ,
    (
     'U8 gesundbrunnen auf dem Gleis stehen welche und kontrollieren',
     'gesundbrunnen',
     'U8',
     None) ,
    (
     'Bananen Kisten  5x abzuholen  Gesundbrunnen',
     'Gesundbrunnen',
     None, None) ,
    (
     'Magic BeamBananen Kisten  5x abzuholen  GesundbrunnenBitte in die foodsharing Gruppe',
     'GesundbrunnenBitte',
     None, None) ,
    (
     'https://t.me/foodsharing_berlin',
     None, None, None) ,
    (
     '19:04 uhr, weitergeleitet:',
     None, None, None) ,
    (
     '',
     None, None, None) ,
    (
     '"U6 Paradestraße',
     'Paradestraße',
     'U6',
     None) ,
    (
     'Wahrscheinlich Richtung Kurt-Schumacher Platz',
     None, None, 'Kurt-Schumacher Platz') ,
    (
     '2 Blauwesten"',
     None, None, None) ,
    (
     'Diskussion zur Kontrollberechtigung in die Diskussionsgruppe verschoben',
     None, None, None) ,
    (
     'U8 leinestrasse, wittenau direction, 4 people',
     'leinestrasse',
     'U8',
     'wittenau') ,
    (
     'U8 Jannowitzbrükcke (2 leute)',
     'Jannowitzbrükcke',
     'U8',
     None) ,
    (
     '[Bea] 🌎Ich dachte security kontrollieren nicht.Kontrollieren auch nicht',
     None, None, None) ,
    (
     'Könnt ihr zum Quatschen bitte in die @Diskussionsgruppe gehen?',
     None, None, None) ,
    (
     'Nachrichten wieder gelöscht.',
     None, None, None) ,
    (
     'AKönnt ihr zum Quatschen bitte in die @Diskussionsgruppe gehen?',
     None, None, None) ,
    (
     'Nachrichten wieder gelöscht.Oki ☺️',
     None, None, None) ,
    (
     '',
     None, None, None) ,
    (
     'U8 Heinrich Heine ausgestiegen',
     'Heinrich Heine',
     'U8',
     None) ,
    (
     'Kontrollieren die mittlerweile samstags?',
     None, None, None) ,
    (
     'MaxKontrollieren die mittlerweile samstags?Ja immer',
     None, None, None) ,
    (
     'Berliner strasse u7 gleis richtung rudow',
     'Berliner strasse',
     'u7',
     'rudow') ,
    (
     'Schöneberg KerstinJa immerOk danke',
     'Schöneberg',
     None, None) ,
    (
     'Bitte hier keine Fragen, ob diese oder jene Linie gerade frei ist, sondern stattdessen die Suchfunktion (das Lupensymbol) nutzen. Danke! Nachricht gelöscht.',
     None, None, None) ,
    (
     'U8 pankstr richtung Hermannstr',
     'pankstr',
     'U8',
     'Hermannstr') ,
    (
     'U2 nach ruleben 4 Kontrolleurs',
     None, 'U2',
     'ruleben') ,
    (
     'Ausgestiegen',
     None, None, None) ,
    (
     '3 gelbe westen S9 am Trepi Richtung Friedrichstraße',
     None, 'S9',
     'Friedrichstraße') ,
    (
     'M10 Kniprodestraße/Danziger Straße Richtung Turmstraße',
     None, None, None) ,
    (
     'U2 zoo richtung ruhleben',
     'zoo',
     'U2',
     'ruhleben') ,
    (
     'M8 Landsberger Chaussee/zossener Straße 2 weibl gelesene',
     None, None, None) ,
    (
     'Eine in komplett schwarz mit schwarzen haaren , die andere mit beiger Jacke und braunen Haaren, beide solar ihm gebräunt',
     None, None, None) ,
    (
     '',
     None, None, None) ,
    (
     'Sind jetzt Betriebshof Marzahn ausgestiegen.',
     'Betriebshof Marzahn',
     None, None) ,
    (
     'unter den linder 2 personas',
     'unter den linder',
     None, None) ,
    (
     'Mmmykolaunter den linder 2 personasRichtung?',
     None, None, None) ,
    (
     'Bundesbullen am Alex oben im Bahnhof',
     'Alex',
     None, None) ,
    (
     'tacco (she/her)Photo, Bundesbullen am Alex oben im BahnhofU oder S',
     'Alex',
     None, None) ,
    (
     '4 Blauwesten U Bismarckstraße. Richtung Pankow',
     'Bismarckstraße.',
     None, 'Pankow') ,
    (
     'S Bahn',
     None, None, None) ,
    (
     'Schöneberg KerstinU oder SS Bahn',
     'Schöneberg',
     None, None) ,
    (
     'Blauwesten ErnstReuter jetzt Richtung Zoo',
     'ErnstReuter',
     None, 'Zoo') ,
    (
     'Schöneberg KerstinU oder SLaut Bild am Übergang zwischen S- und U-Bahn, auf Erdgeschoss-Ebene (kann ja z.B. für Menschen mit Screenreader wichtig sein, dass das in Textform da steht - bloß mal so als Anmerkung).',
     'Schöneberg',
     None, None)
]
