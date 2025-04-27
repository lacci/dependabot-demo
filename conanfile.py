from conan import ConanFile

class HelloConan(ConanFile):
  name = "hello"
  version = "0.1"
  description = """This is a Hello World library.
                    A fully featured, portable, C++ library to say Hello World in the stdout,
                    with incredible iostreams performance"""
  requires = "boost/1.86.0", "botan/3.4.0", "date/3.0.3", "glog/0.7.1", "gsl-lite/0.40.0", "rapidjson/cci.20230929", "utf8proc/2.9.0", "nonexisting/1.0.0", "zlib/1.3.1"
