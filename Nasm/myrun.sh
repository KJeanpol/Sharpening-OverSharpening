#!/bin/bash
nasm -f elf64 l.asm -o l.o
ld l.o -o l
./l 364 681