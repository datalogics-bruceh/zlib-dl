#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile, CMake


class TestZlibConan(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    build_requires = "cmake_installer/3.12.0@conan/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["WITH_MINIZIP"] = self.options["zlib-dl"].minizip
        cmake.configure()
        cmake.build()

    def test(self):
        assert os.path.exists(os.path.join(self.deps_cpp_info["zlib-dl"].rootpath, "licenses", "LICENSE"))
        if "x86" in self.settings.arch:
            self.run(os.path.join("bin", "test"), run_environment=True)
            if self.options["zlib"].minizip:
                self.run(os.path.join("bin", "test_minizip"), run_environment=True)
