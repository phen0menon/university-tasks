# CMAKE generated file: DO NOT EDIT!
# Generated by "NMake Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

!IF "$(OS)" == "Windows_NT"
NULL=
!ELSE
NULL=nul
!ENDIF
SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2019.2.3\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2019.2.3\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Dev\university-tasks\homework-cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Dev\university-tasks\homework-cpp\cmake-build-debug

# Include any dependencies generated for this target.
include Google_tests\lib\googlemock\CMakeFiles\gmock.dir\depend.make

# Include the progress variables for this target.
include Google_tests\lib\googlemock\CMakeFiles\gmock.dir\progress.make

# Include the compile flags for this target's objects.
include Google_tests\lib\googlemock\CMakeFiles\gmock.dir\flags.make

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.obj: Google_tests\lib\googlemock\CMakeFiles\gmock.dir\flags.make
Google_tests\lib\googlemock\CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.obj: ..\Google_tests\lib\googletest\src\gtest-all.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Dev\university-tasks\homework-cpp\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Google_tests/lib/googlemock/CMakeFiles/gmock.dir/__/googletest/src/gtest-all.cc.obj"
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	"C:\Program Files (x86)\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1423~1.281\bin\Hostx86\x86\cl.exe" @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoCMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.obj /Fd..\..\..\bin\gmockd.pdb /FS -c C:\Dev\university-tasks\homework-cpp\Google_tests\lib\googletest\src\gtest-all.cc
<<
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gmock.dir/__/googletest/src/gtest-all.cc.i"
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	"C:\Program Files (x86)\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1423~1.281\bin\Hostx86\x86\cl.exe" > CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.i @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Dev\university-tasks\homework-cpp\Google_tests\lib\googletest\src\gtest-all.cc
<<
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gmock.dir/__/googletest/src/gtest-all.cc.s"
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	"C:\Program Files (x86)\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1423~1.281\bin\Hostx86\x86\cl.exe" @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoNUL /FAs /FaCMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.s /c C:\Dev\university-tasks\homework-cpp\Google_tests\lib\googletest\src\gtest-all.cc
<<
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\src\gmock-all.cc.obj: Google_tests\lib\googlemock\CMakeFiles\gmock.dir\flags.make
Google_tests\lib\googlemock\CMakeFiles\gmock.dir\src\gmock-all.cc.obj: ..\Google_tests\lib\googlemock\src\gmock-all.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Dev\university-tasks\homework-cpp\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object Google_tests/lib/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.obj"
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	"C:\Program Files (x86)\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1423~1.281\bin\Hostx86\x86\cl.exe" @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoCMakeFiles\gmock.dir\src\gmock-all.cc.obj /Fd..\..\..\bin\gmockd.pdb /FS -c C:\Dev\university-tasks\homework-cpp\Google_tests\lib\googlemock\src\gmock-all.cc
<<
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\src\gmock-all.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gmock.dir/src/gmock-all.cc.i"
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	"C:\Program Files (x86)\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1423~1.281\bin\Hostx86\x86\cl.exe" > CMakeFiles\gmock.dir\src\gmock-all.cc.i @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Dev\university-tasks\homework-cpp\Google_tests\lib\googlemock\src\gmock-all.cc
<<
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\src\gmock-all.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gmock.dir/src/gmock-all.cc.s"
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	"C:\Program Files (x86)\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1423~1.281\bin\Hostx86\x86\cl.exe" @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoNUL /FAs /FaCMakeFiles\gmock.dir\src\gmock-all.cc.s /c C:\Dev\university-tasks\homework-cpp\Google_tests\lib\googlemock\src\gmock-all.cc
<<
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug

# Object files for target gmock
gmock_OBJECTS = \
"CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.obj" \
"CMakeFiles\gmock.dir\src\gmock-all.cc.obj"

# External object files for target gmock
gmock_EXTERNAL_OBJECTS =

lib\gmockd.lib: Google_tests\lib\googlemock\CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.obj
lib\gmockd.lib: Google_tests\lib\googlemock\CMakeFiles\gmock.dir\src\gmock-all.cc.obj
lib\gmockd.lib: Google_tests\lib\googlemock\CMakeFiles\gmock.dir\build.make
lib\gmockd.lib: Google_tests\lib\googlemock\CMakeFiles\gmock.dir\objects1.rsp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Dev\university-tasks\homework-cpp\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library ..\..\..\lib\gmockd.lib"
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	$(CMAKE_COMMAND) -P CMakeFiles\gmock.dir\cmake_clean_target.cmake
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	"C:\Program Files (x86)\MICROS~1\2019\COMMUN~1\VC\Tools\MSVC\1423~1.281\bin\Hostx86\x86\link.exe" /lib /nologo /machine:X86 /out:..\..\..\lib\gmockd.lib @CMakeFiles\gmock.dir\objects1.rsp 
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug

# Rule to build all files generated by this target.
Google_tests\lib\googlemock\CMakeFiles\gmock.dir\build: lib\gmockd.lib

.PHONY : Google_tests\lib\googlemock\CMakeFiles\gmock.dir\build

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\clean:
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock
	$(CMAKE_COMMAND) -P CMakeFiles\gmock.dir\cmake_clean.cmake
	cd C:\Dev\university-tasks\homework-cpp\cmake-build-debug
.PHONY : Google_tests\lib\googlemock\CMakeFiles\gmock.dir\clean

Google_tests\lib\googlemock\CMakeFiles\gmock.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" C:\Dev\university-tasks\homework-cpp C:\Dev\university-tasks\homework-cpp\Google_tests\lib\googlemock C:\Dev\university-tasks\homework-cpp\cmake-build-debug C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock C:\Dev\university-tasks\homework-cpp\cmake-build-debug\Google_tests\lib\googlemock\CMakeFiles\gmock.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : Google_tests\lib\googlemock\CMakeFiles\gmock.dir\depend

