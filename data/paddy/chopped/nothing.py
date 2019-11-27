import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paddy",
    version="0.1",
    author="Fendy Prayogi",
    author_email="prayogifendy@gmail.com",
    description="Identifikasi Lahan Pertanian Menggunakan CNN pada Citra Google Earth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
