set(BINARY ${CMAKE_PROJECT_NAME})


add_executable(${BINARY}_run src/main.cpp include/Game.h include/GameObject.h src/common/Game.cpp src/common/GameObject.cpp)

add_library(${BINARY}_lib STATIC src/main.cpp include/Game.h include/GameObject.h src/common/Game.cpp src/common/GameObject.cpp)