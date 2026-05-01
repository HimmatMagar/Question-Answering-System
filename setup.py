import setuptools

__version__ = '0.0.0.0'

REPO_NAME = "Question-Answering-System-GPT"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "QaGPT"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"

setuptools.setup(
      name="QaGPT",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End GPT model implementation for question answering system",
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
      },
      package_dir={"": "src"},
      packages=setuptools.find_packages(where='src')
)