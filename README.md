# pysoundbox

Add this lib ass shortcut and play sounds as a soundbox.

To add a script command to a shorcut, see config folder.

Gnome: see [this link](https://unix.stackexchange.com/questions/41283/how-to-run-the-terminal-using-keyboard-shortcuts-in-gnome-2)

KDE: see [this link](https://ubuntuforums.org/showthread.php?t=1870198)


## Requirements

```bash
sudo apt install mpg321
```

## Pythonic way to create audios

Use [Pydub](https://github.com/jiaaro/pydub) and install [dependencies](https://github.com/jiaaro/pydub#dependencies)

```python
from pydub import AudioSegment
sound = AudioSegment.from_mp3("[AUDIO_FILE].mp3")
new_sound = sound[18*1000:22*1000]
new_sound.export("[NEW_AUDIO_FILE].mp3", format="mp3")
```
