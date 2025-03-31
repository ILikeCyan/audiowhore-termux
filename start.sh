#!/bin/sh

pkg install root-repo git python openssl python-pip zsh && chsh -s zsh
git clone https://github.com/ILikeCyan/audiowhore-termux.git
cp audiowhore-termux/* $HOME/ -r
cp audiowhore-termux/.* $HOME/ -r
pip install qobuz-dl
rm -rf .config/qobuz-dl
zsh
m
echo "Done"



