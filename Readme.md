# Voice-Assistant

Asistente de voz multiproposito basado en whisper AI y CHATGPT.

## Setup

El codigo usar whisper AI para transformar la voz a texto reconocible, para usar whisper AI es necesario python 3.8 o superior

    https://www.python.org

tambien es necesario PyTorch 1.10.1 o superior

    https://pytorch.org/get-started/locally/

por ultimo tambien es necesario tener ffmpeg en el sistema


```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```
