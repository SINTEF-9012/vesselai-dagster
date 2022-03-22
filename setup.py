import setuptools

setuptools.setup(
    name="vesselai_dagster",
    packages=setuptools.find_packages(exclude=["vesselai_dagster_tests"]),
    install_requires=[
        "dagster==0.14.5",
        "dagit==0.14.5",
        "pytest",
    ],
)
