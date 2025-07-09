# mise-en-space

A tool to bootstrap and tools on clean machines, built on [mise](https://mise.jdx.dev/)

## Why?

### Build and test

For every source repo in the world, you should be able to clone it onto a clean machine, run the "build and test" script, and have it just work. 

Mise goes a long way to making this possible, but there are still a couple gaps. The most important one is that you need to install Mise first. Instead, rename this script to `mise` and run it - it will install Mise for you and run the command you want, transparently.

snippet: run_mise

## Other parts of the developer experience

Pretty much every repo has small scripts or tasks that developers need to run directory. You could write a shell script for each one, that does `mise run <taskname>` but that can lead to a huge proliferation of scripts. If you want to tell your developers "run `python --version`", you can use this script to bootstrap Python via Mise, and then run the command:

snippet: run_python

