# TDD_Can_LLM_Code_unit_tests Repository Overview

This repository is dedicated to exploring and testing the capabilities of Large Language Models (LLMs) in coding, particularly focusing on unit testing and statistical analysis implementations in Lua and Python. Our goal is to leverage LLMs to improve code quality and efficiency.

## Getting Started

To get started with this repository, clone it locally and explore the various Lua and Python scripts. Each script was made by a different LLM and is designed to test the LLM's coding capabilities. The repository also contains unit tests for each script, which can be run to evaluate the LLM's performance.

## Contribution

Contributions are closed for the time being. We are currently in the process of evaluating the performance of various LLMs on the scripts in this repository. Once we have completed this evaluation, we expect to be able to open up contributions to the public, in the meantime, feel free to fork this repository and experiment with the scripts and unit tests.

## Directory Structure

The repository is organized into the following directories:

- `Unit_tests_lua`: Contains Lua scripts and their corresponding unit tests.
- `Unit_tests_python`: Contains Python scripts and their corresponding unit tests.

Each directory contains subdirectories for different prompts as EX 01 up to EX 06 (Prompt 1 to Prompt 6) and each subdirectory contains the following files:
Valid for both Python and Lua subdirectories:
- `Prompts_changelog.md`: Contains the prompt description and any revisions made to the prompt.
- `LLM_name.py` or `LLM_name.lua`: Contains the code generated by the LLM for the prompt.

Valid only for Python subdirectories:
- `name_of_the_folder_test.py`: Contains the unit tests for the Python script being named after the folder's name.
- `config.py` and `utils.py`: Contains the configuration and utility functions for the unit tests.
- `Pylint_evaluation.py` and `pylint_runner.py`: Contains the pylint evaluation and runner for the Python script.'
- `cprofile_evaluation.py`: Contains the performance evaluation for the Python script.

Valid only for Lua subdirectories:
- A `tests` or `Test_files` directory: Contains the versions of each LLM-generated Lua script that have been modified to be compatible with my unit tests.

any other directories like `Unit_tests_python_Code_optimization_stage` and possibly in the future `Unit_tests_lua_Code_optimization_stage` are for future use and are not currently in use.

## License

This project is open source and available under the [MIT License](LICENSE).

Thank you for your interest in our LLM coding tests repository. We're excited to see how these tests can push the boundaries of what LLMs can achieve in coding and unit testing.
