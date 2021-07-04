# Holmes2 

![GitHub](https://img.shields.io/github/license/Omoshirokunai/holmes2?style=flat-square) ![GitHub repo size](https://img.shields.io/github/repo-size/Omoshirokunai/holmes2?style=flat-square)

The open source home for digital image foresnics and analysis tools

## Table of contents

- [Holmes2](#holmes2)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Available features](#available-features)
  - [Technologies](#technologies)
  - [Setup](#setup)
  - [File structure](#file-structure)
  - [TODO](#todo)
  - [issues](#issues)

## General info

Holmes2 is designed to be a home for digital image forensics tools that is simple to extend with the aim of creating a platform for researchers and forensic experts to experiment and showcase various digital image forensics algorithms.

This project is my undergrad final project and i initially intended it to be an automated tool for detecting forgery then i realised i didnt have the time for that task, so i decided to pivot to make holmes more of a toolkit. Although the project has not relationship with a similar but more complete project called [sherloq](https://github.com/GuidoBartoli/sherloq), I think thanks to [streamlit](https://github.com/streamlit/streamlit) it should be a lot easier to contribute new algorithms.

**Note**: Holmes is not meant to be an automated tool for deciding if an image if foreged or not. Holmes is still lacking UI polish, and several [issues](#issues).

<!-- ![image](https://user-images.githubusercontent.com/65668668/104768691-5b9d8100-576e-11eb-858d-e89e49a28c82.png) -->

## Available features

* Exif viewer
* Quantization tables matching(not yet complete)
* Error level analysis
* [Noiseprint](https://github.com/grip-unina/noiseprint) by grip-unina
  
## Technologies

Project is created with:

* python: 3.8
* streamlit

## Setup

To run this project

install necessary pip libraries

```bash
 pip install -r requirements.txt
```
To run holmes in browser

```bash
streamlit run holmes.py
```

## File structure

* Holmes.py: is the main script, which contains streamlit page setup and page navigation

* Every other module should be named after what they accomplish.

## TODO

* Using quantization tables from jpeg images we can classify the origins of an image.
* Imporve file structure
* UI changes
  
## issues

* Currently runing noiseprint in an unpythonic fashion.
