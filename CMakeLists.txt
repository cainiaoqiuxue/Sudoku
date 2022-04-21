cmake_minimum_required(VERSION 3.4)
project(sudoku)

add_subdirectory(pybind11)
pybind11_add_module(sudoku sudoku_src.cpp)
