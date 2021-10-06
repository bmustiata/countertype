package(default_visibility = ["PUBLIC"])

subinclude("//_build/please:python.plz")

python_library(
  name="countertype-lib",
  srcs=glob(["countertype/**/*.py"]),
)

ge_python_library(
  name="countertype",
  srcs=glob(["countertype/**/*.py"]),
)
