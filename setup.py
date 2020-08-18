from distutils.core import setup
import setuptools

setup(
    name="cc3220tool",
    version="0.2.0",
    description="A tool to upload files to TI CC3220",
    author="Kiril Zyapkov",
    author_email="k.zyapkov@allterco.com",
    url="https://github.com/AudigoLabs/cc3200tool",
    packages=setuptools.find_packages(),
    package_data={'cc3220tool': ['dll/gen2/*.ptc']},
    scripts=[
                'scripts/cc3220tool',
            ],
    install_requires=['pyserial', 'progress'],
)
