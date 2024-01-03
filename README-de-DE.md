# Discord Attachment Downloader v1.0

![](https://github.com/BD202009/Discord-Attachment-Downloader/blob/main/logo/dad-logo.png)

## Über

Lade Anhänge aus einem angegebenen Discord-Chat oder -Kanal herunter. Die Dateien werden im Format (yyyyMMdd_HHmmss_originalFileName) gespeichert. Zusätzlich werden relevante Informationen wie der Nachrichtentext und der Absender in einer entsprechenden TXT-Datei gespeichert.

## Einrichtung

### Auf einem Windows-Computer

#### Installieren der Abhängigkeiten

1. Installieren Sie [Visual Studio Community 2022](https://visualstudio.microsoft.com/de/downloads/ "Visual Studio Community") oder eine neuere Version.
2. Installieren Sie den Python-Entwicklungs-Workload, einschließlich der optionalen nativen Python-Entwicklungstools, in der Visual Studio Community.
3. Installieren Sie [Python 3.12](https://www.python.org/downloads/ "Python 3.12") oder eine neuere Version.

Nicht mehr erforderlich, da die Abhängigkeiten automatisch installiert werden.

- Installieren Sie die 'discord.py'-Bibliothek mit dem Befehl:
```bash 
pip install discord.py
```

#### Einrichten eines Discord-Bots

1. Öffnen Sie [https://discord.com/developers/](https://discord.com/developers/).
2. Navigieren Sie zum linken Menüpunkt 'Applications' und klicken Sie auf 'New Application', um eine neue Anwendung hinzuzufügen.
3. Benennen Sie Ihre Anwendung (z. B. 'attachment_downloader') und klicken Sie auf 'Create'.
4. Wählen Sie 'Bot' im linken Menü aus.
5. Klicken Sie auf 'Add Bot' und bestätigen Sie das Hinzufügen eines Bots zu Ihrer Anwendung, indem Sie auf 'Yes, do it!' klicken. Ihr Bot ist jetzt erstellt.
6. Klicken Sie neben dem Bot-Symbol auf 'Copy', um den Bot-Token zu kopieren/notieren. Falls der 'Copy'-Button nicht sichtbar ist, klicken Sie zuerst auf 'Regenerate', um einen neuen Bot-Token zu generieren.
<span style="color:red;">Teilen Sie den Token nicht!</span>

#### Um den Bot für Kanäle innerhalb Ihres Servers zu verwenden:

1. Navigieren Sie zu 'OAuth2' und 'URL Generator' über das linke Menü, um einen Berechtigungslink zu generieren.
2. Wählen Sie auf dem folgenden Bildschirm unter 'SCOPES' 'bot' aus und wählen Sie unter 'BOT PERMISSIONS' 'Administrator' aus.
3. Kopieren Sie die 'GENERATED URL' und öffnen Sie sie in einem neuen Browserfenster.
4. Wählen Sie den Server aus, mit dem der Bot verknüpft werden soll, und klicken Sie auf 'Continue'.
5. Klicken Sie auf 'Authorize', um die Berechtigungen des Bots zu bestätigen.

## Skript ausführen

1. Klone oder lade dieses Repository herunter und platziere es in einem beliebigen Ordner auf deinem Computer.
2. Starte das Skript, indem du entweder die Datei 'start.py' oder 'start.bat' öffnest.
3. Gib während des ersten Durchlaufs deinen Bot-Token ein; er wird dauerhaft in der Konfigurationsdatei gespeichert.
4. Gib die Discord-Server-Kanal-ID ein, aus der du Anhänge herunterladen möchtest. Du kannst die Kanal-ID in jedem Skriptlauf bestätigen oder ändern.
5. Gib die Start- und Enddaten für die Anhänge an. Drücke 'Enter', um alle Dateien ohne Datumsfilterung zu erhalten.
6. Das Skript wird alle Anhänge herunterladen. Wenn ein Anhang bereits im Ausgabeordner existiert, wird er automatisch überschrieben.
7. Im Ausgabeordner findest du die Anhänge und entsprechende TXT-Dateien mit dem Namen des Erstellers und dem Nachrichtentext.

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz] - siehe die [LICENSE](LICENSE)-Datei für Details.

### Ende
