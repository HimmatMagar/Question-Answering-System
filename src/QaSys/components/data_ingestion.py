import os
import zipfile
import urllib.request as r
from QaSys import logger
from QaSys.entity import DataIngestionConfig

class DataIngeston:
      def __init__(self, config: DataIngestionConfig):
            self.config = config

      def download_file(self):
            if not os.path.exists(self.config.zip_file):
                  filename, header = r.urlretrieve(
                        url = self.config.source_url,
                        filename=self.config.zip_file
                  )
                  logger.info(f"{filename} download with fillowing {header}")
            else:
                  logger.info("file already exist")
            
      
      def unzip_file(self):
            file = self.config.unzip_file
            os.makedirs(file, exist_ok=True)
            with zipfile.ZipFile(self.config.zip_file, 'r') as f:
                  f.extractall(file)