from conan import ConanFile

class HelloConan(ConanFile):
  name = "hello"
  version = "0.1"
  description = """This is a Hello World library.
                    A fully featured, portable, C++ library to say Hello World in the stdout,
                    with incredible iostreams performance"""
  requires = "boost/1.86.0", "botan/3.6.1", "date/3.0.3", "glog/0.7.1", "gsl-lite/0.40.0", "libxml2/2.13.6", "openssl/3.1.8", "rapidjson/cci.20230929", "utf8proc/2.9.0", "zlib/1.3.1"
