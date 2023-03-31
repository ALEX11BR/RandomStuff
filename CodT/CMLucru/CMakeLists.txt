cmake_minimum_required(VERSION 3.0)
set(CMAKE_CXX_STANDARD 11)

project(CMLucru)

#find_package(PkgConfig REQUIRED)
#pkg_check_modules(GTKMM REQUIRED gtkmm-3.0)

add_executable(main main.cpp)

#target_link_libraries(tlucru ${GTKMM_LIBRARIES})
#target_include_directories(tlucru PUBLIC ${GTKMM_INCLUDE_DIRS})
#target_compile_options(tlucru PUBLIC ${GTKMM_CFLAGS_OTHER})
