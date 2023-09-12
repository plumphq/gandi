#!/bin/bash

printf "> \e[93mEnter the company name: \e[0m"
read companyName

companyName=$(echo "$companyName" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')

base_dir=$(dirname "$0")/..

if [ -d "$base_dir/careers/$companyName" ]; then
    printf "> \e[94mThe folder \e[0m$companyName\e[94m already exists. Perhaps someone from your company already created it before.\e[0m\n"
else
    mkdir -p "$base_dir/careers/$companyName"
    cp $base_dir/careers/template/careers.yaml "$base_dir/careers/$companyName/careers.yaml"
    cp $base_dir/careers/template/company.yaml "$base_dir/careers/$companyName/company.yaml"

    printf "> \e[94mYou can find \e[93mcareers.yaml\e[94m and \e[93mcompany.yaml\e[94m files in the \e[0m$companyName\e[94m folder now.\e[0m\n"
fi