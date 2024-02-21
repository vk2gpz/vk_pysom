import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vk_pysom",
    version="1.0.0",
    author="vk2gpz",
    author_email="vk2gpz@gmail.com",
    license='LGPL',
    description="A collection of Self-Organizing Map related modules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vk2gpz/vk_pysom",
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_namespace_packages(include=['vk_pysom.*']),
    python_requires=">=3.9",
    install_requires=[
          'vk_pygeom @ git+ssh://git@github.com/vk2gpz/vk_pygeom@main',
      ],
)
