cmake_minimum_required(VERSION 3.10)
project(CoolGame)


enable_testing()
include_directories(game)
include_directories(game/include)
include_directories(game/src/common)

include_directories(dependencies/googletest dependencies/googletest/include)

add_subdirectory(game)

add_subdirectory(game/src/test)

add_subdirectory(dependencies/googletest)


