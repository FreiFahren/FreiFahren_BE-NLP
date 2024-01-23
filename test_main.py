import unittest
from main import find_station, find_line, ubahn_lines, sbahn_lines, find_direction

class TestFindStationAndLineFunction(unittest.TestCase):
    def test_find_station_and_line_dynamic_threshold(self):
        # Rules: Always judge as correct as possible, ignoring the current capibility of the model
        test_cases = [
            ("heinrich-heine zwei blauwesten", "Heinrich-Heine-Straße", None, None),
            ("U6 Schumacher-Platz 2 Controller merhingdam", "Schumacherplatz", "U6", None),
            ("2x Hellblau U8 Hermannplatz Richtung Wittenau am Bahnsteig", "Hermannplatz", "U8", "Wittenau"),
            ("U8 pankstrasse 2 Blau veste", "Pankstraße", "U8", None),
            ("2 Kontrolleure U9 Richtung Osloer Straße", None, "U9", "Osloer Straße"),
            ("Und zwei Cops oben am Bahnsteig der SBahn", None, None, None),
            ("U 8 Heinrich Heine str", "Heinrich-Heine-Straße", "U8", None),
            ("Friedrichstrasse bei der u6 waren gerade zwei mit bos westen", "Friedrichstraße", "U6", None),
            ("2personen dunkel blaue weste", None, None, None),
            ("U2 Ernst Reuter Platz", "Ernst-Reuter-Platz", "U2", None),
            ("U9 4 (oder mehr) blauwesten auf Gleis Spichernstraße", "Spichernstraße", "U9", None),
            ("Zwei Stück Richtung Osloer", None, None, "Osloer Straße"),
            ("Jetzt Zoo in der Bahn richtung Steglitz!", "Zoologischer Garten", None, "Rathaus Steglitz"),
            ("U6 Mehringdamm -> hallesches Tor gerade ausgestiegen. 2 Kontrolleure in schwarz, glaube ich. :", "Hallesches Tor", None, None),
            ("S Alexanderplatz west direction at least one ticket checker with a white puffer jacket on the platform", "Alexanderplatz", None, None),
            ("u6 leopoldplatz towards alt mariendorf 2 people with 2 cops", "Leopoldplatz", "U6", "Alt-Mariendorf"),
            ("u6 paradestraße ausgestiegen.", "Paradestraße", None, None),
            ("M10 towards turmstr. two guys with no uniform", None, "M10", "Turmstraße"),
            ("U boddinstrasse. 5 security's / 3 cops", "Boddinstraße", None, None),
            ("Gerade S Tiergarten Richtung zoo", "Tiergarten", None, "Zoologischer Garten"),
            ("Walther Schreiber Platz U9 Richtung Rathaus Steglitz Kontrolletis", "Walther-Schreiber-Platz", "U9", "Rathaus Steglitz"),
            ("2 in schwarz S tempelhof", "Tempelhof", None, None),
            ("Grad ausgestiegen s41", None, "s41", None),
            ("S7, 2 männlich gelesene in zivil grad Friedrichstraße mit jemandem ausgestiegen", "Friedrichstraße", "S7", None),
            ("Ring zwischen S Tempelhof und S Hermannstraße", "Tempelhof", None, None),
            ("U2 Märkisches Museum richtung ruhleben 3 Männer mit B.O.S Jacken", "Märkisches Museum", "U2", "Ruhleben"),
            ("Ring Bahn Hohenzollerndamm vor 2 Minuten eine Person alleine", "Hohenzollerndamm", None, None),
            ("S1 Richtung Spindersfeld, männlich gelesen gerade bei hermannstraße geht durch die Bahn", "Hermannstraße", "S1", "Spindlersfeld"),
            ("S1 nach spindlersfelde war ein am hermannplatz oder vorher", "Hermannplatz", "S1", "Spindlersfeld"),
            ("U8 Wittenau sind U Jannowitzbrücke raus", "Jannowitzbrücke", "U8", "Wittenau"),
            ("messe nord grad raus", "Messe Nord/ICC", None, None),
            ("3x weiblich jetzt westkreuz ina s41", "Westkreuz", "S41", None),
            ("Kontrolle in s42 jetzt Treptower Park", "Treptower Park", "S42", None),
            ("Kontrolle auf der Strecke u9", None, "U9", None),
            ("BOS Alex u8 on the platform", "Alexanderplatz", "U8", None),
            ("A lot of bvg and cops, outside, at Hermanplatz", "Hermannplatz", None, None),
            ("3x m gelesen 1x w gelesen am hermannplatz Gleis u8 Richtung hermannstraße blaue bos jacken", "Hermannplatz", "U8", "Hermannstraße"),
            ("S42 greiswalder strasse2 Männer 1 frau", "Greifswalder Straße", "S42", None),
            ("Ring zwischen Hohenzollerndamm und Halensee. 3x weiblich gelesen, davon 1x weiße Jacke, 1x schwarz glänzende Jacke", "Hohenzollerndamm", None, None),
            ("2 Kontrolleure read male black outfits black beards in S8 to Ostkreuz, now Storkower Str got off at Storkower Straße", "Storkower Straße", "S8", "Ostkreuz"), 
            ("S41 gleich Tempelhof. Ein Typ, eine Frau. Beide schwarze Kapuzenjacke. Er mit North Face Mütze schwarz, Sie mit langen blonden Haaren", "Tempelhof", "S41", None),
            ("U6 steigen gerade Wedding ein Richtung alt mariendorf im hinteren Teil der Bahn 3m blaue Jacken", "Wedding", "U6", "Alt-Mariendorf"),
            ("Kontrolleur m gelesen S2 Frohnau jetzt Halensee In zivil, schwarze Jacke, schwarze Haare, braune Ledertasche", "Halensee", "S2", "Frohnau"),
            ("Jannowitzbrücke U8", "Jannowitzbrücke", "U8", None),
            ("S42 Tempelhof ein Mann und eine Frau mit langen blonden Haaren.", "Tempelhof", "S42", None),
            ("S41 tempelhof", "Tempelhof", "S41", None),
            ("U6 Friedrichstrasse direction north, K.Schumacher platz, 3 mannlich gelesen mit B.O.B. jackets", "Friedrichstraße", "U6", "Kurt-Schumacher-Platz"),
            ("2 männer S42 Treptower park", "Treptower Park", "S42", None),
            ("S41 in Storkowerstr Richtung Ostkreuz", "Storkower Straße", "S41", "Ostkreuz"),
            ("2 civil controllis in s 41 to landsberger", None, "S41", "Landsberger Allee"),
            ("Three female kontrolettis in the S42 soon to be Bundesplatz", "Bundesplatz", "S42", None),
            ("S45 Flughafen BER", "Flughafen BER", "S45", None),
            ("Sind jetzt jungfeenheide. 1 x mal männlich und 1x mal weiblich gelesen komplett in schwarz", "Jungfernheide", None, None),
            ("S8 Ostkreuz", "Ostkreuz", "S8", None),
            ("Controller in S7 Richtung Alexanderplatz Was just checked in jannowitzbrucke", "Jannowitzbrücke", "S7", "Ahrensfelde"),
            ("S42 Landsberger Alle, 2m, schwarze Jacke, schwarze Mütze. 2 m mit Gelber Weste begleiten.", "Landsberger Allee", "S42", None),
            ("3 Kontrolleure s Greifswalder", "Greifswalder Straße", None, None),
            ("S8 Greifswalder Straße", "Greifswalder Straße", "S8", None),
            ("S41 Ringbahn Landsberger allee big group of kontrolettis", "Landsberger Allee", "S41", None),
            ("Ring 41-> Landsberger Allee, glaube mehrere männer die auch Minderjährige hochnehmen", "Landsberger Allee", "S41", None),
            ("S42, 3x agressiv männlich, gerade Schönhauser ausgestiegen", "Schönhauser Allee", None, None),
            ("Ring s42  approaching geundbrunnen civil control", "Gesundbrunnen", "S42", None),
            ("5 Kontrolleure S8 to Birkenwerder", None, "S8", "Birkenwerder"),
            ("U8 heinrrich heinest blue vest at platform", "Heinrich-Heine-Straße", "U8", None),
            ("Friedrichstraße", "Friedrichstraße", None, None),
            ("Spichernstraße U3 am Bahnsteig eine Person männl gelesen, komplett schwarz angezogen mit braunem undercut, ca 30 Jahre.. wirkt aber sehr nett weil er grad jemand erklärt wie er das Ticket einer anderen Person nachreichen kann", "Spichernstraße", "U3", None),
            ("2x Blauwesten u8 Heinrich Heine straße Richtung Hermannstraße", "Heinrich-Heine-Straße", "U8", "Hermannstraße"),
            ("Bitte hier keine Fragen, ob diese oder jene Linie gerade frei ist, sondern stattdessen die Suchfunktion (das Lupensymbol) nutzen. Danke! Nachricht gelöscht.", None, None, None),
            ("Two men wearing normal clothes in M5, checking tickets, just got off at alexanderplatz", "Alexanderplatz", "M5", None),
            ("U1 at hallesches tor towards warschauer str.  2 maybe 3 blue wests giving fines", "Hallesches Tor", "U1", "Warschauer Straße"),
            ("Wenn mein Infopost über die Demo am Sonntag Nachmittag gegen Rechts als Spam gewertet wird (über die ja auch im Bild der Gruppe informiert wird) würde ich mir eine kurze Rückmeldung von euch darüber wünschen", None, None, None),
            ("No basically this is the decision of the admins who run this group because we share certain values and leftist politics. If you happen to dislike actions against fascists, it's you who might not belong in this group. Like Spam.", None, None, None),
            ("S41 Treptower Park, 2 Männer", "Treptower Park", "S41", None),
            ("U1 hallesches tor in der bahn richtung westen", "Hallesches Tor", "U1", "Uhlandstraße"),
            ("s7 nach Ahrensfelde 3 Männer schwarze jacken hackescher markt ausgestiegen", "Hackescher Markt", None, None),
            ("Ring S41 Sonnenallee Richtung Neukölln", "Sonnenallee", "S41", None),
            ("U6 friedrichstr", "Friedrichstraße", "U6", None),
            ("S42 two guys at frankfurterallee", "Frankfurter Allee", "S42", None),
            ("Alexanderplatz an Gleis der u8 hellblaue westen", "Alexanderplatz", "U8", None),
            ("4x männlich gelesen S42 aktuell Landsbegwr immer noch im Zug", "Landsberger Allee", "S42", None),
            ("Alexanderplatz sbahn platform", "Alexanderplatz", None, None),
            ("41 wedding. Grun mantel", "Wedding", "S41", None),
            ("Ostbahnhof 8 Bundesbullen stehen an der Bahnsteigkante. Alle mit gelben Westen. Keine Ahnung ob die eingestiegen sind.", "Ostbahnhof", None, None),
            ("Ostkreuz 6 Polizisten kontrollieren Ausweise willkürlich", "Ostkreuz", None, None),
            ("U6 Unter den Linden", "Unter den Linden", "U6", None),
            ("unter den Linden, U6, Richtung Tegel, eine m gelesene Person mit blauer wrtse", "Unter den Linden", "U6", "Tegel"),
            ("U6 Richtung alt Mariendorf Stadtmitte eingestiegen 2 blauwesten m gelesen", "Stadtmitte", "U6", "Alt-Mariendorf"),
            ("U8 Hermannstr, just saw police + BVG going downstairs from the street", "Hermannstraße", "U8", None),
            ("U8 Hermannstraße", "Hermannstraße", "U8", None),
            ("S42 Hermanstraße , 2x schwarze Jacken", "Hermannstraße", "S42", None),
            ("S25 S Hennigsdorf a least 2Pers.", "Hennigsdorf", "S25", None),
            ("3 Blauwesten Ubhf Heinrich Heine Str", "Heinrich-Heine-Straße", None, None),
            ("U3 freie Universität stehen blau Westen. Sie werden wohl die nächste Bahn in die Innenstadt nehmen", "Freie Universität", "U3", None),
            ("U8 rosenthaler Richtung hermanstr", "Rosenthaler Platz", "U8", "Hermannstraße"),
            ("M27 Pankstr Richtung Jungfernheide", "Pankstraße", "M27", "Jungfernheide"),
            ("U2 From Alex to Ruhleben now bunch of them in a wagon", "Alexanderplatz", "U2", "Ruhleben"),
            ("3 mänlich gelesene 2 mit gelben westen 1 mit blauer bos weste alex u8 richtung wittenau", "Alexanderplatz", "U8", "Wittenau"),
            ("About to get off s8 Prenzlauer Allee", "Prenzlauer Allee", None, None),
            ("M29 two men, to Halensee", None, "M29", "Halensee"),
            ("s47 nach spindlerfeld s tempelhof eingestiegen 2 in zivil", "Tempelhof", "S47", "Spindlersfeld"),
        ]

        def run_tests_for_threshold(threshold, report_failures=False):
            successes = 0
            failure_messages = []
            
            for text, expected_station, expected_line, expected_direction in test_cases:
                line = find_line(text, ubahn_lines + sbahn_lines)
                result = find_direction(text)
                direction = result[0]
                text_without_direction = result[1]
                station = find_station(text_without_direction, threshold)
                if station == expected_station and line == expected_line and direction == expected_direction:
                    successes += 1
                elif report_failures:
                    failure_message = f"Text: '{text}'"
                    if station != expected_station:
                        failure_message += f"\nStation Expected: '{expected_station}' Found: '{station}'"
                    if line != expected_line:
                        failure_message += f"\nLine Expected: '{expected_line}' Found: '{line}'"
                    if line != expected_line:
                        failure_message += f"\nDirection Expected: '{expected_direction}' Found: '{direction}'"
                    failure_message += "\n------"
                    failure_messages.append(failure_message)

            print('Testing for threshold:', threshold)
            print('With sucessrate of: ',successes, '/', len(test_cases))
            return successes, failure_messages

        lower_bound = 0
        upper_bound = 100
        optimal_threshold = lower_bound
        max_successes = 0

        while upper_bound - lower_bound > 1:
            mid_point = (lower_bound + upper_bound) // 2
            lower_successes, _ = run_tests_for_threshold(lower_bound)
            mid_successes, _ = run_tests_for_threshold(mid_point)
            upper_successes, _ = run_tests_for_threshold(upper_bound)

            max_current_success = max(lower_successes, mid_successes, upper_successes)

            # Update the optimal threshold if the current midpoint has the highest success count.
            if mid_successes == max_current_success:
                optimal_threshold = mid_point

            # Adjust bounds
            if lower_successes == max_current_success:
                if mid_point - lower_bound > 1:
                    upper_bound = mid_point
                else:
                    upper_bound -= 1
            elif upper_successes == max_current_success:
                if upper_bound - mid_point > 1:
                    lower_bound = mid_point
                else:
                    lower_bound += 1
            else:
                lower_bound += 1
                upper_bound -= 1

            max_successes = max_current_success

        _, failure_messages = run_tests_for_threshold(optimal_threshold, report_failures=True)
        failure_report = "\n".join(failure_messages)

        self.assertEqual(len(failure_messages), 0, f'Optimal threshold: {optimal_threshold} with {max_successes} successful matches\n\nFailures:\n{failure_report}')

if __name__ == '__main__':
    unittest.main()