
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.6
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
HYPHEN_INSENSITIVE="true"
DISABLE_MAGIC_FUNCTIONS="true"
ENABLE_CORRECTION="true" 
COMPLETION_WAITING_DOTS="true"

export ZSH_COMPDUMP=$ZSH/cache/.zcompdump-$HOST
export ZSH_COMPDUMP=$ZSH/cache/.zcompdump-$HOST
export MANPATH="/usr/local/man:$MANPATH"
export LANG=en_AU.UTF-8
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
 else
  export EDITOR='nvim'
 fi

# Compilation flags
export ARCHFLAGS="-arch $(uname -m)"

alias zshconfig="nvim ~/.zshrc"
alias ohmyzsh="mate ~/.oh-my-zsh"
alias l="lsd -1lr"
alias n="nvim "
alias m="qobuz-dl fun"
alias c="cp Qobuz\ Downloads storage/music/ -r && rm -rf Qobuz\ Downloads"
