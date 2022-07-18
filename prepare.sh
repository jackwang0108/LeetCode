#! /usr/bin/bash

red="\033[0;31m"
green="\033[0;32m"
blue="\033[0;34m"
purple="\033[0;35m"
yellow="\033[1;33m"
normal="\033[0m"




cmakerun(){
    filenum=$#
    if [ $filenum -eq 0 ]
        then
            echo "${red}Planning to run 0 files, stopping${normal}"
    fi
    echo -e "${yellow}===================== Planning to run ${filenum} files =====================${normal}"
    echo -e "${green}Run:${normal}"
    runfiles=( "$@" )
    for i in "${runfiles[@]}";
        do
            echo -e "${green}\t$i${normal}"
    done

    echo -e "${yellow}=========================== Start running =========================${normal}"
    workdir=$(pwd)
    echo -e "Running in ${workdir}"
    bindir="${workdir}/bin"
    if [ ! -d "${bindir}" ]
        then
            echo -e "${bindir} not exists, assuming in build..."
            bindir="$(pwd)"/../bin
            if [ ! -d "${bindir}" ]
                then
                    echo -e "${red}${bindir} not exists, aborting..."
                    exit
            else
                echo "${bindir} detected!"
            fi
    else
        echo "${bindir} detected!"
    fi

    for s in "${runfiles[@]}";
        do
            # bn=${s%.*} 
            bn=$s
            ss="${bindir}/${bn}"
            echo -e "${purple}Running: ${s}${normal}"
            echo -e "\tSource ${ss}"
            echo -e "${blue}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++${normal}"
            "${ss}"
            echo -e "${blue}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++${normal}"
            # echo -e "\t${green}success${normal}"
    done
}


_cmakerun(){
    local cur prev prev_prev
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"


    completion=""
    workdir=$(pwd)
    bindir="${workdir}/bin"
    if [ ! -d "${bindir}" ]
        then
            bindir="$(pwd)"/../bin
            if [ ! -d "${bindir}" ]
                then
                    exit
            fi
    fi

    filelist=$(ls "${bindir}")
    completion=""
    for i in ${filelist};
        do
            completion+=" ${i}"
    done

    case "${cur}" in
        *)
            # COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            COMPREPLY=( $(compgen -W "$completion" -- ${cur}) )
            return 0
            ;;
    esac

    return 0
}
complete -F _cmakerun cmakerun