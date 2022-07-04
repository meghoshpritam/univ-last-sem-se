# TODO

- run this boundary value testing
- gfg run bvt
- alpha testing
- beta testing
- unit testing
- loop count

## Installation

reference <https://gist.github.com/meghoshpritam/eb9b427c8e45ef349bb56279785f5082>

### System prerequisite

#### system update

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```

#### zsh installation

```bash
sudo apt-get install -y zsh curl git
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

#### install python 3

```bash
sudo apt-get install -y python3-pip
sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt-get install -y python3-venv
```

##  Required packages

python version 3.8.10

### packages

```bash
# run if got error: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
sudo apt-get install python3-tk
```

```bash
pip install pytest
pip install matplotlib

```

### Run pytest file

```
# Check python version
python --version

# Check PIP version
pip --version
```


```
# Linux
python3 -m pytest test_fileName.py -v # if you wish to run a single test file
python3 -m pytest directoryLocation -v # if you wish to run all the test file in a directory
```

```
# Windows
pyWindows test_fileName.py -v # if you wish to run a single test file
pytest directoryLocation -v # if you wish to run all the test file in a directory
```
